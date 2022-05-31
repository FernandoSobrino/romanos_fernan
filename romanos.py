def convertir_en_romano(numero):
    millares = ["","M","MM","MMM"]
    centenas = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    decenas = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    unidades = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    
    if not isinstance(numero,int):
        return "No has introducido un número" 
    if numero < 1 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y menor de 4000)"
    
    divisores = [1000,100,10,1]
    factores = []
    
    for divisor in divisores:
        cociente = numero // divisor
        resto = numero % divisor
        factores.append(cociente)
        numero = resto

    r_millares = millares[factores[0]]
    r_centenas = centenas[factores[1]]
    r_decenas = decenas[factores[2]]
    r_unidades = unidades[factores[3]]

    return f"{r_millares}{r_centenas}{r_decenas}{r_unidades}"


def convertir_a_numero(romano):
    digitos_romanos = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    """
    MCXXIII : 1123
        - El dato se lee de izquierda a derecha
        - Convertir cada "letra" en su "valor"
        - Sumo los valores si a la izquierda hay un dígito mayor que a la derecha
        - Resto si el valor de la izquierda es menor que el de la derecha
        
    """
    resultado = 0
    anterior = 0
    for letra in romano:
        actual = digitos_romanos[letra]
        
        if anterior >= actual:
            resultado = resultado + actual
        else:
            resultado = resultado - anterior
            resultado = resultado + (actual - anterior)
        
        anterior = actual
    return resultado

print(convertir_a_numero("IV"))
print(convertir_a_numero("MCXXIII"))
print(convertir_a_numero("MCXXXIV"))
print(convertir_a_numero("IC"))