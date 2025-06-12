
# list comprehension working
# [expression for item in iterable if condition]

# expression: The transformation or value to be included in the new list.
# item: The current element taken from the iterable.
# iterable: A sequence or collection (e.g., list, tuple, set).
# if condition (optional): A filtering condition that decides whether the current item should be included.

matrix = [[col for col in range(8)] for row in range(8)]
print(matrix)

matrixs = [[item for item in range(4)] for x in range(20)]
print(matrixs)