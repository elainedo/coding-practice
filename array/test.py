# arr = [0,1,2,3,4,5,6]
# for element in arr:
#     arr.pop(0)
#     print('x', element)

# Using multiplication (all sublists are the same object)
parent1 = [[None, None, None]] * 2
parent1[0][0] = "X"
print("parent1:", parent1)  # Both sublists will be changed

# Using list comprehension (each sublist is independent)
parent2 = [[None, None, None] for _ in range(2)]
parent2[0][0] = "X"
print("parent2:", parent2)  # Only first sublist will be changed