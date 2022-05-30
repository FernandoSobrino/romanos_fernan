def convertir_en_romano(numero):
    """
    Restricciones:
        - Es un número natural
        - El número está entre 0 y 3999
            - no es negativo
            - no es mayor que 3999
    El resultado es una cadena que contiene (I,V,X,L,C,D,M)
    Ideas para comprobar un entero:
        - convertir a int y si no se puede, error
        - isinstance()
        - type()
    """

    """
    try:
        numero_validado = int(numero)
    except ValueError:
        raise ValueError(f"{numero} no es un número válido")
        

    if numero_validado > 0 and numero_validado > 4000:
       return "OK"
    return "El número introducido no es válido"
    """
    if not isinstance(numero,int) or numero < 1 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y entero)"
    
    simbolos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    #Descomponer en unidades, decenas, centenas y unidades de millar el número que
    #que nos pida
    #opción 1: división entera + módulo en cascada
    #opción 2: convertir en cadena y en función de la longitud y la posición
    #tener u,d,c,um
    
    
print(convertir_en_romano("3a3"))
