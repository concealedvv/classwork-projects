import numpy as np

indexAndSliceArray = np.array([x for x in range(1, 16)]).reshape(3,5)

print(indexAndSliceArray)

print()

row2OfindexAndSliceArray = np.array(indexAndSliceArray[1])

print(row2OfindexAndSliceArray)

print()

column5OfindexAndSliceArray = np.array(indexAndSliceArray[:, 4]) # use 4 instead of 5 because of zero indexing

print(column5OfindexAndSliceArray)

print()

rows0and1Ofrow2OfindexAndSliceArray = np.array(indexAndSliceArray[0:2])

print(rows0and1Ofrow2OfindexAndSliceArray)

print()

columns2and4OfindexAndSliceArray = np.array(indexAndSliceArray[:, 2:5])

print(columns2and4OfindexAndSliceArray)

print()

row1andColumn4OfindexAndSliceArray = np.array(indexAndSliceArray[0][3])

print(row1andColumn4OfindexAndSliceArray)

print()

rowOneAndTwoInColumnsZeroTwoAndFour = np.array(indexAndSliceArray[0:2], [0, 2, 4])

print(rowOneAndTwoInColumnsZeroTwoAndFour)

print()