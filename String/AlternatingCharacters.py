import os

def alternatingCharacters(s):
    deletions = 0
    # Iterate through the string
    for i in range(1, len(s)):
        # If the current character matches the previous one, increment deletions
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())  # Number of test cases

    for q_itr in range(q):
        s = input()  # Input string for each test case

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
