#!/usr/bin/env python

# sentient rocks
from util import read_input
import copy
import sys

def blink(stones):
    new_stones = []
    for stone in stones:
        engraving = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(engraving) % 2 == 0:
            first_half = int(engraving[:len(engraving)//2])
            second_half = int(engraving[len(engraving)//2:])
            new_stones.append(first_half)
            new_stones.append(second_half)
        else:
            new_stones.append(stone * 2024)
    return new_stones

def main():
    sys.set_int_max_str_digits(10000)
    stone_row = read_input('../aoc_data/day11.txt')[0]
    stones = stone_row.split()
    total = 0
    # for stone in stones:
    # test = [125, 17]
    for _ in range(25):
        stones = blink(stones)
    
    print(len(stones))

if __name__ == '__main__':
    main()