# Task 2: List Slicing Demonstration

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original list (1-10):", numbers)

# Step 2: Extract first five elements using slicing [0:5]
first_five = numbers[0:5]
print("First five elements:", first_five)

# Step 3: Reverse the extracted elements using slicing [::-1]
reversed_five = first_five[::-1]
print("Reversed first five:", reversed_five)
