# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.

# Create a list
list1 = [10, 45, 23, 67, 12, 89, 5]

# Assume the first element is both the largest and smallest
largest = list1[0]
smallest = list1[0]

# Traverse the list to find the largest and smallest elements
for i in list1:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

# Display the results
print("Largest element = ", largest)
print("Smallest element = ", smallest)

# Output
"""
Largest element = 89
Smallest element = 5
"""
