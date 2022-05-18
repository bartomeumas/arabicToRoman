import unittest 
import program 

class TestArabicToRoman(unittest.TestCase):
    def test_arabicToRoman(self):
        self.assertEqual(program.printRoman(5), "V")

    def test_arabicToRoman2(self):
        self.assertEqual(program.printRoman(14), "XIV")

    def test_arabicToRoman3(self):
        self.assertEqual(program.printRoman(900), "CM")

    def test_arabicToRoman4(self):
        self.assertEqual(program.printRoman(3549), "MMMDXLIX")

    def test_arabicToRoman5(self):
        self.assertEqual(program.printRoman(456), "CDLVI")


if __name__ == "__main__":
    unittest.main()