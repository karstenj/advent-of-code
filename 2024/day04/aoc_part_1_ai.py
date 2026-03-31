import re

def parse_and_calculate(filename):
    # Read the input from the file
    with open(filename, 'r') as file:
        data = file.read()

    # Define a regex pattern to match valid mul(X,Y) instructions
    pattern = r'mul\(\d+,\d+\)'

    # Find all valid matches in the input data
    matches = re.findall(pattern, data)

    # Initialize the total sum
    total_sum = 0

    # Process each match
    for match in matches:
        # Extract the numbers inside the parentheses
        numbers = re.findall(r'\d+', match)
        if len(numbers) == 2:
            # Multiply the numbers and add to the total sum
            total_sum += int(numbers[0]) * int(numbers[1])

    return total_sum

if __name__ == "__main__":
    # Specify the input file
    input_file = "input2.txt"  # Replace with your actual file path
    result = parse_and_calculate(input_file)
    print(f"Total sum of valid multiplications: {result}")
