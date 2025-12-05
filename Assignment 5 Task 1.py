# Task 1: Student Marks Dictionary Program

# Step 1: Create a dictionary with student names as keys and marks as values
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 88
}

print("Available students and their marks:")
for name, marks in student_marks.items():
    print(f"{name}: {marks}")

# Step 2: Get user input for student's name
name = input("\nEnter a student's name: ")

# Step 3: Retrieve and display marks or show not found message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the dictionary.")
