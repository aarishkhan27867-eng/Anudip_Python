"""
1. Write a Python program and calculate the mean of the below dictionary. 

test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

Output: 6.2 
"""
# Create a dictionary
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Initialize variables to store the sum and count
total = 0
count = 0

# Traverse the dictionary values
for value in test_dict.values():
    total = total + value
    count = count + 1

# Calculate the mean
mean = total / count

# Display the result
print("Mean =", mean)

# Output
"""
Mean = 6.2
"""
