
# 🎯 Goal: Open a file entered by the user, handle FileNotFoundError, and read content safely.

def open_file_safely():
    try:
        filename = input("Enter the file name : ")

        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:\n", content)

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the file name.")

    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# Call the function
open_file_safely() 