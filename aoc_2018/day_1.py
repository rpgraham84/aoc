#!/usr/bin/env python3
from collections import defaultdict
from utils import get_input


def part_1(input_list):
    return sum(map(int, input_list))


def part_2(input_list, frequency=0, max_iterations=1000):
    frequency_counter = defaultdict(int)
    frequency_counter[frequency] += 1

    for _ in range(max_iterations):
        for delta in map(int, input_list):
            frequency += delta
            frequency_counter[frequency] += 1
            if frequency_counter[frequency] > 1:
                return frequency


if __name__ == "__main__":
    input_list = get_input(1)
    print(f"Part 1: {part_1(input_list)}")
    print(f"Part 2: {part_2(input_list)}")