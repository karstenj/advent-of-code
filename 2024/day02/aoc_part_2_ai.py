def is_safe(report):
    """
    Checks if a report is safe without removing any level.
    """
    levels = list(map(int, report.split()))
    if len(levels) < 2:
        return False  # A single level cannot be safely increasing or decreasing.

    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # Check if all differences are within the range [-3, -1] (decreasing) or [1, 3] (increasing)
    if all(-3 <= diff <= -1 for diff in differences) or all(1 <= diff <= 3 for diff in differences):
        return True
    return False


def can_be_safe_with_dampener(report):
    """
    Checks if a report can be made safe by removing a single level.
    """
    levels = list(map(int, report.split()))
    for i in range(len(levels)):
        # Create a new report with the i-th level removed
        modified_levels = levels[:i] + levels[i + 1:]
        modified_report = " ".join(map(str, modified_levels))
        if is_safe(modified_report):
            return True
    return False


def count_safe_reports_with_dampener(filename):
    with open(filename, 'r') as file:
        reports = file.readlines()

    safe_count = 0
    for report in reports:
        stripped_report = report.strip()
        if is_safe(stripped_report) or can_be_safe_with_dampener(stripped_report):
            safe_count += 1
    return safe_count


if __name__ == "__main__":
    input_file = "input2.txt"  # Replace with your input file name
    safe_reports = count_safe_reports_with_dampener(input_file)
    print(f"Number of safe reports with Problem Dampener: {safe_reports}")
