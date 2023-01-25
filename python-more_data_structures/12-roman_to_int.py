#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or None:
        return 0

    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0
    for i, c in enumerate(roman_string):
        if (i + 1) == len(roman_string) or rom[c] >= rom[roman_string[i + 1]]:
            val += rom[c]
        else:
            val -= rom[c]
    return val
