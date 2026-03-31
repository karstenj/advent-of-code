def count_word_occurrences(word_search, target_word):
    # Ensure the word search is clean and rows are uniform in length
    grid = [list(row.strip()) for row in word_search if row.strip()]
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(target_word)
    count = 0

    # Directions to search (row_offset, col_offset)
    directions = [
        (0, 1),  # Horizontal right
        (1, 0),  # Vertical down
        (1, 1),  # Diagonal down-right
        (1, -1), # Diagonal down-left
        (0, -1), # Horizontal left (reversed)
        (-1, 0), # Vertical up (reversed)
        (-1, -1),# Diagonal up-left (reversed)
        (-1, 1)  # Diagonal up-right (reversed)
    ]

    # Function to check for the word in a specific direction
    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + dr * i, c + dc * i
            # Ensure the indices are within bounds
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != target_word[i]:
                return False
        return True

    # Loop through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count


# Read the input from the file
with open("input2.txt", "r") as file:
    word_search_input = file.readlines()

# Target word
target = "XMAS"

# Count occurrences
result = count_word_occurrences(word_search_input, target)

# Output the result
print(f"The word '{target}' appears {result} times in the word search.")
