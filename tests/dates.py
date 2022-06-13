import unittest

from utils.dates import parse_past_date_text


class TestDateUtils(unittest.TestCase):
    def testDateComparissons(self):
        self.assertEqual(parse_past_date_text("2 days ago"), False)


if __name__ == "__main__":
    unittest.main()
