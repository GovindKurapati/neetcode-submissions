class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1:
                        continue

                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
