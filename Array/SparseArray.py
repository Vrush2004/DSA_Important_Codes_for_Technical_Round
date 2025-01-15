def matchingStrings(stringList, queries):
    # Create a dictionary to store the frequency of each string in stringList
    freq_dict = {}
    
    # Count the occurrences of each string in stringList
    for string in stringList:
        if string in freq_dict:
            freq_dict[string] += 1
        else:
            freq_dict[string] = 1
    
    # For each query, retrieve the frequency from the dictionary (or 0 if not found)
    result = []
    for query in queries:
        result.append(freq_dict.get(query, 0))  # Default to 0 if query not found
    
    return result

if __name__ == '__main__':
    stringList_count = int(input().strip())
    stringList = [input().strip() for _ in range(stringList_count)]

    queries_count = int(input().strip())
    queries = [input().strip() for _ in range(queries_count)]

    res = matchingStrings(stringList, queries)

    # Output the result to stdout
    print('\n'.join(map(str, res)))