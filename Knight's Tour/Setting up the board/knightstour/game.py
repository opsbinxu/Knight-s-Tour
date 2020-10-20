def print_board(x, y):
    border = " -------------------"
    xlabel = "  1 2 3 4 5 6 7 8 "
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


def main():
    x, y = map(int, input("Enter knight's starting position: ").split())
    print_board(x, y)


if __name__ == "__main__":
    main()