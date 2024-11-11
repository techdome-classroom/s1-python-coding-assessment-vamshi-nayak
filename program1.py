from collections import deque

class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        numRows = len(grid)
        numCols = len(grid[0])
        islandCount = 0

        def bfs(startRow, startCol):
            queue = deque([(startRow, startCol)])
            grid[startRow][startCol] = 'W' 

            directions = [
                (0, 1),   
                (1, 0),   
                (0, -1),  
                (-1, 0)   
            ]

            while queue:
                currentRow, currentCol = queue.popleft()

                for dRow, dCol in directions:
                    newRow, newCol = currentRow + dRow, currentCol + dCol

                    
                    if 0 <= newRow < numRows and 0 <= newCol < numCols and grid[newRow][newCol] == 'L':
                        grid[newRow][newCol] = 'W' 
                        queue.append((newRow, newCol))

   
        for row in range(numRows):
            for col in range(numCols):
                
                if grid[row][col] == 'L':
                    islandCount += 1
                    bfs(row, col)

        return islandCount
