import unittest

import palindromo


class UnittTestPalindromo(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(palindromo.is_palindrome("Ada"))


if __name__ == "__main__":
    file = './Ejercicio1/output1.txt'
    with open(file, "w") as f:
        runner = unittest.TextTestRunner(f)
        
        unittest.main(testRunner=runner)