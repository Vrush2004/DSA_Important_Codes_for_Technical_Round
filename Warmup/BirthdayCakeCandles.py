def birthdayCakeCandles(candles):
    # Step 1: Find the maximum height candle
    tallest = max(candles)
    
    # Step 2: Count how many times the tallest candle appears
    tallest_count = candles.count(tallest)
    
    # Step 3: Return the count of the tallest candles
    return tallest_count

# Main function to take input and output result
if __name__ == '__main__':
    # Reading the number of candles (not used directly)
    candles_count = int(input().strip())
    
    # Reading the heights of the candles into a list
    candles = list(map(int, input().rstrip().split()))
    
    # Getting the result by calling the function
    result = birthdayCakeCandles(candles)
    
    # Writing the result to output
    print(result)