"""
2.Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}

 Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

# Create three dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create an empty dictionary
result = {}

# Add all key-value pairs from dic1
result.update(dic1)

# Add all key-value pairs from dic2
result.update(dic2)

# Add all key-value pairs from dic3
result.update(dic3)

# Display the concatenated dictionary
print(result)

# Output
"""
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
