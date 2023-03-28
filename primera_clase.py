import unittest

def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 4:
        return "IV"
    elif decimal == 5:
        return 'V'
    elif decimal <= 8:
        return 'V' * decimal
    elif decimal == 10:
        return 'X'
    elif decimal == 50:
        return 'L'
    elif decimal == 100:
        return 'C'
    elif decimal == 500:
        return 'D'
    else:
        return "M"
    
class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')
    def test_tres(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')

    def test_cincuenta(self):
        resultado= decimal_to_roman(50)
        self.assertEqual(resultado, "L")

    def test_cien(self):
        resultado= decimal_to_roman(100)
        self.assertEqual(resultado, "C")

    def test_quinientos(self):
        resultado= decimal_to_roman(500)
        self.assertEqual(resultado, "D")

    def test_mil(self):
        resultado= decimal_to_roman(1000)
        self.assertEqual(resultado, "M")
    
if __name__ == '__main__':
    unittest.main()