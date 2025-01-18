def diagonalDifference(arr):
    n = len(arr)  # The size of the square matrix (n x n)
    
    # Initialize sums for the diagonals
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    # Traverse through each row of the matrix
    for i in range(n):
        primary_diagonal_sum += arr[i][i]  # Element in the primary diagonal
        secondary_diagonal_sum += arr[i][n - 1 - i]  # Element in the secondary diagonal
    
    # Calculate and return the absolute difference
    return abs(primary_diagonal_sum - secondary_diagonal_sum)

if __name__ == '__main__':
    # Reading input
    n = int(input().strip())  # Size of the matrix
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Calculate the result
    result = diagonalDifference(arr)
    
    # Output the result
    print(result)