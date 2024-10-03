# input: [[1,1,1],[1,1,0],[1,0,1]]
# result: [[2,2,2],[2,2,0],[2,0,1]]

from typing import List

class Solution:
    starting_color = None
    checked_cells = set()

    def on_the_map(self, image, x, y):
        return x >= 0 and x < len(image) and y >= 0 and y < len(image[0])

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Initialize starting color
        if self.starting_color is None:
            self.starting_color = image[sr][sc]
        
        # Base case to stop recursion: check if the cell has already been filled or is the wrong color
        if image[sr][sc] != self.starting_color or (sr, sc) in self.checked_cells:
            return image
        
        # Mark the current cell as checked and update its color
        self.checked_cells.add((sr, sc))
        image[sr][sc] = color

        # Explore neighbors (up, down, left, right)
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_sr, new_sc = sr + x, sc + y
            if self.on_the_map(image, new_sr, new_sc):
                self.floodFill(image, new_sr, new_sc, color)

        return image
