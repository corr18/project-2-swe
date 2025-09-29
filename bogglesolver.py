class Boggle:
    def __init__(self, grid, dictionary):
        # normalize grid and dictionary to uppercase
        self.grid = [[cell.upper() for cell in row] for row in grid]
        self.dictionary = set(word.upper() for word in dictionary)
        self.solutions = set()
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if grid else 0

        # build prefix set
        self.prefixes = set()
        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])

    def getSolution(self):
        self.solutions.clear()
        for r in range(self.rows):
            for c in range(self.cols):
                self._dfs(r, c, "", set())
        return sorted(self.solutions)

    def _dfs(self, r, c, path, visited):
        if (r, c) in visited:
            return

        path += self.grid[r][c]
        visited.add((r, c))

        # only accept dictionary words of length >= 3
        if path in self.dictionary and len(path) >= 3:
            self.solutions.add(path)

        if path not in self.prefixes:
            visited.remove((r, c))
            return

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    self._dfs(nr, nc, path, visited)

        visited.remove((r, c))

