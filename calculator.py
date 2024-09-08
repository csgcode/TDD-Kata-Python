import re
import logging

DEFAULT_DELIMITER = ","

def comma_separator(sequence):
    """function to join a list of comma separated numbers
    ref: https://stackoverflow.com/a/32008908
    """
    if not sequence:
        return ''
    if len(sequence) == 1:
        return sequence[0]

    return ",".join(map(str, sequence))

def Add(numbers: str) -> int:
    """A python function to add numbers from a string"""
    if not numbers:
        return 0
    delimiter = DEFAULT_DELIMITER
    delimiter_search_pattern = r"^//(.+?)\n(.+)$"

    if match := re.match(delimiter_search_pattern, numbers):
        delimiter = re.escape(match.group(1))
        numbers = match.group(2)

    addends = list(map(int, re.split(f"{delimiter}|\n", numbers)))
    negative_numbers = [number for number in addends if number < 0]

    if negative_numbers:
        raise Exception(f"negative numbers not allowed {comma_separator(negative_numbers)}")
    return sum(addends)
