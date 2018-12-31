#!/usr/bin/env python3
import numpy as np
from collections import Counter
from string import ascii_letters
from utils import get_input


def get_coords(input_list):
    return sorted([tuple(map(int, map(str.strip, c.split(",")))) for c in input_list])


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_distances(coords, root=(0, 0)):
    distances = {}
    for counter, coord in enumerate(coords, start=1):
        distances[counter] = manhattan(root, coord)

    return distances


def get_closest(coords, root=(0, 0)):
    distances = get_distances(coords, root)
    lowest = sorted(distances.items(), key=lambda x: x[1])[:2]
    if lowest[0][1] == lowest[1][1]:
        return 0
    else:
        return lowest[0][0]


def minimize_coords(coords):
    amin = np.amin(coords, 0)
    return np.array([(x - amin[0], y - amin[1]) for x, y in coords])


def make_grid(coords):
    coords = minimize_coords(coords)
    amax = np.amax(coords, 0)
    grid = np.zeros([x + 1 for x in amax], dtype=int)
    for counter, coord in enumerate(coords, start=1):
        grid[coord[0]][coord[1]] = counter

    return coords, grid


def is_under_limit(limit, coords, root=(0, 0)):
    distances = get_distances(coords, root)
    return sum(distances.values()) < limit


def part_1(coords, grid):
    amax = np.amax(coords, 0)
    infinite_areas = set()
    for row in range(grid.shape[1]):
        for col in range(grid.shape[0]):
            closest = get_closest(coords, (col, row))
            grid[col][row] = closest
            if any((row in (0, amax[0] + 1), col in (0, amax[1] + 1))):
                infinite_areas.add(closest)

    areas = sorted(Counter(grid.flatten()).items(), key=lambda x: x[1])
    return [a[1] for a in areas if a[0] not in infinite_areas][-1]


def part_2(coords, grid):
    area = 0
    for row in range(grid.shape[1]):
        for col in range(grid.shape[0]):
            if is_under_limit(10000, coords, (col, row)):
                area += 1
    return area


if __name__ == "__main__":
    input_list = get_input(6, 1)
    coords, grid = make_grid(np.array(get_coords(input_list)))
    print(f"Part 1: {part_1(coords, grid)}")
    print(f"Part 2: {part_2(coords, grid)}")
