import unittest

from approvaltests.approvals import verify


class GettingStartedTest(unittest.TestCase):
    def test_simple_approval(self):
        verify("Hello ApprovalTests")

if __name__ == "__main__":
    unittest.main()