import os  # Importing os module

def rotateLeft(d, arr):
    # If d is greater than the array length, take modulo
    d = d % len(arr)
    
    # Rotate the array using slicing
    return arr[d:] + arr[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # This line requires the os module

    # Read the input values
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    # Get the result by rotating the array
    result = rotateLeft(d, arr)

    # Write the result to the output file
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()