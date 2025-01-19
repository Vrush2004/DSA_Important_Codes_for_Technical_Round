#!/bin/python3

import os

# Check if a word can be placed horizontally
def can_place_horizontally(grid, word, row, col):
    if col + len(word) > 10:
        return False
    for i in range(len(word)):
        if grid[row][col + i] not in ('-', word[i]):
            return False
    return True

# Place a word horizontally
def place_horizontally(grid, word, row, col):
    original = []
    for i in range(len(word)):
        original.append(grid[row][col + i])
        grid[row][col + i] = word[i]
    return original

# Undo horizontal placement
def undo_horizontally(grid, original, row, col):
    for i in range(len(original)):
        grid[row][col + i] = original[i]

# Check if a word can be placed vertically
def can_place_vertically(grid, word, row, col):
    if row + len(word) > 10:
        return False
    for i in range(len(word)):
        if grid[row + i][col] not in ('-', word[i]):
            return False
    return True

# Place a word vertically
def place_vertically(grid, word, row, col):
    original = []
    for i in range(len(word)):
        original.append(grid[row + i][col])
        grid[row + i][col] = word[i]
    return original

# Undo vertical placement
def undo_vertically(grid, original, row, col):
    for i in range(len(original)):
        grid[row + i][col] = original[i]

# Backtracking function
def solve_crossword(grid, words):
    if not words:
        return True
    word = words[0]
    for row in range(10):
        for col in range(10):
            if can_place_horizontally(grid, word, row, col):
                original = place_horizontally(grid, word, row, col)
                if solve_crossword(grid, words[1:]):
                    return True
                undo_horizontally(grid, original, row, col)
            if can_place_vertically(grid, word, row, col):
                original = place_vertically(grid, word, row, col)
                if solve_crossword(grid, words[1:]):
                    return True
                undo_vertically(grid, original, row, col)
    return False

def crosswordPuzzle(crossword, words):
    grid = [list(row) for row in crossword]
    word_list = words.split(';')
    solve_crossword(grid, word_list)
    return [''.join(row) for row in grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()