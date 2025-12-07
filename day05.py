def build_ranges(data_input: str) -> list[tuple[int,int]]:
    ranges = []
    for line in data_input.splitlines():
        if "-" in line:
            ranges.append(tuple(map(int, line.split('-'))))
    
    return ranges


def part1(ingredients: list[int], fresh_ranges: list[tuple[int,int]]) -> int:
    fresh = []
    for ingredient in ingredients:
        for start, end in fresh_ranges:
            if start <= ingredient <= end:
                fresh.append(ingredient)
                break
    

    return len(set(fresh))

def part2(fresh_ranges: list[tuple[int,int]]) -> int:
    fresh_count = 0

    fresh_ranges.sort(key=lambda range: range[0])

    current_start, current_end = fresh_ranges[0]

    for start, end in fresh_ranges[1:]:
        if start > current_end + 1:
            fresh_count += current_end - current_start + 1
            current_start, current_end = start, end
        else:
            current_end = max(current_end, end)

    fresh_count += current_end - current_start + 1
    
    return fresh_count

def main(data_input: str):
    range_data, ingredient_data = data_input.split('\n\n')
    
    fresh_ranges = build_ranges(range_data)
    ingredients = [int(ingredient_id) for ingredient_id in ingredient_data.splitlines()]

    part1_output = part1(ingredients, fresh_ranges)
    part2_output = part2(fresh_ranges)

    return (part1_output, part2_output)