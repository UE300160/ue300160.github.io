#!/usr/bin/env python

from util import read_input

def parse_slot_machines(text):
    slot_machines = []
    for line in text:
        if line.startswith('Button A'):
            info = line.split(':')[1]
            a = info.split(',')
            ax = int(a[0].split('+')[1])
            ay = int(a[1].split('+')[1])
        elif line.startswith('Button B'):
            info = line.split(':')[1]
            b = info.split(',')
            bx = int(b[0].split('+')[1])
            by = int(b[1].split('+')[1])
        elif line.startswith('Prize'):
            info = line.split(':')[1]
            p = info.split(',')
            px = int(p[0].split('=')[1])
            py = int(p[1].split('=')[1])
        else:
            slot_machines.append([ax, ay, bx, by, px, py])
    return slot_machines
            

# def 

def main():
    slots = read_input('../aoc_data/day13_test.txt')
    machines = parse_slot_machines(slots)
    print(machines)

if __name__ == '__main__':
    main()