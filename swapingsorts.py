def simpleBubbleSort(array: list[int]) -> None:
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def bubbleSortWithFlag(array: list[int]) -> None:
    n = len(array)
    swapped: bool = False
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            break

def shakerSort(array: list[int]) -> None:
    n = len(array)

    start = 0
    end = n - 1
    swapped: bool = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if array[i] > array[i+1]:
                array[i+1], array[i] = array[i], array[i+1]
                swapped = True

        if not swapped: break

        end -= 1
        for i in range(end, start, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                swapped = True

        start += 1