class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words and remove extra spaces
        words = s.split()
        
        # Reverse the list of words
        words.reverse()
        
        # Join the words with a single space and return the result
        return ' '.join(words)


class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Initialize variables
        words = []
        word = ''
        
        # Step 2: Iterate through the string and collect words
        for char in s:
            if char != ' ':
                word += char  # Add character to current word
            else:
                if word:  # If word is not empty, add it to the list
                    words.append(word)
                    word = ''  # Reset the word
        
        # Add the last word if any
        if word:
            words.append(word)
        
        # Step 3: Reverse the list of words manually
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        
        # Step 4: Construct the final string
        result = ''
        for word in words:
            result += word + ' '
        
        # Step 5: Remove the trailing space and return the result
        return result.strip()