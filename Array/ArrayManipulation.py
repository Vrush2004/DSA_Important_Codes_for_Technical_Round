def arrayManipulation(n, queries):
    # Initialize an array of size n+1 (to avoid index out of range for b+1)
    arr = [0] * (n + 1)

    # Process each query
    for query in queries:
        a, b, k = query
        arr[a - 1] += k  # Add k at index a-1 (0-based index)
        if b < n:
            arr[b] -= k  # Subtract k at index b (next index after b)

    # Now, find the maximum value by calculating the prefix sum
    max_value = 0
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        max_value = max(max_value, current_sum)

    return max_value

if __name__ == '__main__':
    # Reading input
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])  # size of array
    m = int(first_multiple_input[1])  # number of queries

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    # Print the result (max value in the array after all operations)
    print(result)