from time import time
from copy import deepcopy
from typing import (Callable,
                    Any)

class StopwatchOfFunctions:
    def __init__(self, *functs: Callable[..., Any]):
        self.__functs = functs
        self.__functsLength = len(self.__functs)
        self.__times: list[list[float]] = [
            [] for i in range(self.__functsLength)
        ]

    def executeWithAveraging(self, functIndex: int, count: int,
                             *sourceArgs: ...) -> float:
        self.__checkFunctIndex(functIndex)
        if count <= 0:
            raise ValueError("Repeat count must be > 0")

        summaryTime = 0.0
        for i in range(count):
            args = deepcopy(sourceArgs)
            start = time()
            self.__functs[functIndex](*args)

            deltaTime = (time() - start) * 1000

            summaryTime += deltaTime

        deltaTime = summaryTime / count
        self.__times[functIndex].append(deltaTime)
        return deltaTime
    
    def getTimesOf(self, functIndex: int) -> list[float]:
        self.__checkFunctIndex(functIndex)

        return self.__times[functIndex]

    def __checkFunctIndex(self, functIndex: int):
        if functIndex >= self.__functsLength or functIndex < -self.__functsLength:
            raise IndexError(
                f"functIndex={functIndex} must be < {self.__functsLength} " +
                f"and > {-self.__functsLength}"
                 )
        
    @property
    def functsCount(self) -> int:
        return self.__functsLength