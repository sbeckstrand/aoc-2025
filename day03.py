def build_banks(data_input) -> list[list[int]]:
    return [[int(x) for x in bank] for bank in data_input.splitlines()]

def get_largest(bank: list[int], limit: int):
    end = (limit - 1) * -1 if limit > 1 else len(bank)
    return max(bank[:end]), bank[bank.index(max(bank[:end])) + 1:] 

def get_joltage(banks: list[list[int]], battery_count: int):
    total = 0
    
    for bank in banks:
        joltage = ""
        for battery in range(battery_count, 0, -1):
            new_joltage, bank = get_largest(bank, limit=battery)
            joltage += str(new_joltage)
        
        total += int(joltage)

    return total

def main(data_input: str):

    banks = build_banks(data_input)

    part1_output = get_joltage(banks, 2)
    part2_output = get_joltage(banks, 12)

    return (part1_output, part2_output)