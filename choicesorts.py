def simpleChoiceSort(array: list[int]) -> None:
    n = len(array)
    for i in range(n):
        minValueIndex = min(range(i, n), key=lambda x: array[x])
        array[i], array[minValueIndex] = array[minValueIndex], array[i]

def doubleChoiceSort(array: list[int]) -> None:
    n = len(array)
    for i in range(n//2):
        minValueIndex = min(range(i, n-i), key=lambda x: array[x])
        maxValueIndex = max(range(i, n-i), key=lambda x: array[x])

        array[i], array[minValueIndex] = array[minValueIndex], array[i]
        array[n-i-1], array[maxValueIndex] = array[maxValueIndex], array[n-i-1]