import re

class Problem():
    def __init__(self, numbers: list[str], operation: str):
        self.numbers = [number.replace("0", " ") for number in numbers]

        match operation:
            case '+':
                self.operation = 'add'
            case '*':
                self.operation = 'mult'
    
    def solve(self, num_format: str = 'standard'):
        solve_numbers = []
        match num_format:
            case 'standard':
                solve_numbers = [int(number.strip()) for number in self.numbers]
            case 'cephalopod':
                for idx in range(len(self.numbers[0])):
                    ceph_number = ""
                    for number in self.numbers:
                        ceph_number += number[idx]
                    solve_numbers.append(int(ceph_number.strip()))
                                    
        match self.operation:
            case 'add':
                return sum(solve_numbers)
            case 'mult':
                result = 1
                for number in solve_numbers:
                    result *= number
                return result


def build_problem_sheet(data_input: str):
    problems = []
    problem_numbers = []
    operations = [operation for operation in data_input.splitlines()[-1].split()]
    
    # Build dataframe and replace all spaces with zeroes. 
    # In columns where there are only zeroes, replace with space.
    data = [list(line.replace(" ", "0")) for line in data_input.splitlines()[:-1]]
    num_cols = len(data[0])
    zero_cols = [
        all(row[c] == "0" for row in data)
        for c in range(num_cols)
    ]

    for row_idx in range(len(data)):
        for col_idx in range(num_cols):
            if zero_cols[col_idx]:
                data[row_idx][col_idx] = " "

    # Build array of number strings now including zeroes
    for idx in range(len(data)):
        number_string = "".join(data[idx])
        numbers = number_string.split(" ")
        
        if not problem_numbers:
            problem_numbers = [[number] for number in numbers]
            continue

        for num_idx in range(len(numbers)):
            problem_numbers[num_idx].append(numbers[num_idx])
            
    # Build problem objects 
    for idx in range(len(problem_numbers)):
        problems.append(Problem(problem_numbers[idx], operations[idx]))
    
    return problems


def part1(problems: list[Problem]):
    total = 0
    for problem in problems:
        total += problem.solve()
    
    return total

def part2(problems: list[Problem]):
    total = 0
    for problem in problems:
        total += problem.solve(num_format='cephalopod')
    
    return total

def main(data_input: str):

    problems = build_problem_sheet(data_input)
    part1_output = part1(problems)
    part2_output = part2(problems)

    return (part1_output, part2_output)