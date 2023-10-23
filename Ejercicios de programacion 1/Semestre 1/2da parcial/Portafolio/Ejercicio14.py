from guizero import App, Box, TextBox, PushButton, Text, info, error

numeros = []

def agregar_numero():
    numero = entry.value
    if not numero:
        error("Error", "Ingrese un número antes de agregarlo.")
        return
    try:
        numero = int(numero)
        if 5 <= numero <= 10:
            numeros.append(numero)
            actualizar_numeros_agregados()
            entry.value = ""
            if len(numeros) == 5:
                calcular_button.enable()  
                agregar_button.disable()
        else:
            error("Error", "Ingrese un número entre 5 y 10.")
            entry.value = ""
    except ValueError:
        error("Error", "Ingrese un número válido.")
        entry.value = ""

def actualizar_numeros_agregados():
    numeros_agregados_text.clear()
    for i, num in enumerate(numeros, start=1):
        numeros_agregados_text.append(f"Número {i}: {num}\n")

def calcular_suma():
    resultado = sum(numeros)
    mensaje = f"La suma es: {resultado}"
    info("Resultado", mensaje)
    entry.disable()
    agregar_button.disable()

def reiniciar():
    numeros.clear()
    entry.enable()
    entry.value = ""
    numeros_agregados_text.clear()
    resultado_text.value = ""
    error_text.value = ""
    agregar_button.enable()
    calcular_button.disable()  

app = App("Suma de 5 números entre 5 y 10")

box = Box(app, layout="grid")

instrucciones_text = Text(box, text='Ingrese 5 números entre 5 y 10 uno por uno.', grid=[0, 0])

entry = TextBox(box, grid=[0, 1], width=5)
agregar_button = PushButton(box, text='Agregar Número', command=agregar_numero, grid=[0, 2])
calcular_button = PushButton(box, text='Calcular Suma', command=calcular_suma, grid=[0, 3])
reiniciar_button = PushButton(box, text='Reiniciar', command=reiniciar, grid=[0, 4])
calcular_button.disable()  

numeros_agregados_text = Text(box, text='Números agregados:', grid=[0, 5])

resultado_text = Text(box, text='', grid=[0, 6])
error_text = Text(box, text='', grid=[0, 7])

app.display()