class RomanNumber:

    millares = [ "", "M", "MM", "MMM" ]
    centenas = [ "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" ]
    decenas = [ "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
    unidades = [ "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" ]
    conversores = [millares, centenas, decenas, unidades]

    digitos_romanos = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    

    def __init__(self, numero):
        
        if isinstance(numero,int):
            self.valor = numero
            self.cadena = self.int_a_romano()
        if isinstance(numero,str):
            self.cadena = numero
            self.valor = self.romano_a_int()

    def __str__(self) -> str:
        return self.cadena

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, otro):
        if isinstance(otro,RomanNumber):
            return self.valor == otro.valor
        if isinstance(otro,int):
            return self.valor == otro
        if isinstance(otro,str):
            return self.cadena == otro
        raise ValueError(f"{otro} debe ser un número romano, un entero o una cadena")

    def __add__(self,sumando):
        if isinstance(sumando,RomanNumber):
            return self.valor + sumando.valor
        if isinstance(sumando,int):
            return self.valor + sumando
        if isinstance(sumando,str):
            return self.valor + RomanNumber(sumando).valor

    def __radd__(self,sumando):
        return self.__add__(sumando)

    def validar_numero(self):
        """
        Comprueba que el 'valor' sea un entero 
        con valor entre 1 y 3999 (incluidos)
        """
        if not isinstance(self.valor, int):
            raise ValueError("No has introducido un número")
        if self.valor < 1 or self.valor > 3999:
            raise ValueError ("El número introducido no es válido (debe ser positivo y menor que 4000)")


    def int_a_romano(self):
        """
        Convierte el 'valor' numérico a su representación en 'cadena' como número romano. 
        """
        self.validar_numero()
        numero = self.valor
        divisores = [1000, 100, 10, 1]
        factores = []
        

        for divisor in divisores:
            cociente = numero // divisor
            resto = numero % divisor
            factores.append(cociente)
            numero = resto

        resultado = ""

        for pos, factor in enumerate(factores):
            resultado = resultado + self.conversores[pos][factor]

        return resultado

    def romano_a_int(self):
        """
        Obtiene el valor numérico de la representación de 'cadena'
        del número romano
        """
        romano = self.cadena
        resultado = 0
        anterior = 0
        restado = False
        cuenta_repetidos = 0

        for letra in romano:
            actual = self.digitos_romanos[letra]

            if anterior >= actual:
                resultado = resultado + actual
                restado = False
            else:
                if cuenta_repetidos == 1:
                    raise ValueError("No se puede restar símbolos repetidos")

                if restado:
                    raise ValueError("No se puede restar más de un símbolo")

                if anterior in (5,50,500):
                    raise ValueError("No se puede restar un número múltiplo de 5")

                if 0 < anterior*10 < actual:
                    raise ValueError("No se puede restar más de un orden de magnitud")
                
                resultado = resultado - anterior
                resultado = resultado + (actual - anterior)
                if anterior > 0:
                    restado = True

            if anterior == actual:
                cuenta_repetidos = cuenta_repetidos + 1
                if actual in (5, 50, 500):
                    raise ValueError("No se puede restar un número múltiplo de 5")
                if cuenta_repetidos > 2:
                    raise ValueError("No puedes tener más de tres símbolos iguales")
            else:
                cuenta_repetidos = 0
            
            anterior = actual
        return resultado