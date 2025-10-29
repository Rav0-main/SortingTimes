from sys import stderr
from os import system

def printError(message: str) -> None:
    print(f"\033[91mОшибка!\033[0m {message}", file=stderr)

def printWarning(message: str) -> None:
    print(f"\033[33mВнимание!\033[0m {message}")

def printCompletion(message: str) -> None:
    print(f"\033[92mЗавершено!\033[0m {message}")

def titleScreen(name: str) -> None:
    system(f"title {name}")