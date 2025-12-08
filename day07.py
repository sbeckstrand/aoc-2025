from functools import lru_cache

class Manifold():

    def __init__(self, data_input: str):
        self.grid = [list(line) for line in data_input.splitlines()]
        self.beam = [(self.grid[0].index("S"), 0)]

    def count_splits(self):
        splits = []
        while self.beam:
            next_cells = []
            
            for current in self.beam:
                x, y = current
                if not 0 <= x < len(self.grid[0]) or not 0 <= y < len(self.grid):
                    continue
                
                cell = self.grid[y][x]

                if cell == "^":
                    splits.append((x, y))
                    next_cells.extend([(x - 1, y), (x + 1, y)])

                if cell in [".", "S"]:
                    next_cells.append((x, y + 1))

            self.beam = list(set(next_cells))

        return len(set(splits))
    
    def count_timelines(self, start: tuple[int, int]):
        height = len(self.grid)
        width = len(self.grid[0])

        @lru_cache(None)
        def dfs(coordinates: tuple[int, int]):
            x, y = coordinates

            # reached bottom
            if y == height:
                return 1

            if not (0 <= x < width):
                return 0
            
            cell = self.grid[y][x]

            if cell == "^":
                return dfs((x - 1, y)) + dfs((x + 1, y))

            if cell in (".", "S"):
                return dfs((x, y + 1))
            
            return 0
        
        return dfs(self.beam[0]) or 1
            
def part1(data_input: str):
    manifold = Manifold(data_input)
    return manifold.count_splits()

def part2(data_input: str):
    manifold = Manifold(data_input)
    return manifold.count_timelines(manifold.beam)

def main(data_input: str):

    part1_output = part1(data_input)
    part2_output = part2(data_input)

    return (part1_output, part2_output)