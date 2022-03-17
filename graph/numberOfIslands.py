from collections import deque

class Solution:
    def numIslands(self, grid):
        # edge cases
        # Keep counters of number of island and visited set.
        # Iterate row and then cols
        # Check if the current index is land and is not visited
        # If not visited: perform bfs/dfs to visit all land and add to visited.
        # increment count
        # if visited: move to the next index
        
        count = 0
        visited = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr = grid[row][col]
                coord = (row, col)
                if coord not in visited and curr == "1":
                    count += 1
                    self.bfs(coord, grid, visited)
        
        return count
                    
        
    def bfs(self, coord, grid, visited):
        colBound = len(grid[0])
        rowBound = len(grid)
        
        queue = deque()
        queue.append(coord)
        visited.add(coord)

        while queue:
            row, col = queue.popleft()
            directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]
            for rowAdd, colAdd in directions:
                newRow = row + rowAdd
                newCol = col + colAdd
                if (newRow, newCol) not in visited and newRow in range(rowBound) and newCol in range(colBound) and grid[newRow, newCol] == 1:
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
                

s = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(s.numIslands(grid))
            
            
            
            
            
            
            
            
            