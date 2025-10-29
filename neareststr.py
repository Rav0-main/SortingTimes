def _getSimilarityPercentage(str1: str, str2: str):
    return 1 - _levensteinDistance(str1, str2) / max(len(str1), len(str2))

def _levensteinDistance(str1: str, str2: str):
    n, m = len(str1), len(str2)
    if n > m:
        str1, str2 = str2, str1
        n, m = m, n

    currentRow = range(n + 1)
    for i in range(1, m + 1):
        previousRow, currentRow = currentRow, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previousRow[j] + 1, currentRow[j - 1] + 1, previousRow[j - 1]
            if str1[j - 1] != str2[i - 1]:
                change += 1
            currentRow[j] = min(add, delete, change)

    return currentRow[n]

def getNearestStrOf(source: str, dist: list[str]) -> str:
    result: str = ""
    maxValue: float = 0.0
    for example in dist:
        value = _getSimilarityPercentage(source, example)
        if maxValue < value:
            result = example
            maxValue = value

    return result