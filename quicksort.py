def quickSortByEnd(array: list[int]):
    left = 0
    right = len(array)-1
    stack: list[tuple[int, int]] = [(left, right)]

    while stack:
        left, right = stack.pop()
        if left < right:
            flag = array[right]
            i = left - 1
            for j in range(left, right):
                if array[j] <= flag:
                    i += 1
                    array[i], array[j] = array[j], array[i]

            i += 1
            array[i], array[right] = array[right], array[i]

            stack.append((left, i-1))
            stack.append((i+1, right))

def quickSortByHalf(array: list[int]) -> None:
    n = len(array)
    stack: list[tuple[int, int]] = [(0, n-1)]

    while stack:
        left, right = stack.pop()
        if right - left > 0:
            flag = array[left + (right-left) // 2]

            i = left
            j = right
            while i <= j:
                while array[i] < flag and i <= n-1:
                    i += 1
                while array[j] > flag and j >= 0:
                    j -= 1

                if i > j:
                    break

                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

            stack.append((left, j))
            stack.append((i, right))