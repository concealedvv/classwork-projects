import numpy as np

evenListComprehension: list = [x for x in range(2, 19) if x % 2 == 0]

evenNumbersBetween2and18Array = np.array(evenListComprehension).reshape(3,3)

listComprehensionNineBelow: list = [x for x in range (9, 0, -1)]

nineToOneArray = np.array(listComprehensionNineBelow).reshape(3,3)

multipliedArray = evenNumbersBetween2and18Array * nineToOneArray

print(multipliedArray)