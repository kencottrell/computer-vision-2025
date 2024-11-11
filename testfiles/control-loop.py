input_list = []

while True:
    # Input loop
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    input_list.append(user_input)

# Output loop
print("You entered:")
for item in input_list:
    print(item)