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





#print(convertir_en_romano("3a3"))
#print(convertir_en_romano(-3))
print(convertir_en_romano(444))
#convertir_en_romano("a")