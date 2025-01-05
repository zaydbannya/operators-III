
def print_ascii_codes():
    print("ASCII codes for uppercase alphabets:")
    for char in range(65, 91):
        print(f"{chr(char)}: {char}")
    print("\nASCII codes for lowercase alphabets:")
    for char in range(97, 123):
        print(f"{chr(char)}: {char}")
print_ascii_codes()