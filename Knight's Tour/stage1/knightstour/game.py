# **********************************************************************
#  Project           : Hyperskill Knight's Tour, Stage 1
#  Program name      : game.py
#  Author            : Bing Xu / opsbinxu / bingdaxu@gmail.com
#  Date created      : 2020 / 10 / 22
#  Purpose           : Display chessboard
# **********************************************************************

def print_board(x, y):
    border = " -------------------"
    xlabel = "   1 2 3 4 5 6 7 8 "
    nrows = 8
    ncols = 8

    print(border)
    for row in range(nrows):
        print(nrows - row,  "|", end=' ', sep='')
        for col in range(ncols):
            if x == (col + 1) and y == (nrows - row):
                print("X", end=' ')
            else:
                print("_", end=' ')
        print("|")
    print(border)
    print(xlabel)

def invalidMove(x, y):
    if x < 1 or y < 1 or x > 8 or y > 8:
        return True
    return False

def main():
    while True:
        try:
            x, y = map(int, input("Enter knight's starting position: ").split())
            if invalidMove(x, y):
                raise ValueError
        except ValueError:
            print('Invalid position!')
            continue
        else:
            break
    print_board(x, y)

if __name__ == "__main__":
    main()
