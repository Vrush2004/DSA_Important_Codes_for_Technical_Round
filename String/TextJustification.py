# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        current_line = []
        current_line_length = 0

        for word in words:
            # Check if adding the current word exceeds maxWidth
            if current_line_length + len(word) + len(current_line) > maxWidth:
                # Distribute spaces for the current line
                for i in range(maxWidth - current_line_length):
                    current_line[i % (len(current_line) - 1 or 1)] += " "
                # Add the fully justified line to the result
                result.append("".join(current_line))
                # Start a new line
                current_line, current_line_length = [], 0

            # Add the current word to the line
            current_line.append(word)
            current_line_length += len(word)

        # Handle the last line (left-justified)
        result.append(" ".join(current_line).ljust(maxWidth))

        return result