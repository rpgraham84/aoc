#!/usr/bin/env python


def get_input(day, number=1):
    with open(f"./inputs/day-{day}-number-{number}.txt") as f:
        return f.read().strip().splitlines()