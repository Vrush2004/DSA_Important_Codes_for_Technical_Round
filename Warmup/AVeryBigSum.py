import os

def aVeryBigSum(ar):
    # Calculate and return the sum of the array
    return sum(ar)

if __name__ == '__main__':
    # Open the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in the array
    ar_count = int(input().strip())

    # Read the array of integers
    ar = list(map(int, input().rstrip().split()))

    # Get the result by calling the function
    result = aVeryBigSum(ar)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()