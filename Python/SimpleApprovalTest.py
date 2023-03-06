import unittest

from approvaltests.approvals import verify


class Calculator:
    def add(self, a, b):
        return a + b


class GettingStartedTest(unittest.TestCase):
    def test_simple_approval(self):
        verify("Hello ApprovalTests")

    def test_refactoring(self):
        result = Calculator().add(1, 2)
        verify(result)


if __name__ == "__main__":
    unittest.main()
