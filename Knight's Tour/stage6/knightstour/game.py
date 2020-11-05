# **********************************************************************
#  Project           : Hyperskill Knight's Tour, Stage 6
#  Program name      : game.py
#  Author            : Bing Xu / opsbinxu / bingdaxu@gmail.com
#  Date created      : 2020 / 10 / 22
#  Purpose           : Solve knight's tour using backtracking
# **********************************************************************

from copy import deepcopy
DIRECTIONS = 8
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
win = False
deadend = False
mode = ""


def digits(num):
    return len(str(num))


def printBoard(ncols, nrows, board):
    board = board[::-1]

    # determine x and y axis number width
    yaxiswidth = digits(nrows)
    xaxiswidth = digits(nrows * ncols)
    # xaxiswidth = 1

    # generate x axis labels
    xlabel = [" " * (yaxiswidth + 1)]
    for col in range(ncols):
        colnum = col + 1
        xlabel.append(str(colnum).rjust(xaxiswidth))

    # generate top and bottom border
    border = " " * yaxiswidth + "-" + "-" * (xaxiswidth + 1) * ncols + "--"

    # print out board
    print(border)

    for y, row in enumerate(board):
        rownum = nrows - y
        print(str(rownum).rjust(yaxiswidth), "|", end=' ', sep='')
        for x, col in enumerate(row):
            if col == -1:
                print("_" * xaxiswidth, end=' ')
            else:
                print(str(col).rjust(xaxiswidth), end=' ', sep='')
        print("|")
    print(border)

    # print out x labels
    print(*xlabel)
    return


def validMove(x, y, past_x, past_y, ncols, nrows, board):  # user coordinates 1 - n
    if not freeSpot(x, y, ncols, nrows, board):
        return False
    if not knightsMove(x, y, past_x, past_y):
        return False
    return True


def freeSpot(x, y, ncols, nrows, board):
    if not onBoard(x, y, ncols, nrows):
        return False

    if not board[y-1][x-1] == -1:
        return False
    return True


def knightsMove(x, y, last_x, last_y):
    if (abs(x-last_x) == 1 and abs(y-last_y) == 2) or (abs(x-last_x) == 2 and abs(y-last_y) == 1):
        return True
    return False


def onBoard(x, y, ncols, nrows):  # user coordinates 1 - n
    if x > 0 and y > 0 and x <= ncols and y <= nrows:
        return True
    return False


def warnsdorff(cur_x, cur_y, ncols, nrows, board):
    possible = 0
    for i in range(DIRECTIONS):
        new_x = cur_x + move_x[i]   # user coordinates 1 - n
        new_y = cur_y + move_y[i]   # user coordinates 1 - n
        if freeSpot(new_x, new_y, ncols, nrows, board):    # user coordinates 1 - n
            possible += 1
    return possible


def checkMove(cur_x, cur_y, ncols, nrows, board):
    global deadend
    deadend = True

    for i in range(DIRECTIONS):
        new_x = cur_x + move_x[i]   # user coordinates 1 - n
        new_y = cur_y + move_y[i]   # user coordinates 1 - n
        if freeSpot(new_x, new_y, ncols, nrows, board):
            possible = warnsdorff(new_x, new_y, ncols, nrows, board)
            board[new_y-1][new_x - 1] = possible
            deadend = False
    return board


def rank_moves(cur_x, cur_y, ncols, nrows, board):
    move_rank = []
    for i in range(DIRECTIONS):
        new_x = cur_x + move_x[i]   # user coordinates 1 - n
        new_y = cur_y + move_y[i]   # user coordinates 1 - n
        if freeSpot(new_x, new_y, ncols, nrows, board):
            possible = warnsdorff(new_x, new_y, ncols, nrows, board)
            move_rank.append(possible)
        else:
            move_rank.append(8)
    return move_rank


