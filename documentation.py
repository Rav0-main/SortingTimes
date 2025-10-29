from settings import (SORTING_NAMES,
                      HelpCmd,
                      HELP_CMD_LIST,
                      CALC_ALL_ALGORITHMS_CMD,
                      CALC_ONE_ALGORITHM_CMD,
                      SHOW_GRAPHIC_CMD,
                      SHOW_DOCUMENTATION_CMD)

from typing import Callable
from outputer import printWarning
from neareststr import getNearestStrOf

def printFullDocumentation() -> None:
    print("Документация: ")
    print("1) ", end="")
    printDeclaration(len("1) "))

    print("2) Команды: ")
    printAllCommand(0)

    printCalcCommand(0)

    printShowCommand(0)

    printHelpCommand(0)

    print("3) ", end="")
    printSortingIndexes(len("3) "))

"""
'delta' - is shift length of first line by normal
"""

def printDeclaration(delta: int) -> None:
    print("Декларация: python main.py 'cmd' ['args'...]")
    print()

def printAllCommand(delta: int) -> None:
    print(f"* '{CALC_ALL_ALGORITHMS_CMD}' - Вывод графика всех сортировок,")
    print(" "*delta + "          тестируя каждую по 'repeat' раз для одного размера.")
    print(" "*delta + f"          Syntax: python main.py {CALC_ALL_ALGORITHMS_CMD} 'repeat'")
    print()
    print(" "*delta + "          Аргумент(ы):")
    print(" "*delta + "          ~ 'repeat' - Количество повторений выполнения")
    print(" "*delta + "                       сортировки для усреднения времени.")
    print(" "*delta + "                       Значение: Целое число > 0.")
    print()

def printCalcCommand(delta: int) -> None:
    print(f"* '{CALC_ONE_ALGORITHM_CMD}' - Считает и запоминает время выполнения")
    print(" "*delta + "           определенной сортировки.")
    print(" "*delta + "           По запросу, выводит полученный график.")
    print(" "*delta + f"           Syntax: python main.py {CALC_ONE_ALGORITHM_CMD} 'ind' 'repeat' ['graphic']")
    print()
    print(" "*delta + "           Аргумент(ы):")
    print(" "*delta + "           ~ 'ind' - Индекс определенной сортировки.")
    print(" "*delta + "                     см. 'Индексы сортировок'.")
    print(" "*delta + "                     Значение: Целое число >= 0.")
    print(" "*delta + "           ~ 'repeat' - Количество повторений выполнения")
    print(" "*delta + "                        сортировки для усреднения времени.")
    print(" "*delta + "                        Значение: Целое число > 0.")
    print(" "*delta + "           ~ 'graphic' - Необязательный параметр для отображения")
    print(" "*delta + "                         графика по расчитанным данным.")
    print(" "*delta + "                         Значение: +d, иначе принимается за отсутствие.")
    print()

def printShowCommand(delta: int) -> None:
    print(f"* '{SHOW_GRAPHIC_CMD}' - Выводит на графике данные о времени,")
    print(" "*delta + "           созданные отдельно для каждой подсчитанной сортировки.")
    print(" "*delta + f"           Syntax: python main.py {SHOW_GRAPHIC_CMD} ['ind'...]")
    print()
    print(" "*delta + "           Аргумент(ы):")
    print(" "*delta + "           ~ 'ind'... - Необязательный параметр, имеющий множество значений.")
    print(" "*delta + "                        Каждый введенный параметр является индексом сортировки,")
    print(" "*delta + "                        требующий отображение на графике.")
    print(" "*delta + "                        При отсутствии отобразаться данные всех сортировок,")
    print(" "*delta + "                        отдельно посчитанные до этого.")
    print()

def printHelpCommand(delta: int) -> None:
    print(f"* '{SHOW_DOCUMENTATION_CMD}' - Вывод всей справки или справки по командам.")
    print(" "*delta + f"           Syntax: python main.py {SHOW_DOCUMENTATION_CMD} ['cmd'...]")
    print()

def printSortingIndexes(delta: int) -> None:
    print("Индексы сортировок ('inds'):")
    for i, sortingName in enumerate(SORTING_NAMES):
        print(" "*delta + f"* {i} - {sortingName}")
    print()

_CommandDocs: dict[HelpCmd | str, Callable[[int], None]] = {
    "decl": printDeclaration,
    CALC_ALL_ALGORITHMS_CMD: printAllCommand,
    CALC_ONE_ALGORITHM_CMD: printCalcCommand,
    SHOW_GRAPHIC_CMD: printShowCommand,
    SHOW_DOCUMENTATION_CMD: printHelpCommand,
    "inds": printSortingIndexes
}

def printDocumentationsOf(commandList: list[str]):
    hashedCommandList: dict[str, bool] = {}
    k: int = 0
    for i in range(len(commandList)):
        textCommand = commandList[i]
        if commandList[i] not in hashedCommandList:
            commandList[k] = commandList[i]
            k += 1

        hashedCommandList[textCommand] = True
    
    commandList = commandList[:k]
    skippedCount: int = 0
    indexesOfWrongTextCommand: list[int] = []
    for i, textCommand in enumerate(commandList):
        if textCommand not in _CommandDocs:
            indexesOfWrongTextCommand.append(i)
            skippedCount += 1
            continue

        print(f"{i+1-skippedCount}) ", end="")
        _CommandDocs[textCommand](len(f"{i+1-skippedCount}) "))

    for wrongTextCommand in map(lambda x: commandList[x], indexesOfWrongTextCommand):
        printWarning(f"Команда: \033[1m{wrongTextCommand}\033[0m не найдена.")
        nearestCommand = getNearestStrOf(wrongTextCommand, HELP_CMD_LIST)
        if nearestCommand != "":
            print(f"Возможно вы имели ввиду: \033[1m{nearestCommand}\033[0m?", end="")
        print()

if __name__ == "__main__":
    printFullDocumentation()