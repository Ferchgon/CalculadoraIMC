# CalculadoraIMC

# Calculadora de IMC en Python

Esta es una calculadora de Índice de Masa Corporal (IMC) implementada en Python. El IMC es una medida que se utiliza para evaluar si una persona tiene un peso saludable en relación con su altura.
El programa empieza con un ciclo while, dentro de este ciclo se usan más ciclos while para capturar los datos de la persona y poder validar los datos ingresados, por ejemplo, en los input pertenecientes al nombre,
apellido paterno, apellido materno se utiliza el metodo strip() en el input para eliminar el espacio en blanco que pudiera haber ingresado el usuario por error al principio y al final de la entrada,
después se realiza su respectivo "if" en el que verifica que la variable no esté vacía, se utiliza el metodo .replace() para hacer una version de cada variable quitando los 
espacios sin alterar la variable (en caso de que la persona tenga dos nombres o sus apellidos lleven más de dos palabras) y usando el operador "and" se verifica también con el método .isalpha() que la variable solo
contenga letras sin caracteres especiales ni números. Si ambas condiciones no se cumplen se imprimirá un mensage de error pidiendo que se ingrese un valor válido 
y el ciclo while se repetirá hasta que las condiciones del "if" se cumplan.

En el caso de los datos Edad, Peso y Estatura, se utiliza la conversión de cada input a un dato de tipo "int" para la edad y "float" para el peso y la estatura, ya que por defecto los input son de tipo string
y se requiere que los datos sean números enteros y decimales respectivamente. En este caso su su ciclo while de estas variables cambia un poco ya que se está utilizando un bloque try y except para manejar posibles 
errores que puedan ocurrir durante la conversión del valor ingresado por el usuario a un valor entero o decimal.
En el bloque "try" se coloca el código que puede generar un error, y en el bloque except se coloca el mensaje de error en caso de que ocurra un error de tipo "ValueError".
"ValueError" se produce cuando el usuario ingresa algo que no puede ser convertido en un número entero o decimal, por ejemplo si el usuario ingresa letras o caracteres que no son un número.

Una vez que todos los datos son capturados correctamente se procede a calcular el IMC.
El IMC se calcula con la formula Peso / estatura2   -> Peso sobre estatura al cuadrado.
Después de calcular el IMC se hace una comparación utilizando "if" y "elif" para guardar una variable con el mensaje de acuerdo a la condicion del peso de la persona según su IMC.

Después se hace una impresión de los datos de la persona, agregando formato al nombre usando title(), "IMC:.2f" para formatear el IMC y que solo muestre 2 decimales y formateando en mayúsculas el mensaje usando upper()

Al final, se realiza la captura una respuesta del usuario preguntando si desea salir del programa, a este input se le eliminan los espacios en blanco
y se formatea en minúsculas, una vez hecho esto se compara con un "if" si la respuesta es diferente de "si" y es diferente de "s", pudiendo ser un "no" o cualquier otra letra o símbolo, el programa termina su ejecución.
Si la respuesta es "si" o "s" el ciclo while se repite y vuelve a empezar con la captura de datos.

## Uso

1. Ejecuta el archivo `CalcIMC.py`.

2. La calculadora te guiará a través del proceso de ingreso de tus datos:

    - Nombre: Ingresa sun nombre (solo letras).
    - Apellido Paterno: Ingresa su apellido paterno (solo letras).
    - Apellido Materno: Ingresa su apellido materno (solo letras).
    - Edad: Ingresa su edad en años (número entero).
    - Peso: Ingresa su peso en kg (número decimal).
    - Estatura: Ingresa su estatura en metros (número decimal).

3. Una vez que todos los datos hayan sido ingresados, la calculadora calculará automáticamente tu IMC y te proporcionará una clasificación de peso según la tabla proporcionada por el IMSS con los siguientes datos.
    Menor a 18.9   = peso bajo
    18.50 a 24.99   = peso normal
    25.00 a 29.99   = sobrepeso
    30.00 a 34.99   = obesidad leve
    35.00 a 39.99   = obesidad media
    Mayor a 40.0   = obesidad mórbida

5. Después de mostrar los resultados, se te preguntará si deseas calcular otro IMC. Ingresa "si" o "s" para continuar o ingrsa "no" o "n" o cualquier otra letra para salir del programa.


## EJEMPLO DE RESULTADO
------- CALCULADORA DE IMC -------
Ingrese su Nombre: Luis Fernando
Ingrese su Apellido Paterno: Gonzalez
Ingrese su Apellido Materno: Rojas
Ingrese su edad en años: 24
Ingrese su peso en kg: 65
Ingrese su estatura en metros: 1.65

************** DATOS **************
Nombre: Fernando Gonzalez Rojas
Edad: 24 años
Estatura: 1.65m
Peso: 65.0kg

Tu IMC es de 23.88
Condición: PESO NORMAL

¿Deseas calcular otro IMC? (si/no): no
