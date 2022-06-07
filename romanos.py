class RomanNumber:

    millares = [ "", "M", "MM", "MMM" ]
    centenas = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
    decenas = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
    unidades = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]

    conversores = [millares, centenas, decenas, unidades]

    def __init__(self, numero):
        if not isinstance(numero, int):
            raise ValueError("No has introducido un número")
        if numero < 1 or numero > 3999:
            raise ValueError ("El número introducido no es válido (debe ser positivo y menor que 4000)")
        self.numero = numero

    def int_a_romano(self):
        divisores = [1000, 100, 10, 1]
        factores = []
        numero = self.numero

        for divisor in divisores:
            cociente = numero // divisor
            resto = numero % divisor
            factores.append(cociente)
            numero = resto

        resultado = ""

        for pos, factor in enumerate(factores):
            resultado = resultado + self.conversores[pos][factor]

        return resultado