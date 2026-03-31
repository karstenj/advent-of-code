def parse_disk_map(disk_map):
    """Parse the disk map into blocks representing files and free space."""
    blocks = []
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1])
        blocks.extend([len(blocks) // 2] * file_length + ['.'] * free_length)
    return blocks

def compact_disk(blocks):
    """Perform the disk compaction by moving file blocks to the left."""
    write_index = 0
    for read_index in range(len(blocks)):
        if blocks[read_index] != '.':
            blocks[write_index] = blocks[read_index]
            write_index += 1
    # Fill the rest with free space
    for i in range(write_index, len(blocks)):
        blocks[i] = '.'
    return blocks

def calculate_checksum(blocks):
    """Calculate the checksum by summing the product of position and file ID."""
    checksum = 0
    for position, block in enumerate(blocks):
        if block != '.':
            checksum += position * block
    return checksum

def main():
    # Read input
    with open('input1.txt', 'r') as file:
        disk_map = file.read().strip()

    # Parse the disk map into blocks
    blocks = parse_disk_map(disk_map)

    # Compact the disk
    compacted_blocks = compact_disk(blocks)

    # Calculate the checksum
    checksum = calculate_checksum(compacted_blocks)

    print(f"Resulting Filesystem Checksum: {checksum}")

if __name__ == "__main__":
    main()
