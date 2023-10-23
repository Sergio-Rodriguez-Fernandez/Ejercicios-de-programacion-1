from guizero import App, Box, Text, TextBox, PushButton, error, info

numeros = []
cantidad_numeros = 0
numero_actual = 1

def agregar_numero():
    global numero_actual
    try:
        numero = int(entrada_numero.value)
        if numero >= 0:
            numeros.append(numero)
            entrada_numero.clear()
            numeros_label.value = f"Números ingresados:\n{obtener_numeros_formateados()}"
            if len(numeros) >= cantidad_numeros:
                agregar_button.disable()
                entrada_numero.disable()
                calcular_button.enable()  
            numero_actual += 1
        else:
            error("Error", "Ingrese un número entero positivo.")
    except ValueError:
        error("Error", "Ingrese un número entero válido.")

def obtener_numeros_formateados():
    numeros_formateados = ""
    for i, numero in enumerate(numeros):
        numeros_formateados += f"Número {i + 1}: {numero}\n"
    return numeros_formateados

def calcular_suma():
    suma_pares = 0
    suma_impares = 0
    for numero in numeros:
        if numero % 2 == 0:  
            suma_pares += numero ** 2
        else:  
            suma_impares += numero ** 3

    resultado = f'Suma de cuadrados de pares: {suma_pares}\nSuma de cubos de impares: {suma_impares}'
    info("Resultado", resultado)

def reiniciar():
    global numeros, cantidad_numeros, numero_actual
    numeros = []
    cantidad_numeros = 0
    numero_actual = 1
    entrada_cantidad.enable()
    entrada_numero.disable()
    agregar_button.disable()
    calcular_button.disable()
    numeros_label.value = ""
    resultado_text.value = ""
    entrada_numero.clear()
    entrada_cantidad.clear()
    indicacion_label.value = ""
    solicitar_button.enable()
    reiniciar_button.disable()

def solicitar_cantidad():
    global cantidad_numeros, numero_actual
    try:
        cantidad = int(entrada_cantidad.value)
        if cantidad > 0:
            cantidad_numeros = cantidad
            entrada_numero.enable()
            agregar_button.enable()
            calcular_button.disable()  
            entrada_cantidad.disable()
            solicitar_button.disable()
            indicacion_label.value = "Ingrese números uno por uno:"
            numero_actual = 1
            entrada_numero.enable()
            reiniciar_button.enable()  
        else:
            error("Error", "Ingrese una cantidad válida.")
    except ValueError:
        error("Error", "Ingrese una cantidad válida.")

app = App("Calculadora de Suma de Cuadrados y Cubos")

instrucciones = Text(app, "Ingrese la cantidad de números a sumar:")
entrada_cantidad = TextBox(app)
solicitar_button = PushButton(app, text="Solicitar Cantidad", command=solicitar_cantidad)
indicacion_label = Text(app, "")
entrada_numero = TextBox(app, enabled=False)
agregar_button = PushButton(app, text="Agregar Número", command=agregar_numero, enabled=False)
numeros_label = Text(app, "")
calcular_button = PushButton(app, text="Calcular Suma", command=calcular_suma, enabled=False)
resultado_text = Text(app, "")
reiniciar_button = PushButton(app, text="Reiniciar", command=reiniciar, enabled=False)

app.display()