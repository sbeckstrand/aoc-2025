class Grid():

    def __init__(self, grid_data: str):
        self.grid_data = grid_data
        self.grid = []

        for line in grid_data.splitlines():
            self.grid.append(list(line))

        self.width = len(self.grid[0])
        self.height = len(self.grid)

class Forklift():

    def __init__(self, start_position: tuple[int, int], grid: Grid):
        self.position = (0,0)
        self.grid = grid
    
    def count_rolls(self, position: tuple[int, int]) -> int:
        surrounding_cells = []
        surrounding_indexes = [
            (-1, -1), (0, -1), ( 1,  -1),
            ( -1, 0),          ( 1,  0 ),
            ( -1, 1), ( 0, 1), ( 1,  1 ),
        ]
        x, y  = position

        for dx, dy in surrounding_indexes:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < self.grid.width and 0 <= ny < self.grid.height:
                surrounding_cells.append(self.grid.grid[ny][nx])

        rolls = sum(1 for cell in surrounding_cells if cell == '@')

        return rolls
    
    def remove_roll(self, position: tuple[int, int]) -> None:
        x, y = position
        if self.grid.grid[y][x] == '@':
            self.grid.grid[y][x] = '.'
    
def part1(data_input: str):
    grid = Grid(data_input)
    forklift = Forklift((0, 0), grid)

    rolls = 0
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.grid[y][x] == "@":
                if forklift.count_rolls((x, y)) < 4:
                    rolls += 1
    
    return rolls

def part2(data_input: str):
    grid = Grid(data_input)
    forklift = Forklift((0, 0), grid)

    rolls = 0
    current_cycle_rolls = -1
    while current_cycle_rolls != 0:
        current_cycle_rolls = 0
        for y in range(grid.height):
            for x in range(grid.width):
                if grid.grid[y][x] == "@":
                    if forklift.count_rolls((x, y)) < 4:
                        forklift.remove_roll((x, y))
                        current_cycle_rolls += 1
        
        rolls += current_cycle_rolls

    return rolls

def main(data_input: str):

    part1_output = part1(data_input)
    part2_output = part2(data_input)

    return (part1_output, part2_output)