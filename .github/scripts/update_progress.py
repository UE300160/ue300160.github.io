"""Update the progress data shown on the dashboard.

- Rosalind: each student's "Solved" count -> _data/rosalind.json, keyed by Rosalind username.
- Advent of Code: stars from the private leaderboard -> _data/aoc.json, keyed by GitHub username.
  Students are matched by GitHub username, or by the numeric ID in their optional `aoc` field.
  Skipped when the AOC_LEADERBOARD_URL environment variable is not set.

Run by .github/workflows/progress.yml. Data that cannot be fetched keeps its
previous value, and the script exits non-zero so the failure is visible.
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
STUDENTS_DIR = ROOT / "_data" / "students"
ROSALIND_OUTPUT = ROOT / "_data" / "rosalind.json"
AOC_OUTPUT = ROOT / "_data" / "aoc.json"

SOLVED_RE = re.compile(
    r'<div class="title">\s*Solved\s*</div>\s*<div class="value">\s*(\d+)\s*</div>'
)


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "UE300160-dashboard"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def load_json(path):
    return json.loads(path.read_text()) if path.exists() else {}


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def load_students():
    return [yaml.safe_load(path.read_text()) or {} for path in sorted(STUDENTS_DIR.glob("*.yml"))]


def update_rosalind(students):
    old_counts = load_json(ROSALIND_OUTPUT)
    counts = {}
    ok = True
    for username in sorted({str(s["rosalind"]) for s in students if s.get("rosalind")}):
        url = f"https://rosalind.info/users/{username}/"
        try:
            match = SOLVED_RE.search(fetch(url))
            if match is None:
                raise ValueError(f"no 'Solved' count found on {url}")
            counts[username] = int(match.group(1))
            print(f"rosalind {username}: {counts[username]}")
        except Exception as error:
            print(f"::error::rosalind {username}: {error}")
            ok = False
            if username in old_counts:
                counts[username] = old_counts[username]
        time.sleep(1)
    write_json(ROSALIND_OUTPUT, counts)
    return ok


def leaderboard_json_url(url):
    """Accept the leaderboard page link as well as its .json API link."""
    parts = urllib.parse.urlsplit(url)
    if not parts.path.endswith(".json"):
        parts = parts._replace(path=parts.path.rstrip("/") + ".json")
    return urllib.parse.urlunsplit(parts)


def update_aoc(students):
    url = os.environ.get("AOC_LEADERBOARD_URL")
    if not url:
        print("AOC_LEADERBOARD_URL not set, skipping Advent of Code")
        return True
    try:
        members = json.loads(fetch(leaderboard_json_url(url)))["members"].values()
    except Exception as error:
        # never print the URL: it contains the leaderboard's secret view key
        print(f"::error::aoc leaderboard: {error}")
        return False

    by_id = {str(m["id"]): m for m in members}
    by_name = {m["name"].lower(): m for m in members if m.get("name")}
    stars = {}
    matched = set()
    for student in students:
        github = student.get("github")
        if not github:
            continue
        if student.get("aoc"):
            member = by_id.get(str(student["aoc"]))
        else:
            member = by_name.get(str(github).lower())
        if member is None:
            continue
        stars[str(github)] = member["stars"]
        matched.add(str(member["id"]))
        print(f"aoc {github}: {member['stars']}")

    for member_id, member in by_id.items():
        if member_id not in matched:
            print(f"::warning::aoc member not matched to a student: {member.get('name') or 'anonymous'} (id {member_id})")
    write_json(AOC_OUTPUT, stars)
    return True


def main():
    students = load_students()
    ok = update_rosalind(students)
    ok = update_aoc(students) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
