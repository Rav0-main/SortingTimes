import matplotlib.pyplot as plt
from pandas import (DataFrame,
                    read_csv)

from stopwatch import StopwatchOfFunctions
from testcasegenerator import getDecreasingArray

from settings import *
from outputer import *

from random import shuffle
from os.path import exists as fileExists

_stopwatch = StopwatchOfFunctions(*SORTING_FUNCTIONS)

def calcAllAlgorithms(countOfOneExecution: int):
    sortingIndexes: list[int] = SORTING_INDEXES.copy()
    testcaseSizes: list[int] = []
    i = 1

    print("Выбраны все сортировки.")

    print("Для каждого размера будет высчитываться среднее время")
    print(f"по {countOfOneExecution} выполнениям.")

    for n in generateTestCaseCount(INPUT_DATA_COUNT_FOR_ALL):
        print(f"№{i}")
        print("=" * MAX_LEN_OF_SORTING_NAME)
        print(f"\033[1mРазмер массива: {n}\033[0m")
        testcaseSizes.append(n)

        shuffle(sortingIndexes)
        
        sourceTestcase: list[int] = getDecreasingArray(
            n, MIN_INT_VALUE, MAX_INT_VALUE
        )

        for sortingIndex in sortingIndexes:
            print("\033[3mТестируемая сортировка:\033[0m")
            print(f"\033[91m{SORTING_NAMES[sortingIndex]}\033[0m")
            print("\033[5mВыполнение...\033[0m")

            executionTime = _stopwatch.executeWithAveraging(sortingIndex,
                                                           countOfOneExecution,
                                                           sourceTestcase)

            printCompletion(f"Выполнено за {executionTime:.5f} мс.")

            print("-" * MAX_LEN_OF_SORTING_NAME)

        i += 1
    
    plt.figure(figsize=(12, 6))

    executionTimes: list[float] = []
    for sortingIndex in SORTING_INDEXES:
        executionTimes = _stopwatch.getTimesOf(sortingIndex)
        plt.plot(testcaseSizes,
                 executionTimes,
                 label=SORTING_NAMES[sortingIndex],
                 linewidth=3.1, alpha=0.7)
        
        plt.scatter(testcaseSizes,
                    executionTimes,
                    s=35, marker="o")
        
    plt.title("Время выполнения всех сортировок.")
    plt.xlabel("Длина массива для сортировки, кол-во")
    plt.ylabel("Время сортировки, мс")
    plt.grid(True)
    plt.legend(loc="best")
    plt.show()

def calcOneAlgorithm(sortingIndex: int, needDrawGraphic: bool,
             countOfOneExecution: int) -> None:
    print("Выбрана сортировка:")
    print(f"{SORTING_NAMES[sortingIndex]}")

    print("Для каждого размера массива будет высчитываться среднее время")
    print(f"по {countOfOneExecution} выполнениям.")

    lenOfSortingName: int = len(SORTING_NAMES[sortingIndex])
    testcaseSizes: list[int] = []
    for n in generateTestCaseCount(INPUT_DATA_COUNT_FOR_ONE):
        sourceTestcase: list[int] = getDecreasingArray(
            n, MIN_INT_VALUE, MAX_INT_VALUE
        )

        testcaseSizes.append(n)

        print(f"\033[1mРазмер массива: {n}\033[0m")
        print("\033[5mВыполнение...\033[0m")

        executionTime = _stopwatch.executeWithAveraging(sortingIndex,
                                       countOfOneExecution,
                                       sourceTestcase)
        
        printCompletion(f"Среднее время выполнения: {executionTime:.5f} мс.")
        
        print("-" * (lenOfSortingName+10))

    executionTimes: list[float] = _stopwatch.getTimesOf(sortingIndex)
    if needDrawGraphic:
        plt.plot(testcaseSizes,
                executionTimes,
                label=SORTING_NAMES[sortingIndex],
                linewidth=3.1, alpha=0.7)
    
        plt.scatter(testcaseSizes,
                    executionTimes,
                    s=35, marker="o")
    
        plt.title(f"Время выполнения сортировки: {SORTING_NAMES[sortingIndex]}.")
        plt.xlabel("Длина массива для сортировки, кол-во")
        plt.ylabel("Время сортировки, мс")
        plt.grid(True)
        plt.legend(loc="best")
        plt.show()

    csvFileName: str = getCsvFileName(sortingIndex)
    print(f"Запись данных в {csvFileName}...")

    dataFrame = DataFrame({
        "sizes": testcaseSizes,
        "executionTimes": executionTimes
    })

    try:
        dataFrame.to_csv(f"{csvFileName}", index=False,
                        encoding="utf-8")
        
    except BaseException as error:
        printError("Произошла неизвестная ошибка.")
        raise error
    
    printCompletion(f"Запись данных прошла успешна.")

