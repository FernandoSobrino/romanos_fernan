def convertir_en_romano(numero):
    millares = ["","M","MM","MMM"]
    centenas = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    decenas = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    unidades = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    
    conversores = [millares, centenas, decenas, unidades]

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

    resultado = ""
    for pos, factor in enumerate(factores):
        resultado = resultado + conversores[pos][factor]

    return resultado

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
    restado = False
    cuenta_repetidos = 0

    for letra in romano:
        actual = digitos_romanos[letra]

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


if __name__ == '__main__':
    """
    print(convertir_a_numero("IV"))
    print(convertir_a_numero("MCXXIII"))
    print(convertir_a_numero("MCXXXIV"))
    print(convertir_a_numero("IC"))
    print(convertir_a_numero("VX"))
    """
    print(convertir_a_numero("VX"))


    