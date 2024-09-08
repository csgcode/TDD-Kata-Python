import re


def Add(numbers: str) -> int:
    """A python function to add numbers from a string"""
    if not numbers:
        return 0

    try:
        if "," not in numbers:
            return int(numbers)
        addends = map(int, re.split(",|\n", numbers))
        return sum(addends)
    
    except ValueError:
        raise ValueError("Non-numerical input received")
