import unittest

from translator import englishToFrench, frenchToEnglish


class Test_E2F_Translator(unittest.TestCase):
    # Check that Hello returns Bonjour, and not Hello.  Also check for None/empty string cases. 
    def test_e2f_translation1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_e2f_translation2(self):
        self.assertNotEqual(englishToFrench("Hello"), "Hello")

    def test_e2f_translation3(self):
        self.assertNotEqual(englishToFrench("None"), '')

    def test_e2f_translation4(self):
        self.assertNotEqual(englishToFrench(0), 0)


class Test_F2E_Translator(unittest.TestCase):
    # Check that Bonjour returns Hello, and not Bonjour.  Also check for None/empty string cases. 

    def test_f2e_translation1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test_f2e_translation2(self):
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")

    def test_f2e_translation3(self):
        self.assertNotEqual(frenchToEnglish("Néant"), '')

    def test_f2e_translation4(self):
        self.assertNotEqual(frenchToEnglish(0), 0)


if __name__ == '__main__':
    unittest.main()