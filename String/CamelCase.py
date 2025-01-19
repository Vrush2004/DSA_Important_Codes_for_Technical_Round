import os

def camelcase(s):
    # Start with 1 word (first word is always lowercase)
    count = 1
    
    # Count uppercase letters, as each indicates a new word
    for char in s:
        if char.isupper():
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()