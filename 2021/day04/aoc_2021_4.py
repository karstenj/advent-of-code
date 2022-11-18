def get_numbers(input_file_name):
    fh = open(input_file_name)
    lines = fh.readlines()
    fh.close()
    numbers = [int(s) for s in lines[0].strip().split(',')]
    boards = []
    for i in range(2, len(lines), 6):
        board = []
        for j in range(i, i+5):
            board.append([int(s) for s in lines[j].strip().split()])
        boards.append(board)
    return numbers, boards


def mark_number(number, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == number:
                board[i][j] = -1


def check_win(board):
    for i in range(len(board)):
        if sum(board[i]) == -5:
            return True
    for j in range(len(board[i])):
        score = 0
        for i in range(len(board)):
            score += board[i][j]
        if score == -5:
            return True
    return False


def calculate_win(board):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != -1:
                score += board[i][j]
    return score


def process_numbers(numbers, boards):
    first_win = None
    win_board = [False] * len(boards)
    for n in numbers:
        #print(f'N: {n}')
        for i, b in enumerate(boards):
            mark_number(n, b)
            if check_win(b) and not win_board[i]:
                #print(n)
                win_board[i] = True
                if first_win is None:
                    first_win = calculate_win(b) * n
                last_win = calculate_win(b) * n
    return first_win, last_win


def get_number_part1(input_file_name):
    numbers, boards = get_numbers(input_file_name)
    first_win, last_win = process_numbers(numbers, boards)
    return first_win


def get_number_part2(input_file_name):
    numbers, boards = get_numbers(input_file_name)
    first_win, last_win = process_numbers(numbers, boards)
    return last_win
