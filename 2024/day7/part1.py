from itertools import product

with open("2024/inputs/day7.in") as file:
    f = file.read().split("\n")

ans = 0

def calculate_left_to_right(expression):
    tokens = expression.split()
    result = int(tokens[0])  
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        number = int(tokens[i + 1])
        if operator == '+':
            result += number
        elif operator == '*':
            result *= number
        i += 2
    return result

def evaluate_equation(equation, result):
    nums = list(map(int,equation.split(" ")))
    operators = ['+', '*']
    operator_combinations = list(product(operators, repeat=len(nums) - 1))
    
    expressions = []
    results = []
    for ops in operator_combinations:
        expression = str(nums[0])
        for num, op in zip(nums[1:], ops):
            expression += f" {op} {num}"
        
        expressions.append(expression)
        results.append(calculate_left_to_right(expression))
    
    for r in results:
        if r == int(result):
            return True    

for line in f:
    result, equation = line.split(": ")
    if evaluate_equation(equation,result):
        ans += int(result)
print(ans)
    
    

