def reverse_string(input_string):
    # Uses slicing to step backward through the string
    return input_string[::-1]

# Get dynamic input from the user
user_input = input("Enter a string to reverse: ")

# Test the function with the user's input
reversed_result = reverse_string(user_input)
print(f"Original: {user_input} -> Reversed: {reversed_result}")