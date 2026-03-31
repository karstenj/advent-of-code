import re

def parse_and_calculate_with_conditions(filename):
    # Read the input from the file
    with open(filename, 'r') as file:
        data = file.read()

    # Define a regex pattern to match valid instructions
    mul_pattern = r'mul\(\d+,\d+\)'
    condition_pattern = r'do\(\)|don\'t\(\)'

    # Combine both patterns into one to identify all relevant parts
    combined_pattern = fr'{mul_pattern}|{condition_pattern}'

    # Find all relevant instructions in the order they appear
    instructions = re.findall(combined_pattern, data)

    # Initialize state
    mul_enabled = True  # Multiplications are enabled at the beginning
    total_sum = 0

    # Process each instruction
    for instruction in instructions:
        if instruction == "do()":
            mul_enabled = True  # Enable future multiplications
        elif instruction == "don't()":
            mul_enabled = False  # Disable future multiplications
        else:  # It's a mul(X,Y) instruction
            if mul_enabled:
                # Extract the numbers and calculate the multiplication
                numbers = re.findall(r'\d+', instruction)
                if len(numbers) == 2:
                    total_sum += int(numbers[0]) * int(numbers[1])

    return total_sum

if __name__ == "__main__":
    # Specify the input file
    input_file = "input2.txt"  # Replace with your actual file path
    result = parse_and_calculate_with_conditions(input_file)
    print(f"Total sum of enabled multiplications: {result}")
