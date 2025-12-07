def part1(challenge_input: str, start_point: int):
    current = start_point
    zero_count = 0
    for line in challenge_input:
        direction, value = line[:1], int(line[1:])
        current += (value * -1) if direction == 'L' else value
        
        if current % 100 == 0:
            zero_count += 1

    return zero_count

def part2(challenge_input: str, start_point: int):
    current = start_point
    zero_count = 0

    for line in challenge_input:
        direction, value = line[:1], int(line[1:])
        start = current
        current += (value * -1) if direction == 'L' else value

        if abs(current) >= 100:
            zero_count += int(abs(current / 100))
        if current <= 0 and start != 0:
            zero_count += 1

        current = current % 100
    
    return zero_count


def main():
    start_point = 50
    input_file = 'input.txt'
    with open(input_file) as f:
        challenge_input = f.read()

    part1_answer = part1(challenge_input.splitlines(), start_point)
    part2_answer = part2(challenge_input.splitlines(), start_point)
    
    return (part1_answer, part2_answer)

print(main())