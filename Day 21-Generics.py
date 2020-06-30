from typing import TypeVar

Element = TypeVar("Element")


def printArray(array: [Element]):
    for element in array:
        print(element)


n = [1, 2, 3]
str1 = ["Hello", "World"]

printArray(n)
printArray(str1)
