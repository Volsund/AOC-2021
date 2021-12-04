with open('example_data.txt') as f:
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
        board_num +=1
# print(game_boards)

for i in range(len(win_nums)):
    for board in game_boards:
        if win_nums[i] in board.keys():
            board[win_nums[i]] = True
    print(board)
        # print(win_nums[i], '--', board.get(win_nums[i]))