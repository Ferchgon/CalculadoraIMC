#---------CREANDO VARIBLES PARA EL FORMULARIO ---------#

while True:
    print('------- CALCULADORA DE IMC -------')

    while True:
        nombre = input('Ingrese su Nombre: ').strip() #Método .strip() para eliminar los espacios que existan
        if nombre.strip() and nombre.isalpha():  # Verifica si la variable no está vacía con .strip() y que sean solo letras con .isalpha()
            break  # Sale del bucle si se ingresa un valor válido
        else:
            print("****** ¡Error! Ingresa un valor válido *****")

    while True:
        apePaterno = input('Ingrese su Apellido Paterno: ').strip()
        if apePaterno.strip() and apePaterno.isalpha():  # Verifica si la variable no está vacía con .strip() y que sean solo letras con .isalpha()
            break  # Sale del bucle si se ingresa un valor válido
        else:
            print("****** ¡Error! Ingresa un valor válido *****")

    while True:
        apeMaterno = input('Ingrese su Apellido Materno: ').strip()
        if apeMaterno.strip() and apeMaterno.isalpha():  # Verifica si la variable no está vacía con .strip() y que sean solo letras con .isalpha()
            break  # Sale del bucle si se ingresa un valor válido
        else:
            print("****** ¡Error! Ingresa un valor válido *****")

    while True:
        try:
            edad = int(input('Ingrese su edad en años: '))
            break
        except ValueError:
            print("****** ¡Error! Ingresa un valor válido *****")

    while True:
        try:
            peso = float(input('Ingrese su peso en kg: '))
            break
        except ValueError:
            print("****** ¡Error! Ingresa un valor válido *****")

    while True:
        try:
            estatura = float(input('Ingrese su estatura en metros: '))
            break
        except ValueError:
            print("****** ¡Error! Ingresa un valor válido *****")

    IMC = peso / estatura**2


    #****** Se compara el IMC para ver su condición ******
    if IMC <= 18.9 :
        mensaje = 'Peso Bajo'
    elif IMC >= 19.00 and IMC <= 24.99 :
        mensaje = 'Peso Normal'
    elif IMC >= 25.00 and IMC <= 29.99 :
        mensaje = 'Sobrepeso'
    elif IMC >= 30.00 and IMC <= 34.99 :
        mensaje = 'Obesidad leve'
    elif IMC >= 35.00 and IMC <= 39.99 :
        mensaje = 'Obesidad media'
    elif IMC >= 40.00 :
        mensaje = 'Obesidad mórbida'

    #******Se imprimen los datos de la persona******
    print(f""" 
    ************** DATOS **************
    Nombre: {nombre} {apePaterno} {apeMaterno}
    Edad: {edad} años
    Estatura: {estatura}m
    Peso: {peso}kg
        
    Tu IMC es de {IMC:.2f}

    Condición: {mensaje.upper()}
    """)

    respuesta = input("¿Deseas calcular otro IMC? (si/no): ").strip().lower()
    if respuesta != "si" and respuesta != "s":
        print("¡Hasta luego!")
        break  # Sale del bucle exterior