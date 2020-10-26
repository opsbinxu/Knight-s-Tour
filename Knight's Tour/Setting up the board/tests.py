# from hstest.stage_test import StageTest
from hstest.stage_test import *
from hstest.test_case import TestCase, SimpleTestCase
# from hstest.check_result import CheckResult
import random

x_start = random.randint(1, 8)
y_start = random.randint(1, 8)
random.seed()
x_start2 = str(random.randint(1, 8))
y_start2 = str(random.randint(1, 8))
start = str(x_start) + " " + str(y_start)
start2 = str(x_start2) + " " + str(y_start2)
ncols = 8
nrows = 8

class KnightsTourTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin=[self.check_request]),
                # TestCase(stdin=["1 10", start], check_function=self.check_bounds),
                # TestCase(stdin=["-1 5", start], check_function=self.check_bounds),
                # TestCase(stdin=["1", start], check_function=self.check_length),
                # TestCase(stdin=["1 1 1", start], check_function=self.check_length),
                # TestCase(stdin=["1 a", start], check_function=self.check_num),
                TestCase(stdin=start)]

    def check_request(self, output):
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
        reply = reply.split("-------------------\n")

        # check starting position and axis labels
        try:
            board = reply[1].split("\n")[0:nrows]
            xaxis = reply[2].strip().split(" ")
        except IndexError:
            return CheckResult.wrong("Incorrect top or bottom border")

        for n, row in enumerate(board):
            rownum = nrows - n
            colnum = n + 1
            if colnum != int(xaxis[n]):
                return CheckResult.wrong("Incorrect column numbers")
            if rownum == y_start:
                row = row.split("|")
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
