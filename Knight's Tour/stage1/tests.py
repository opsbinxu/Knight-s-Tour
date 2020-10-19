from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class KnightsTourTest(StageTest):
    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        return CheckResult.correct()


if __name__ == '__main__':
    KnightsTourTest('knightstour.game').run_tests()
