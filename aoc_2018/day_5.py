#!/usr/bin/env python3
"""
--- Day 5: Alchemical Reduction ---
You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

In aA, a and A react, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned? (Note: in this puzzle and others, the input is large; if you copy/paste your input, make sure you get the whole thing.)
"""
from utils import get_input


def same_type(a, b):
    return a.lower() == b.lower()


def same_polarity(a, b):
    return (a.islower() and b.islower()) or (a.isupper() and b.isupper())


def reacts(a, b):
    if same_type(a, b):
        return not same_polarity(a, b)

result_hash = {}
def do_reactions(polymer):
    global result_hash
    s_polymer = ''.join(polymer)
    new_polymer = result_hash.get(s_polymer, '')
    if new_polymer:
        return new_polymer

    skip = False
    for i, unit in enumerate(polymer[:-1]):
        next_unit = polymer[i + 1]
        if not skip:
            if reacts(unit, next_unit):
                skip = True
                continue
            new_polymer += unit
        else:
            skip = False

    result_hash[s_polymer] = new_polymer + next_unit

    return new_polymer + next_unit


def part_1(input_list):
    polymer = list(input_list[0])
    post_reaction = do_reactions(polymer)

    while len(post_reaction) > len(do_reactions(post_reaction)):
        post_reaction = do_reactions(post_reaction)

    return len(post_reaction)


def part_2(input_list):
    polymer = input_list[0]
    length_hash = {}
    chars = set(polymer.lower())
    for char in chars:
        test_polymer = polymer.replace(char, '').replace(char.upper(), '')
        length_hash[len(test_polymer)] = part_1([test_polymer])

    return sorted(length_hash.items(), key=lambda x: x[1])[0][1]


if __name__ == "__main__":
    input_list = get_input(5)
    print(f"Part 1: {part_1(input_list)}")
    print(f"Part 2: {part_2(input_list)}")