def generateTestCaseCount(count: int):
    currentCount: int = 1
    for i in range(0, count):
        currentCount *= TESTCASE_ITERATION_CONSTANTS[i % 2]
        yield currentCount

def showGraphicsOf(sortingIndexes: list[str]) -> None:
    filesFound: bool = False
    calculatedSortingIndexes: list[int] = []
    testcaseSizesLengths: list[int] = []
    sortingIndexesToCheck: list[int] = []
    startSortingIndexesLength: int = len(sortingIndexes)
    foundNotValidSortingIndex: bool = False

    if(sortingIndexes == []):
        sortingIndexesToCheck = SORTING_INDEXES
    else:
        k: int = 0
        hashedSortingIndexes: dict[str, bool] = {}
        for i in range(len(sortingIndexes)):
            if(sortingIndexes[i] not in hashedSortingIndexes and
               sortingIndexes[i].isdigit() and
               int(sortingIndexes[i]) in SORTING_INDEXES):
                
                sortingIndexes[k] = sortingIndexes[i]
                k += 1

            elif(sortingIndexes[i] not in hashedSortingIndexes and
                 (not sortingIndexes[i].isdigit() or
                 int(sortingIndexes[i]) not in SORTING_INDEXES)):

                printWarning(f"Введенный индекс: \033[1m{sortingIndexes[i]}\033[0m "+ 
                             "является неверным.")
                foundNotValidSortingIndex = True

            hashedSortingIndexes[sortingIndexes[i]] = True

        sortingIndexes = sortingIndexes[:k]
        sortingIndexesToCheck = list(map(int, sortingIndexes))

    for sortingIndex in sortingIndexesToCheck:
        csvFileName = getCsvFileName(sortingIndex)
        if not fileExists(csvFileName):
            continue

        dataFrame = read_csv(csvFileName)

        testcaseSizes: list[int] = dataFrame["sizes"].tolist()
        executionTimes: list[float] = dataFrame["executionTimes"].to_list()

        plt.plot(testcaseSizes,
                executionTimes,
                label=SORTING_NAMES[sortingIndex],
                linewidth=3.1, alpha=0.7)
    
        plt.scatter(testcaseSizes,
                    executionTimes,
                    s=35, marker="o")
        
        filesFound = True
        
        testcaseSizesLengths.append(len(testcaseSizes))
        calculatedSortingIndexes.append(sortingIndex)
        
    if(not filesFound and startSortingIndexesLength == 0):
        printWarning("Ни одной сортировки до этого не вычислялось.")
        return
    elif(not filesFound):
        if(foundNotValidSortingIndex):
            print("Для справки используйте 'python main.py help show'.")
        return

    print("Вычисленные сортировки: ")
    for i, sortingIndex in enumerate(calculatedSortingIndexes):
        print(f" * {sortingIndex} - {SORTING_NAMES[sortingIndex]}, "+
              f"кол-во входных данных: {testcaseSizesLengths[i]}")

    plt.title(f"Время выполнения вычисленных сортировок.")
    plt.xlabel("Длина массива для сортировки, кол-во")
    plt.ylabel("Время сортировки, мс")
    plt.grid(True)
    plt.legend(loc="best")
    plt.show()