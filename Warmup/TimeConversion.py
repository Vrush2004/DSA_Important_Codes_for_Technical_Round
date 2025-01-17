def timeConversion(s):
    # Extract the period (AM/PM)
    period = s[-2:]
    # Extract the hour, minute, and second
    hour = int(s[:2])
    minute_second = s[2:-2]
    
    # Convert the hour based on AM/PM
    if period == "AM":
        if hour == 12:
            hour = 0  # 12 AM is 00 in 24-hour time
    else:  # PM case
        if hour != 12:
            hour += 12  # For PM times other than 12, add 12 to convert to 24-hour time
    
    # Format hour to always have 2 digits
    return f"{hour:02}{minute_second}"

if __name__ == '__main__':
    # Input time in 12-hour format
    s = input().strip()

    # Call the function to convert to military time
    result = timeConversion(s)

    # Output the result
    print(result)