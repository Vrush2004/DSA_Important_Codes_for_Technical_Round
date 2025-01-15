import os

def hourglassSum(arr):
    # Initialize max_sum to a very low value to ensure we update it with the real sums
    max_sum = -float('inf')
    
    # Iterate through each possible top-left corner of the hourglass
    for i in range(1, 5):  # Loop through rows 1 to 4
        for j in range(1, 5):  # Loop through columns 1 to 4
            # Calculate the sum of the current hourglass
            top = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]  # Top row of the hourglass
            mid = arr[i][j]  # Middle value of the hourglass
            bottom = arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]  # Bottom row of the hourglass
            hourglass_sum = top + mid + bottom
            
            # Update max_sum if the current hourglass sum is larger
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum
    
    # Return the maximum hourglass sum found
    return max_sum

if __name__ == '__main__':
    # Open the output file
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    # Read the 6x6 array from input
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # Call the function to get the maximum hourglass sum
    result = hourglassSum(arr)

    # Write the result to the file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()