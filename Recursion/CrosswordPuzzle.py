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
