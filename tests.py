import unittest

from romanos import convertir_a_numero

class RomanosTest(unittest.TestCase):

    def test_unidades(self):
        self.assertEqual(convertir_a_numero('I'),1)
        self.assertEqual(convertir_a_numero('V'),5)
        self.assertEqual(convertir_a_numero('X'),10)
        self.assertEqual(convertir_a_numero('L'),50)
        self.assertEqual(convertir_a_numero('C'),100)
        self.assertEqual(convertir_a_numero('D'),500)
        self.assertEqual(convertir_a_numero('M'),1000)

    def test_no_resta_mas_de_un_orden_de_magnitud(self):
        self.assertRaises(ValueError, convertir_a_numero, "IC")
        self.assertRaises(ValueError, convertir_a_numero, "VC")

    def test_no_restas_signos_multiplos_de_cinco(self):
        self.assertRaises(ValueError, convertir_a_numero, "VX")
        self.assertRaises(ValueError, convertir_a_numero, "LC")
        self.assertRaises(ValueError, convertir_a_numero, "DM")

    def test_no_restas_consecutivas(self):
        self.assertRaises(ValueError,convertir_a_numero,"MIXC")

    def no_repetir_simbolos_resta(self):
        self.assertRaises(ValueError,convertir_a_numero,"CCM")
        self.assertRaises(ValueError,convertir_a_numero,"XXC")
        self.assertRaises(ValueError,convertir_a_numero,"MMCCM")
        
        
        #Lo que viene a continuación dará ok si una llamada se cumple, no todas
        """
        with self.assertRaises(ValueError):
            convertir_a_numero("VX")
            convertir_a_numero("VX")
            convertir_a_numero("VX")
        """


if __name__ == '__main__':
    unittest.main()