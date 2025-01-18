def staircase(n):
    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Print spaces and '#' symbols for each level
        print(' ' * (n - i) + '#' * i)

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)