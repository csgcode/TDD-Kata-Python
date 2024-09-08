def Add(numbers: str) -> int:
    """A python function to add numbers from a string"""
    if not numbers:
        return 0

    try:
        int(numbers)
        return int(numbers)
    except ValueError:
        pass

    addends = map(int, numbers.split(","))
    return sum(addends)