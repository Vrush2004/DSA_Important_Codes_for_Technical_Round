import os

def simpleArraySum(ar):
    total = 0  
    for num in ar:  
        total += num  
    return total  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the size of the array
    ar_count = int(input().strip())

    # Read the array elements
    ar = list(map(int, input().rstrip().split()))

    # Call the function to compute the sum
    result = simpleArraySum(ar)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()