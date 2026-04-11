"""
In this lab you will practice the basics of Python by building a small app that creates a character for an RPG adventure.
"""

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

full_dot = "●"
empty_dot = "○"


def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if not name:
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if (
        not isinstance(strength, int)
        or not isinstance(intelligence, int)
        or not isinstance(charisma, int)
    ):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    result = f"{name}\nSTR {strength * full_dot}{(10 - strength) * empty_dot}\nINT {intelligence * full_dot}{(10 - intelligence) * empty_dot}\nCHA {charisma * full_dot}{(10 - charisma) * empty_dot}"
    return result


test = create_character("ren", 4, 2, 1)
print(test)
