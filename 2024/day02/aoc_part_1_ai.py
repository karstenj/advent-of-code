def is_safe(report):
    levels = list(map(int, report.split()))
    if len(levels) < 2:
        return False  # A single level cannot be safely increasing or decreasing.

    differences = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]

    # Check if all differences are within the range [-3, -1] (decreasing) or [1, 3] (increasing)
    if all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences):
        return True
    return False

def count_safe_reports(filename):
    with open(filename, 'r') as file:
        reports = file.readlines()

    safe_count = sum(1 for report in reports if is_safe(report.strip()))
    return safe_count

if __name__ == "__main__":
    input_file = "input2.txt"  # Replace with your input file name
    safe_reports = count_safe_reports(input_file)
    print(f"Number of safe reports: {safe_reports}")
