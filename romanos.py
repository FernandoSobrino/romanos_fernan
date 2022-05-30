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
    
    
print(convertir_en_romano("3a3"))