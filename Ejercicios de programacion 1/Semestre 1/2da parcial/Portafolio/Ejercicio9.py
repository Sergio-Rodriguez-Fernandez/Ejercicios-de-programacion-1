from guizero import App, TextBox, PushButton, Text, error, info

def calcular_cuadrado():
    try:
        numero = int(input_box.value)
        if numero >= 0:
            resultado = numero ** 2
            info("Resultado", f"El cuadrado de {numero} es {resultado}")
        else:
            error("Error", "Por favor, ingrese un número positivo.")
            input_box.clear()
    except ValueError:
        error("Error", "Por favor, ingrese un número válido.")
        input_box.clear()

app = App("Calculadora de Cuadrado", width=300, height=150)

instrucción = Text(app, text="Ingrese un número:")

input_box = TextBox(app)

calculate_button = PushButton(app, text="Calcular Cuadrado", command=calcular_cuadrado)

app.display()