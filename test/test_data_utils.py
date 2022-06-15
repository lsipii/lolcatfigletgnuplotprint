import unittest
from lolcatfigletgnuplotprint.utils.data_structures import make_dotdict


class TestDataUtils(unittest.TestCase):
    def test_make_dotdict(self):
        Configuration = make_dotdict(
            {
                "plotter": {"show_ip_address": False},
            }
        )
        self.assertEqual(Configuration.plotter.show_ip_address, False)


if __name__ == "__main__":
    unittest.main()