def setup():
    while True:
        try:
            ncols, nrows = map(int, input(
                "Enter your board's dimensions: ").split())
            if ncols < 1 or nrows < 1:
                raise ValueError
        except ValueError:
            print("Invalid entry!")
            continue
        else:
            break
    while True:
        try:
            x, y = map(int, input("Enter knight's starting position: ").split())
            if not onBoard(x, y, ncols, nrows):
                raise ValueError
        except ValueError:
            print('Invalid position!')
            continue
        else:
            break
    return x, y, ncols, nrows


def play_game(start_x, start_y, ncols, nrows):
    global win, deadend

    # check board is possible
    solnboard = [[-1 for i in range(ncols)] for i in range(nrows)]
    moves = 1
    solnboard[start_y-1][start_x-1] = moves
    soln_exist = find_tour(start_x, start_y, ncols, nrows, solnboard, moves+1)
    if not soln_exist:
        print("No solution exists!")
        return

    # set up board for play
    playboard = [[-1 for i in range(ncols)] for i in range(nrows)]
    playboard[start_y-1][start_x-1] = "X"
    last_x, last_y = start_x, start_y
    spaces = ncols * nrows

    # generate first hint and print board
    warns_board = deepcopy(playboard)       # duplicate board to show hint
    warns_board = checkMove(start_x, start_y, ncols, nrows, warns_board)
    printBoard(ncols, nrows, warns_board), print("")

    while not win and not deadend:
        while True:
            try:
                x, y = map(int, input("Enter your next move: ").split())
                if not onBoard(x, y, ncols, nrows):
                    raise ValueError
                if not validMove(x, y, last_x, last_y, ncols, nrows, playboard):
                    raise ValueError
            except ValueError:
                print('Invalid move! ', end='')
                continue
            else:
                playboard[y-1][x-1] = "X"
                playboard[last_y-1][last_x-1] = "*"
                last_x, last_y = x, y
                warns_board = deepcopy(playboard)
                warns_board = checkMove(x, y, ncols, nrows, warns_board)
                printBoard(ncols, nrows, warns_board), print("")
                moves += 1
                break
    if moves == spaces:
        win = True
        print("Your knight toured the whole board!")
    elif deadend:
        print("No more possible moves!")
        print(f"Your knight visted {moves} space",
              "s" * (1 if (moves > 1) else 0), "!", sep="")
    return


def show_answer(x, y, ncols, nrows):
    solnboard = [[-1 for i in range(ncols)] for i in range(nrows)]
    moves = 1
    solnboard[y-1][x-1] = moves
    soln_exist = find_tour(x, y, ncols, nrows, solnboard, moves+1)
    if soln_exist:
        print("Here's a solution!")
        printBoard(ncols, nrows, solnboard)
    else:
        print("No solution exists!")
    return


def find_tour(cur_x, cur_y, ncols, nrows, board, moves):
    spaces = ncols * nrows

    move_rank = rank_moves(cur_x, cur_y, ncols, nrows, board)
    sorted_moves = sorted(zip(move_rank, move_x, move_y))

    if moves > spaces:
        return True

    for i in range(DIRECTIONS):
        new_x = cur_x + sorted_moves[i][1]   # user coordinates 1 - n
        new_y = cur_y + sorted_moves[i][2]  # user coordinates 1 - n
        if freeSpot(new_x, new_y, ncols, nrows, board):
            board[new_y-1][new_x - 1] = moves   # try this next move
            if find_tour(new_x, new_y, ncols, nrows, board, moves + 1):
                return True
            # unsuccessful move, backtrack one move and try next one
            board[new_y-1][new_x-1] = -1
    return False


def main():
    global mode
    x, y, ncols, nrows = setup()
    while True:
        try:
            mode = input("Do you want to try the puzzle? (y/n): ")
            if mode not in ['y', 'n']:
                raise NameError
        except NameError:
            print("Invalid entry!")
            continue
        else:
            break
    if mode == "y":
        play_game(x, y, ncols, nrows)
    else:
        show_answer(x, y, ncols, nrows)
    return


if __name__ == "__main__":
    main()
