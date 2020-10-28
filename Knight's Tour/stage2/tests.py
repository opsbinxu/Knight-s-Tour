# from hstest.stage_test import StageTest
from hstest.stage_test import *
from hstest.test_case import TestCase, SimpleTestCase
from hstest.check_result import CheckResult
from copy import deepcopy
import random


def digits(num):
    return len(str(num))


random.seed()
# ncols = random.randint(1, 8)
# nrows = random.randint(1, 8)
ncols = 10
nrows = 10

yaxiswidth = digits(nrows)
xaxiswidth = digits(nrows * ncols)
size = str(ncols) + " " + str(nrows)
x_start = random.randint(1, ncols)
y_start = random.randint(1, nrows)
start = str(x_start) + " " + str(y_start)


class KnightsTourTest(StageTest):
    def generate(self) -> List[TestCase]:
        # return [TestCase(stdin=[self.check_request]),
        #         TestCase(stdin=["1 10", start], check_function=self.check_bounds),
        #         TestCase(stdin=["-1 5", start], check_function=self.check_bounds),
        #         TestCase(stdin=["1", start], check_function=self.check_length),
        #         TestCase(stdin=["1 1 1", start], check_function=self.check_length),
        #         TestCase(stdin=["1 a", start], check_function=self.check_num),
        #         TestCase(stdin=start),]
        return [TestCase(stdin=[self.check_request_size, self.check_request_start]), ]
        # TestCase(stdin=["1 10", start], check_function=self.check_bounds),]

    def check_request_size(self, output):
        output = output.lower()
        if "dimension" not in output:
            return CheckResult.wrong("Your program should ask for the board dimensions")
        return size

    def check_request_start(self, output):
        output = output.lower()
        if "position" not in output:
            return CheckResult.wrong("Your program should ask for the knight's starting position")
        return start

    def check_bounds(self, reply: str, attach: Any) -> CheckResult:
        if "invalid" not in reply.lower():
            return CheckResult.wrong("Your program should check if the position is within bounds")
        return CheckResult.correct()

    def check_length(self, reply: str, attach: Any) -> CheckResult:
        if "invalid" not in reply.lower():
            return CheckResult.wrong("Your program should check if there are the right number of inputs")
        return CheckResult.correct()

    def check_num(self, reply: str, attach: Any) -> CheckResult:
        if "invalid" not in reply.lower():
            return CheckResult.wrong("Your program should only accept integer inputs")
        return CheckResult.correct()

    def check(self, reply: str, attach: Any) -> CheckResult:
        # check output
        try:
            if reply == "":
                return CheckResult.wrong("Output was empty")
            border = "-" * (ncols * (xaxiswidth) + 3) + "\n"
            reply = reply.split(border)
            if len(reply) != 3:
                return CheckResult.wrong("Incorrect border or spacing")
        except:
            return CheckResult.wrong("Incorrect output")

        # extract board and xlabels
        try:
            board = reply[1].split(" |\n")[0:nrows]
            if len(board) != nrows:
                return CheckResult.wrong("Incorrect side borders or format")

            xaxis1 = deepcopy(reply[2])
            xaxis1 = xaxis1.strip().split()
            xaxis2 = deepcopy(reply[2])
            if len(xaxis1) != ncols:
                return CheckResult.wrong("Incorrect column numbers")
        except IndexError:
            return CheckResult.wrong("Incorrect border or spacing")

        # check location of xcol = 1 for alignment
        try:
            x_one_pos = yaxiswidth + 1 + 1 + xaxiswidth
            if xaxis2[x_one_pos - 1] != "1":
                return CheckResult.wrong("Incorrect column number alignment or placeholder width")
            xaxis2 = xaxis2.strip()
            # check rest of column numbers for alignment
            for n in range(1, ncols):
                xaxis2 = xaxis2.split(" "*(xaxiswidth - digits(n+1)+1), 1)
                if len(xaxis2) != 2:
                    return CheckResult.wrong("Spacing between column numbers is incorrect")
                if str(n) != xaxis2[0]:
                    return CheckResult.wrong("Incorrect column number alignment or placeholder width")
                xaxis2 = xaxis2[1]
            if str(ncols) != xaxis2:
                return CheckResult.wrong("Incorrect column number alignment or placeholder width")
        except:
            return CheckResult.wrong("There is something wrong with your column numbers")


        # iterate through rows to check
        for n, row in enumerate(board):
            rownum = nrows - n
            colnum = n + 1

            # check column numbers
            if colnum > ncols:
                pass
            elif colnum != int(xaxis1[n]):
                return CheckResult.wrong("Incorrect column numbers")

            # split at left border, check if row split correctly
            row = row.split("|")
            if len(row) != 2:
                return CheckResult.wrong("Incorrect side borders or format")

            if len(row[0]) != yaxiswidth:
                return CheckResult.wrong("Row numbers or side border not aligned")

            # check if knight in correct position
            if rownum == y_start:

                # check row number
                if rownum != int(row[0]):
                    return CheckResult.wrong("Incorrect row numbers")

                # extract each position, including placeholders and knight
                row = row[1].strip().split()

                #   check if number of columns is correct
                if len(row) != ncols:
                    return CheckResult.wrong("Incorrect board dimension")

                # check correct position
                if row[x_start - 1] not in ['x', 'X']:
                    return CheckResult.wrong("Incorrect starting position")

                # check this row if placeholders are correct
                for place in row:
                    if place not in ['x', 'X']:
                        if place != '_' * xaxiswidth:
                            return CheckResult.wrong("Incorrect placeholder width")

        return CheckResult.correct()


if __name__ == '__main__':
    KnightsTourTest('knightstour.game').run_tests()
    # print(KnightsTourTest.generate.__annotations__)
