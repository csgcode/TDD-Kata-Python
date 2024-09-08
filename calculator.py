import re
import logging

DEFAULT_DELIMITER = ","

def Add(numbers: str) -> int:
    """A python function to add numbers from a string"""
    if not numbers:
        return 0
    delimiter = DEFAULT_DELIMITER
    delimiter_search_pattern = r"^//(.+?)\n(.+)$"

    if match := re.match(delimiter_search_pattern, numbers):
        delimiter = re.escape(match.group(1))
        numbers = match.group(2)

    try:        
        addends = map(int, re.split(f"{delimiter}|\n", numbers))
        return sum(addends)
    
    except ValueError:
        raise ValueError("Non-numerical input received")
