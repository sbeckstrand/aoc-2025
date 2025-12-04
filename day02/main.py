import re

def build_ranges(data_input: str):
    ranges = [(int(start), int(end)) for start, end in [id_range.split("-") for id_range in data_input.split(",")]]
    return ranges

def part1(ranges: list[tuple[int, int]]):
    total = 0

    for id_range in ranges:
        start, end = id_range
        total += sum([product_id for product_id in range(start, end + 1) if re.match(r"^([0-9]+)\1$", str(product_id))])

    return total


def part2(ranges: list[tuple[int, int]]):
    total = 0

    for id_range in ranges:
        start, end = id_range
        total += sum([product_id for product_id in range(start, end + 1) if re.match(r"^(.+)\1+$", str(product_id))])
    
    return total

def main(data_input: str):

    ranges = build_ranges(data_input)

    part1_output = part1(ranges)
    part2_output = part2(ranges)
    return (part1_output, part2_output)