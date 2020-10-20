# from hstest.stage_test import StageTest
from hstest.stage_test import *
from hstest.test_case import TestCase
# from hstest.check_result import CheckResult

class KnightsTourTest(StageTest):  # this is a child class
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin="TestName")]

    def check(self, reply: str, attach) -> CheckResult:
        if len(reply.strip().split('\n')) == 2:
            return CheckResult.correct()
        return CheckResult.wrong("You should output exactly two lines")


if __name__ == '__main__':
    KnightsTourTest('knightstour.game').run_tests()
    # print(KnightsTourTest.generate.__annotations__)
