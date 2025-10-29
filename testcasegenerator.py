from random import randint

def getDecreasingArray(length: int, start: int, end: int) -> list[int]:
    if start > end:
        raise ValueError(f"start={start} must be <= end={end}")
    
    pastValue: int = end
    array: list[int] = []
    for i in range(length):
        array.append(
            randint(min(pastValue, start+length-i-1), pastValue)
        )
        pastValue = array[-1]

    return array