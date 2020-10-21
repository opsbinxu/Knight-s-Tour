from copy import deepcopy
DIRECTIONS = 8
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
win = False
deadend = False


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
        # xlabel.append(" " * (xaxiswidth - digits(colnum)) + str(colnum))
        # xlabel.append("{num:{fill}{width}}".format(num=colnum, fill=" ", width=xaxiswidth))
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


def validMove(x, y, ncols, nrows, board):  # user coordinates 1 - n
    if not onBoard(x, y, ncols, nrows):
        return False

    if not board[y-1][x-1] == -1:
        return False
    return True


def onBoard(x, y, ncols, nrows):  # user coordinates 1 - n
    if x > 0 and y > 0 and x <= ncols and y <= nrows:
        return True
    return False


def checkMove(cur_x, cur_y, ncols, nrows, board):
    # move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    # move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    global deadend
    deadend = True
    for i in range(DIRECTIONS):
        new_x = cur_x + move_x[i]   # user coordinates 1 - n
        new_y = cur_y + move_y[i]   # user coordinates 1 - n
        if validMove(new_x, new_y, ncols, nrows, board):
            board[new_y-1][new_x -
                           1] = warnsdorff(new_x, new_y, ncols, nrows, board)
            deadend = False


def warnsdorff(cur_x, cur_y, ncols, nrows, board):
    # move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    # move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    possible = 0
    for i in range(DIRECTIONS):
        new_x = cur_x + move_x[i]   # user coordinates 1 - n
        new_y = cur_y + move_y[i]   # user coordinates 1 - n
        if validMove(new_x, new_y, ncols, nrows, board):    # user coordinates 1 - n
            possible += 1
    return possible


def main():
    while True:
        try:
            ncols, nrows = map(int, input(
                "Enter your board's dimensions: ").split())
        except ValueError:
            print("Invalid entry!")
            continue
        else:
            board = [[-1 for i in range(ncols)] for i in range(nrows)]
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
            board[y-1][x-1] = "X"
            break

    play_game(x, y, ncols, nrows, board)
    # warns_board = deepcopy(board)
    # checkMove(x, y, ncols, nrows, warns_board)
    # printBoard(ncols, nrows, warns_board), print("")

    # moves = 1
    # spaces = ncols * nrows

    # while not win and not deadend:
    #     while True:
    #         try:
    #             x, y = map(int, input("Enter your next move: ").split())
    #             if not onBoard(x, y, ncols, nrows):
    #                 raise ValueError
    #             if not validMove(x, y, ncols, nrows, board):
    #                 raise ValueError
    #         except ValueError:
    #             print('Invalid move! ', end='')
    #             continue
    #         else:
    #             board[y-1][x-1] = "X"
    #             board[last_y-1][last_x-1] = "*"
    #             last_x, last_y = x, y
    #             warns_board = deepcopy(board)
    #             checkMove(x, y, ncols, nrows, warns_board)
    #             printBoard(ncols, nrows, warns_board), print("")
    #             moves += 1
    #             if moves == spaces:
    #                 win = True
    #                 print("Your knight toured the whole board!")
    #             if deadend:
    #                 print("No more possible moves!")
    #                 print(f"Your knight moved {moves} space",
    #                     "s" * (1 if (moves > 1) else 0), "!", sep="")
    #             break


def play_game(start_x, start_y, ncols, nrows, board):
    global win, deadend
    last_x, last_y = start_x, start_y
    warns_board = deepcopy(board)
    checkMove(start_x, start_y, ncols, nrows, warns_board)
    printBoard(ncols, nrows, warns_board), print("")

    moves = 1
    spaces = ncols * nrows

    while not win and not deadend:
        while True:
            try:
                x, y = map(int, input("Enter your next move: ").split())
                if not onBoard(x, y, ncols, nrows):
                    raise ValueError
                if not validMove(x, y, ncols, nrows, board):
                    raise ValueError
            except ValueError:
                print('Invalid move! ', end='')
                continue
            else:
                board[y-1][x-1] = "X"
                board[last_y-1][last_x-1] = "*"
                last_x, last_y = x, y
                warns_board = deepcopy(board)
                checkMove(x, y, ncols, nrows, warns_board)
                printBoard(ncols, nrows, warns_board), print("")
                moves += 1
                if moves == spaces:
                    win = True
                    print("Your knight toured the whole board!")
                elif deadend:
                    print("No more possible moves!")
                    print(f"Your knight moved {moves} space",
                        "s" * (1 if (moves > 1) else 0), "!", sep="")
                break

if __name__ == "__main__":
    main()
