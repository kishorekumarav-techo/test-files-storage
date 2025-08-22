def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(row, col):
        # boundary check + water/visited check
        if (row < 0 or row >= rows or
            col < 0 or col >= cols or
            grid[row][col] == "0" or
            (row, col) in visited):
            return

        visited.add((row, col))
        # explore 4 directions
        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)

    islands = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col) not in visited:
                dfs(row, col)
                islands += 1

    return islands


# Example usage
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print("Number of Islands:", numIslands(grid))
