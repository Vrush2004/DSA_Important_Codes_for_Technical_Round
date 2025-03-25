# Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
# Output: true

from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Collect unique x and y coordinates
        x_coords = set()
        y_coords = set()

        for x1, y1, x2, y2 in rectangles:
            x_coords.add(x1)
            x_coords.add(x2)
            y_coords.add(y1)
            y_coords.add(y2)

        x_sorted = sorted(x_coords)
        y_sorted = sorted(y_coords)

        # Check vertical and horizontal cuts
        return self.canMakeTwoValidCuts(rectangles, x_sorted, vertical=True) or \
               self.canMakeTwoValidCuts(rectangles, y_sorted, vertical=False)

    def canMakeTwoValidCuts(self, rectangles: List[List[int]], cut_points: List[int], vertical: bool) -> bool:
        """
        Checks if two valid cuts can be made based on x or y coordinates.
        """
        for i in range(1, len(cut_points) - 1):  # First cut
            for j in range(i + 1, len(cut_points) - 1):  # Second cut
                cut1, cut2 = cut_points[i], cut_points[j]
                section = [0, 0, 0]  # Track how many rectangles exist in each section
                valid = True

                for rect in rectangles:
                    start, end = (rect[0], rect[2]) if vertical else (rect[1], rect[3])

                    # Determine which section this rectangle belongs to
                    if end <= cut1:
                        section[0] += 1
                    elif start >= cut2:
                        section[2] += 1
                    elif start >= cut1 and end <= cut2:
                        section[1] += 1
                    else:
                        valid = False  # Rectangle crosses a cut
                        break

                if valid and all(s > 0 for s in section):  # Each section must have at least 1 rectangle
                    return True

        return False
