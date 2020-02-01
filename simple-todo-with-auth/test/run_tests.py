import unittest
from test.password_utils_test import GetSha512Test


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(GetSha512Test('test_if_can_sha512'))
    suite.addTest(GetSha512Test('fail_if_not_sah512'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
