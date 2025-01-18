def miniMaxSum(arr):
    # Sort the array
    arr.sort()
    
    # Calculate the minimum sum (sum of the first 4 elements)
    min_sum = sum(arr[:4])
    
    # Calculate the maximum sum (sum of the last 4 elements)
    max_sum = sum(arr[1:])
    
    # Print the result
    print(min_sum, max_sum)

if __name__ == '__main__':
    # Read the input array of integers
    arr = list(map(int, input().rstrip().split()))
    
    # Call the function with the input array
    miniMaxSum(arr)