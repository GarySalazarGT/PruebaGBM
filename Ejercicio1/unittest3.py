import unittest

import palindromo


class UnittTestPalindromo(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertFalse(palindromo.is_palindrome("Mario"))


if __name__ == "__main__":
    file = './Ejercicio1/output3.txt'
    with open(file, "w") as f:
        runner = unittest.TextTestRunner(f)
        
        unittest.main(testRunner=runner)