with open('data.txt') as f:
    win_nums = [int(num) for num in (f.readline().strip()).split(',')]
    num_data = f.read().strip().split()

game_boards = []
board = {}
board_num = 1
for i in range(len(num_data)):
    board[int(num_data[i])] = False
    if len(board) == 25:
        game_boards.append(board)
        board = {}
        board_num += 1
# print(game_boards)


def check_win(board: dict):
    key_arr = list(board.keys())
    row_counter = 0
    column_counter = 0
    for i in range(5):
        # Checking rows
        if (board[key_arr[row_counter]] and board[key_arr[row_counter+1]] and 
            board[key_arr[row_counter+2]] and board[key_arr[row_counter+3]] and 
            board[key_arr[row_counter+4]]):
            return True
        if (board[key_arr[column_counter]] and board[key_arr[column_counter+5]] and 
            board[key_arr[column_counter+10]] and board[key_arr[column_counter+15]] and 
            board[key_arr[column_counter+20]]):
            return True
        row_counter += 5
        column_counter += 1
    return False

def calculate_score(board: dict, win_num: int):
    sum = 0
    for key, value in board.items():
        if not value:
            sum += key
    return sum * win_num


game_finished = False
for i in range(len(win_nums)):
    for board in game_boards:
        if win_nums[i] in board.keys():
            board[win_nums[i]] = True
            if check_win(board):
                game_finished = True
                print(calculate_score(board, win_nums[i]))
                break
    if game_finished:
        break
