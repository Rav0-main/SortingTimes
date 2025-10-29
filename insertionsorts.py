def simpleInsertionSort(array: list[int]) -> None:
    for i, value in enumerate(array):
        j = i-1
        while array[j] > value and j >= 0:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = value

def insertionSortWithAppend(array: list[int]) -> None:
    n = len(array)
    array.append(0)
    for i in range(1, n):
        if array[i - 1] > array[i]:
            array[-1] = array[i]
            j = i - 1
            while array[j] > array[-1]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = array[-1]

    array.pop()

def insertionSortWithBinSearch(array: list[int]) -> None:
    for i, value in enumerate(array):
        left = 0
        right = i-1
        while left < right:
            middle = left + (right - left) // 2
            if value < array[middle]:
                right = middle
            else:
                left = middle + 1

        for j in range(i, left+1, -1):
            array[j] = array[j-1]

        array[left] = value

def insertionShellSort(array: list[int]):
    dist = len(array) // 2
    while dist:
        for i, value in enumerate(array):
            while i >= dist and array[i - dist] > value:
                array[i] = array[i - dist]
                i -= dist
            array[i] = value
        dist = 1 if dist == 2 else int(dist * 5.0 / 11)