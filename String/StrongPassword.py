import os

def minimumNumber(n, password):
    # Character sets
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    # Flags for missing character types
    missing_digit = 1
    missing_lower = 1
    missing_upper = 1
    missing_special = 1
    
    # Check each character in the password
    for char in password:
        if char in numbers:
            missing_digit = 0
        elif char in lower_case:
            missing_lower = 0
        elif char in upper_case:
            missing_upper = 0
        elif char in special_characters:
            missing_special = 0
    
    # Total missing character types
    missing_types = missing_digit + missing_lower + missing_upper + missing_special
    
    # Ensure password is at least 6 characters long
    return max(missing_types, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')
    fptr.close()