# Safe Division Calculator (Using try-except)
# 🎯 Goal: Build a calculator that divides two numbers safely and handles ZeroDivisionError and ValueError.

def safe_division():
    try:
        numerator = float(input("Enter Numerator: "))
        denominator = float(input("Enter Denominator: "))

        result = numerator/denominator
        print(f"Result: {result:.2f}")

    except ZeroDivisionError:
        print("❌ Error: You can't divide by zero!")  

    except ValueError:
        print("❌ Error: Please enter valid numbers!")  

    except Exception as e:
        print(f"⚠️ unexpexted error: {e}")

# Call the function
safe_division()  
