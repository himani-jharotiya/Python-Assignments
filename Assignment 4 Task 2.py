# Step 1: Take user input and write to file
user_input = input("Enter text to write to output.txt: ")
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')
print("Initial data written to output.txt.")

# Step 2: Append additional data
additional_data = "This is appended data."
with open('output.txt', 'a') as file:
    file.write(additional_data + '\n')
print("Additional data appended to output.txt.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open('output.txt', 'r') as file:
    for line in file:
        print(line.strip())
