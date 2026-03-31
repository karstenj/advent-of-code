def count_xmas_patterns(word_search):
    # Clean and process the grid
    grid = [list(row.strip()) for row in word_search if row.strip()]
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Check if the X-MAS pattern exists at the given center (r, c)
    def is_xmas(r, c):
        # Ensure the X-pattern center is not on the edges
        if r < 1 or r >= rows - 1 or c < 1 or c >= cols - 1:
            return False

        # Top-left to bottom-right diagonal
        top_left = (r - 1, c - 1)
        bottom_right = (r + 1, c + 1)
        if not (grid[top_left[0]][top_left[1]] == 'M' and
                grid[r][c] == 'A' and
                grid[bottom_right[0]][bottom_right[1]] == 'S'):
            return False

        # Top-right to bottom-left diagonal
        top_right = (r - 1, c + 1)
        bottom_left = (r + 1, c - 1)
        if not (grid[top_right[0]][top_right[1]] == 'M' and
                grid[r][c] == 'A' and
                grid[bottom_left[0]][bottom_left[1]] == 'S'):
            return False

        return True

    # Iterate through all possible centers
    for r in range(rows):
        for c in range(cols):
            if is_xmas(r, c):
                count += 1

    return count


# Read the input from the file
with open("input1.txt", "r") as file:
    word_search_input = file.readlines()

# Count X-MAS patterns
result = count_xmas_patterns(word_search_input)

# Output the result
print(f"The number of X-MAS patterns is: {result}")
