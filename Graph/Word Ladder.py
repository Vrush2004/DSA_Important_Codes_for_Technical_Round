# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # Convert wordList to a set for O(1) lookups
        if endWord not in wordSet:
            return 0  # If endWord is not in wordList, no valid transformation exists
        
        queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)
        
        while queue:
            word, steps = queue.popleft()
            
            # Try mutating each character in the word
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]
                    
                    if newWord == endWord:
                        return steps + 1  # Found the shortest transformation path
                    
                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)  # Remove to prevent cycles
        
        return 0  # No valid transformation sequence found
