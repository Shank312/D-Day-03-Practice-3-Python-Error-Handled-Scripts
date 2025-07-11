
# 🎯 Goal: Ask user to enter a number, and reject non-numeric inputs gracefully using try/except.

def get_valid_number():
    while True:
        try:
            num = float(input("Enter a number: "))
            print(f"✅ You entered: {num}")
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

# Call the function
get_valid_number()            