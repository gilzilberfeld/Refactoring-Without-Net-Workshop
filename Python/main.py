import unittest

from approvaltests.approvals import verify


class GettingStartedTest(unittest.TestCase):
    def test_simple(self):
        verify("Hello ApprovalTests")

    def test_first(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()