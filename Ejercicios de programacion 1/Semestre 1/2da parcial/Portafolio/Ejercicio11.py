from guizero import App, Box, TextBox, PushButton, Text, error, info

numeros = []
contador_numeros = 1
cantidad_numeros = 1
app = None

def agregar_numero():
    global contador_numeros
    numero = num_input.value
    if numero.isnumeric() and int(numero) >= 0:
        numeros.append(int(numero))
        contador_numeros += 1
        num_input.clear()

        if contador_numeros > cantidad_numeros:
            agregar_button.disable()
            calcular_button.enable()
    else:
        error("Número Inválido", "Por favor, ingrese un número válido (mayor o igual a 0).")

def calcular_suma_cuadrados():
    suma = sum([n**2 for n in numeros])
    resultado_text = f"La suma de los cuadrados es: {suma}"
    info("Resultado", resultado_text)
    reiniciar_calculadora()

def ver_numeros():
    if not numeros:
        info("Números Ingresados", "Todavía no se han ingresado números.")
    else:
        numeros_text = "\n".join([f"Número {i}: {num}" for i, num in enumerate(numeros, start=1)])
        info("Números Ingresados", numeros_text)

def pedir_cantidad_numeros():
    global cantidad_numeros
    cantidad = cantidad_numeros_input.value
    if cantidad.isnumeric() and int(cantidad) >= 1:
        cantidad_numeros = int(cantidad)
        cantidad_numeros_input_box.disable()
        pedir_cantidad_numeros_button.disable()
        cantidad_numeros_input_box.hide()
        contador_numeros = 1
        numeros.clear()
        num_input.enable()
        agregar_button.enable()
        pedir_numeros(cantidad_numeros)
    else:
        error("Número Inválido", "Por favor, ingrese una cantidad válida de números (mayor o igual a 1).")
        cantidad_numeros_input.clear()
        reiniciar_calculadora()

def pedir_numeros(cantidad_numeros):
    num_input_box.show()
    num_input_box.show()
    num_input.clear()
    calcular_button.disable()

def reiniciar_calculadora():
    contador_numeros = 1
    numeros.clear()
    cantidad_numeros_input_box.show()
    cantidad_numeros_input_box.enable()
    pedir_cantidad_numeros_button.enable()
    cantidad_numeros_input.clear()
    num_input_box.hide()
    agregar_button.disable()
    calcular_button.disable()
    num_input.disable()

app = App("Calculadora de Suma de Cuadrados", width=600, height=400)

input_box = Box(app, layout="grid")
Text(input_box, text="Cantidad de números:", grid=[0, 0])
cantidad_numeros_input = TextBox(input_box, grid=[1, 0])
pedir_cantidad_numeros_button = PushButton(input_box, text="Ingresar", command=pedir_cantidad_numeros, grid=[2, 0])

cantidad_numeros_input_box = Box(app, layout="grid")
Text(cantidad_numeros_input_box, text="Número de números a sumar:", grid=[0, 0])
cantidad_numeros_input_box.hide()

num_input_box = Box(app, layout="grid")
Text(num_input_box, text="Número:", grid=[0, 0])
num_input = TextBox(num_input_box, grid=[1, 0])
agregar_button = PushButton(num_input_box, text="Agregar", command=agregar_numero, grid=[2, 0])
num_input_box.hide()

calcular_button = PushButton(app, text="Calcular Suma de Cuadrados", command=calcular_suma_cuadrados)
calcular_button.disable()

ver_numeros_button = PushButton(app, text="Ver Números", command=ver_numeros)

reiniciar_button = PushButton(app, text="Reiniciar Calculadora", command=reiniciar_calculadora)

app.display()