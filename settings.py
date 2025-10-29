from typing import (Literal,
                    Callable)
from choicesorts import (simpleChoiceSort,
                         doubleChoiceSort)

from insertionsorts import (simpleInsertionSort,
                            insertionSortWithAppend,
                            insertionSortWithBinSearch,
                            insertionShellSort)

from quicksort import quickSortByHalf
from swapingsorts import (simpleBubbleSort,
                          bubbleSortWithFlag,
                          shakerSort)


MAX_INT_VALUE: int = int(1e6)
MIN_INT_VALUE: int = -MAX_INT_VALUE

SORTING_FUNCTIONS: list[Callable[[list[int]], None]] = [
    simpleBubbleSort, bubbleSortWithFlag, shakerSort,
    simpleInsertionSort, insertionSortWithAppend,
    insertionSortWithBinSearch, insertionShellSort,
    simpleChoiceSort, doubleChoiceSort,
    quickSortByHalf
]

SORTING_NAMES: list[str] = [
        "Обменная сортировка: сортировка пузырьком",
        "Обменная сортировка: сортировка пузырьком с флагом",
        "Обменная сортировка: шейкер-сортировка ",
        "Сортировка вставками: метод простых вставок",
        "Сортировка вставками: вставки с барьером",
        "Сортировка вставками: метод вставок с бинарным поиском",
        "Сортировка вставками: метод Шелла",
        "Простая сортировка выбором",
        "Двунаправленная сортировка выбором",
        "Быстрая сортировка"
]

MAX_LEN_OF_SORTING_NAME: int = len(max(SORTING_NAMES, key=lambda x: len(x)))

SORTING_INDEXES: list[int] = list(range(len(SORTING_FUNCTIONS)))

INPUT_DATA_COUNT_FOR_ALL: int = 7
INPUT_DATA_COUNT_FOR_ONE: int = 10

TESTCASE_ITERATION_CONSTANTS: list[int] = [5, 2]

CALC_ALL_ALGORITHMS_CMD: str = "all"
CALC_ONE_ALGORITHM_CMD: str = "calc"
SHOW_GRAPHIC_CMD: str = "show"
SHOW_DOCUMENTATION_CMD: str = "help"

DEV_MODE_ARGUMENT: str = "--dev"

HelpCmd = Literal["decl", "all", "calc",
                    "show", "help", "inds"]

PROGRAM_CMD_LIST: list[str] = [CALC_ALL_ALGORITHMS_CMD,
                               CALC_ONE_ALGORITHM_CMD,
                               SHOW_GRAPHIC_CMD,
                               SHOW_DOCUMENTATION_CMD]

HELP_CMD_LIST: list[str] = PROGRAM_CMD_LIST + ["decl", "inds"]

def getCsvFileName(index: int) -> str:
    if index not in SORTING_INDEXES:
        raise IndexError("Index must be in diaposon of"+
                         f"[0, {SORTING_INDEXES[-1]}]")
    
    return f"table_of_{index}.csv"