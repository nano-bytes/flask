import unittest
import hashlib
from app.utils.password_utils import get_hashed_password_with_sha512


class GetSha512Test(unittest.TestCase):

    def test_work_if_is_sha512(self):
        expected = hashlib.sha512("Hello".encode('utf-8')).hexdigest()
        actual = get_hashed_password_with_sha512("Hello")
        self.assertEqual(expected, actual)

    def test_fail_if_not_sah512(self):
        expected = hashlib.sha1("Hello".encode('utf-8')).hexdigest()
        actual = get_hashed_password_with_sha512("Hello")
        self.assertNotEqual(expected, actual)
