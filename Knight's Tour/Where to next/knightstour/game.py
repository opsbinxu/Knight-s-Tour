# **********************************************************************
#  Project           : Hyperskill Knight's Tour, Stage 3
#  Program name      : game.py
#  Author            : Bing Xu, opsbinxu
#  Date created      : 2020 / 10 / 22
#  Purpose           : See where the knight can move
# **********************************************************************

DIRECTIONS = 8


def digits(num):
    return len(str(num))


def printBoard(x, y, ncols, nrows, board):
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
                print(col.rjust(xaxiswidth), end=' ', sep='')
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
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(DIRECTIONS):
        new_x = cur_x + move_x[i]   # user coordinates 1 - n
        new_y = cur_y + move_y[i]   # user coordinates 1 - n
        if validMove(new_x, new_y, ncols, nrows, board):
            board[new_y-1][new_x-1] = "O"


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

    checkMove(x, y, ncols, nrows, board)
    # print(*board[::-1], sep="\n")

    print("\nHere are the possible moves:")
    printBoard(x, y, ncols, nrows, board)


if __name__ == "__main__":
    main()
