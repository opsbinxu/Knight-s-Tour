# from hstest.stage_test import StageTest
from hstest.stage_test import *
from hstest.test_case import TestCase, SimpleTestCase
from hstest.check_result import CheckResult
import random

random.seed()
ncols = random.randint(1, 8)
nrows = random.randint(1, 8)
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
        return [TestCase(stdin=[self.check_request_size, self.check_request_start]),
                TestCase(stdin=["1 10", start], check_function=self.check_bounds),]

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
            border = "-"*(2 * ncols+3)+"\n"
            if reply == "":
                return CheckResult.wrong("Output was empty")
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
            xaxis = reply[2].strip().split(" ")
        except IndexError:
            return CheckResult.wrong("Incorrect border or spacing")

        # iterate through rows to check
        for n, row in enumerate(board):
            rownum = nrows - n
            colnum = n + 1

            if colnum > ncols:
                pass
            elif colnum != int(xaxis[n]):
                return CheckResult.wrong("Incorrect column numbers")

            if rownum == y_start:
                row = row.split("|")
                if len(row) != 2:
                    return CheckResult.wrong("Incorrect side borders or format")
                if rownum != int(row[0]):
                    return CheckResult.wrong("Incorrect row numbers")
                row = row[1].strip().split(" ")
                if len(row) != ncols:
                    return CheckResult.wrong("Incorrect board dimension")
                if row[x_start - 1] == "_":
                    return CheckResult.wrong("Incorrect starting position")

        return CheckResult.correct()


if __name__ == '__main__':
    KnightsTourTest('knightstour.game').run_tests()
    # print(KnightsTourTest.generate.__annotations__)
