import unittest
import saltos


class UnitTestSaltos(unittest.TestCase):
    def test_saltos(self):
        self.assertEqual(saltos.min_jumps(10), 5)


if __name__ == "__main__":
    file = './Ejercicio3/output_saltos3.txt'
    with open(file, "w") as f:
        runner = unittest.TextTestRunner(f)
        
        unittest.main(testRunner=runner)