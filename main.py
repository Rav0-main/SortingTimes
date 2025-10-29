from screen import (calcAllAlgorithms,
                    calcOneAlgorithm,
                    showGraphicsOf)

from outputer import (printWarning,
                      printError,
                      titleScreen)

from documentation import (printDocumentationsOf,
                           printFullDocumentation)

from sys import argv

from settings import (SORTINGS_INDEXES,
                      PROGRAM_CMD_LIST,
                      CALC_ALL_ALGORITHMS_CMD,
                      CALC_ONE_ALGORITHM_CMD,
                      SHOW_GRAPHIC_CMD,
                      SHOW_DOCUMENTATION_CMD,
                      DEV_MODE_ARGUMENT)

from neareststr import getNearestStrOf

def isDevelopingMode():
    return argv[-1] == DEV_MODE_ARGUMENT

def main():
    if isPromptToCalcAllAlgorithms():
        titleScreen("Подсчет всех алгоритмов.")
        if len(argv) == 2:
            printError(f"\033[1mНеполные аргументы команды '{CALC_ALL_ALGORITHMS_CMD}'.\033[0m\n"+
                  "Введите количество повторений 'ind'-ой сортировки для усреднения"+
                   " времени выполнения.\n"+
                  f"Для справки используйте 'python main.py {SHOW_DOCUMENTATION_CMD} {CALC_ALL_ALGORITHMS_CMD}'.")
            
            return
            
        elif not argv[2].isdigit() or int(argv[2]) <= 0:
            printError(f"\033[1mНеверный тип аргументов команды '{CALC_ALL_ALGORITHMS_CMD}'.\033[0m\n"+
                  "Аргумент должен быть 'repeat>0'.\n"+
                  f"Для справки используйте 'python main.py {SHOW_DOCUMENTATION_CMD} {CALC_ALL_ALGORITHMS_CMD}'.")
            
            return

        countOfOneExecution = int(argv[2])
        calcAllAlgorithms(countOfOneExecution)

    elif isPromptToPrintDocumentation():
        titleScreen("Справка.")
        commandList: list[str] = argv[2:]
        if commandList == []:
            printFullDocumentation()
        else:
            printDocumentationsOf(commandList)

    elif isPromptToCalcOneAlgorithm():
        titleScreen("Подсчет одного алгоритма.")
        if len(argv) == 2:
            printError("\033[1mНе введен индекс сортировки ('ind').\033[0m\n"+
                       f"Для справки используйте 'python main.py {SHOW_DOCUMENTATION_CMD} {CALC_ONE_ALGORITHM_CMD}'.")
            return 
            
        elif not argv[2].isdigit():
            printError("\033[1mИндекс сортировки ('ind') должен быть целым числом.\033[0m\n"+
                       f"Для справки используйте 'python main.py {SHOW_DOCUMENTATION_CMD} {CALC_ONE_ALGORITHM_CMD}'.")
            return 
        
        sortingIndex = int(argv[2])

        if sortingIndex not in SORTINGS_INDEXES:
            printError(
                "\033[1mНеверный индекс сортировки ('ind').\033[0m\n"+
                f"Индекс сортировки должен быть в отрезке [{min(SORTINGS_INDEXES)}, {max(SORTINGS_INDEXES)}].\n"+
                f"Для справки используйте 'python main.py {SHOW_DOCUMENTATION_CMD} {CALC_ONE_ALGORITHM_CMD}'."
            )
            
            return

        elif len(argv) == 3 or not argv[3].isdigit() or int(argv[3]) <= 0:
            printError(
                "\033[1mНеверные аргументы при выборе сортировки ('ind').\033[0m\n"+
                "Должно содержаться 'repeat>0'.\n"+
                f"Для справки используйте 'python main.py {SHOW_DOCUMENTATION_CMD} {CALC_ONE_ALGORITHM_CMD}'."
            )
            
            return
        
        elif len(argv) >= 5 and argv[4] != "+d":
            printWarning("\033[1mНерекомендуемое значение аргумента.\033[0m\n"+
                         "Третье значение рекомендуется '+d', если нужно отобразить график,\n"+
                         "иначе опускать.\n"+
                         f"Для справки используйте 'python main.py {SHOW_DOCUMENTATION_CMD} {CALC_ONE_ALGORITHM_CMD}'.\n")

        needDrawGraphic: bool = argv[4] == "+d" if len(argv) >= 5 else False
        countOfOneExecution = int(argv[3])

        calcOneAlgorithm(sortingIndex, needDrawGraphic, countOfOneExecution)

    elif isPromptToShowGraphic():
        titleScreen("График.")
        sortingIndexes: list[str] = argv[2:]
        showGraphicsOf(sortingIndexes)

    else:
        printError(
            "\033[1mНеопознанный запрос.\033[0m\n" +
            f"Для справки используйте 'python main.py {SHOW_DOCUMENTATION_CMD}'."
        )
        
        if len(argv) >= 2:
            nearestCommand = getNearestStrOf(argv[1], PROGRAM_CMD_LIST)
            if nearestCommand != "":
                print(f"Возможно вы имели ввиду: \033[1m{nearestCommand}\033[0m?")
        
        return

def isPromptToCalcAllAlgorithms():
    return len(argv) >= 2 and argv[1] == CALC_ALL_ALGORITHMS_CMD

def isPromptToPrintDocumentation():
    return len(argv) >= 2 and argv[1] == SHOW_DOCUMENTATION_CMD

def isPromptToCalcOneAlgorithm():
    return len(argv) >= 2 and argv[1] == CALC_ONE_ALGORITHM_CMD

def isPromptToShowGraphic():
    return len(argv) >= 2 and argv[1] == SHOW_GRAPHIC_CMD
        
if __name__ == "__main__":
    needOutputErrors = isDevelopingMode()
    if isDevelopingMode():
        argv = argv[:len(argv)-1]

    try:
            main()

    except BaseException as error:
        if not needOutputErrors:
            printWarning("\033[1mАварийное завершение программы.\033[0m")

        else:
            raise error