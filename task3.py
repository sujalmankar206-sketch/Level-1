import re

def is_valid_email(email):
    # Regex framework checking for characters, an '@' symbol, a domain name, and a dot extension
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    return False

# Interactive loop for user input
print("--- Email Validator ---")
print("Type 'exit' to quit the program.\n")

while True:
    user_input = input("Enter an email to validate: ").strip()
    
    # Check if the user wants to quit
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
        
    # Skip empty inputs
    if not user_input:
        print("Please enter a valid string.")
        continue
    
    # Validate and print result
    is_valid = is_valid_email(user_input)
    print(f"Result -> Valid: {is_valid}\n")