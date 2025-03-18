# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store the word at the end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark end of the word
        
        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word:  # Found a word
                result.append(next_node.word)
                next_node.word = None  # Avoid duplicate results
            
            # Mark cell as visited
            board[r][c] = "#"
            
            # Explore all four directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in next_node.children:
                    dfs(nr, nc, next_node)
            
            # Restore the cell
            board[r][c] = char
            
            # Prune Trie nodes for optimization
            if not next_node.children:
                del node.children[char]
        
        # Step 2: Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        
        return result