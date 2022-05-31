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
    if not isinstance(numero,int):
        return "No has introducido un número" 
    if numero < 1 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y menor de 4000)"

    simbolos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}



    #Descomponer en unidades, decenas, centenas y unidades de millar el número
    #que nos pida
    #opción 1: división entera + módulo en cascada
    #opción 2: convertir en cadena y en función de la longitud y la posición
    #tener u,d,c,um
    
    divisores = [1000,100,10,1]
    
    
    for divisor in divisores:
        cociente = numero // divisor
        resto = numero % divisor
        print(divisor,cociente)
        numero = resto
        
    

#print(convertir_en_romano("3a3"))
#print(convertir_en_romano(-3))
print(convertir_en_romano(1123))
#convertir_en_romano("a")