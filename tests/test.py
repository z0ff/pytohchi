import unittest
from pytohchi import put_root_to_head


class MyTestCase(unittest.TestCase):
    def test_put_predicate_to_first(self):
        s = "吾輩は猫である。名前はまだ無い。"
        expected = "猫である。吾輩は。無い。名前はまだ。"
        inverted = put_root_to_head(s)
        self.assertEqual(expected, inverted)


if __name__ == '__main__':
    unittest.main()
