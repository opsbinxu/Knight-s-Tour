def digits(num):
    return len(str(num))


def print_board(x, y, ncols, nrows):

    # border = " " * yaxiswidth + "---"

    yaxiswidth = digits(nrows)
    # xaxiswidth = digits(nrows * ncols)
    xaxiswidth = 1

    xlabel = [" " * (yaxiswidth + 1)]
    for col in range(ncols):
        colnum = col + 1
        xlabel.append(" " * (xaxiswidth - digits(colnum)) + str(colnum))

    border = " " * yaxiswidth + "-" + "-" * (xaxiswidth + 1) * ncols + "--"
    print(border)
    for row in range(nrows):
        rownum = nrows - row
        print(" " * (yaxiswidth - digits(rownum)),
              rownum,  "|", end=' ', sep='')
        for col in range(ncols):
            colnum = col + 1
            if x == colnum and y == rownum:
                print(" " * (xaxiswidth - 1), "X", end=' ', sep='')
            else:
                print("_" * xaxiswidth, end=' ')
        print("|")
    print(border)

    print(*xlabel)


def main():
    while True:
        try:
            ncols, nrows = map(int, input(
                "Enter your board's dimensions: ").split())
        except ValueError:
            print("Invalid entry!")
            continue
        else:
            break
    while True:
        try:
            x, y = map(int, input("Enter knight's starting position: ").split())
            if x > ncols or y > nrows:
                raise ValueError('Invalid position!')
        except ValueError:
            print("Invalid position!")
            continue
        else:
            break
    print_board(x, y, ncols, nrows)


if __name__ == "__main__":
    main()
