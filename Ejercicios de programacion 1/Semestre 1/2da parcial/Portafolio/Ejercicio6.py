from guizero import App, Box, Text, TextBox, PushButton, info, error

numeros = []
promedio = 0

def agregar_numero():
    numero_str = entrada_numero.value
    if numero_str.isdigit():
        numero = int(numero_str)
        if numero > 0:
            numeros.append(numero)
            entrada_numero.clear()
        else:
            error("Error", "Ingrese números positivos.")
    else:
        error("Error", "Ingrese números válidos.")

def calcular_promedio():
    if numeros:
        promedio = sum(numeros) / len(numeros)
        info("Resultado", f"Promedio: {promedio:.2f}")
    else:
        error("Error", "No se ingresaron números.")

def ver_numeros():
    if numeros:
        numeros_str = ', '.join(map(str, numeros))
        info("Números ingresados", f"Números: {numeros_str}")
    else:
        error("Error", "No se ingresaron números.")

def reiniciar_valores():
    numeros.clear()
    entrada_numero.clear()
    resultado_text.clear()

app = App("Calculadora de Promedio", width=400, height=250)

titulo = Text(app, "Ingrese números positivos uno por uno:")
entrada_numero = TextBox(app, width=40)
agregar_button = PushButton(app, text="Agregar Número", command=agregar_numero)
calcular_button = PushButton(app, text="Calcular Promedio", command=calcular_promedio)
ver_numeros_button = PushButton(app, text="Ver Números", command=ver_numeros)
reiniciar_button = PushButton(app, text="Reiniciar Valores", command=reiniciar_valores)
resultado_text = Text(app, "")

app.display()