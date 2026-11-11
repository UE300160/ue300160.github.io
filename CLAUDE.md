# UE300160 dashboard

GitHub Pages site (built by Jekyll on GitHub) showing students' progress in a programming course.

## Design rule: students' PRs must never conflict
- Each student edits only their own `_data/students/<firstname>.yml` (last initial if taken: `anna-k.yml`).
  Never move student data back into `index.html` or into any shared file students edit.
- `_data/rosalind.json` and `_data/aoc.json` are written only by the daily Action
  (`.github/workflows/progress.yml` → `.github/scripts/update_progress.py`). Don't hand-edit them.
- Progress targets (`rosalind_target`, `aoc_target`) are set at the top of the student loop in `index.html`.

## Secrets
- `AOC_LEADERBOARD_URL` (repository secret) holds the AoC view-only link. Never put it, or the
  leaderboard join code, in the repo: the repo and its Action logs are public.
- AoC asks for at most one leaderboard request per 15 minutes.

## Local preview
macOS's built-in Ruby (2.6) is too old for Jekyll; use Homebrew Ruby or chruby, then `jekyll serve`.
