import unittest

from app.utils.json_utils import is_not_json_request


class JsonUtilsTest(unittest.TestCase):

    def test_string_is_not_json(self):
        with self.assertRaises(AttributeError) as ex:
            is_not_json_request("Hello")
            self.assertEqual("'str' object has no attribute 'json'" in ex.exception)
