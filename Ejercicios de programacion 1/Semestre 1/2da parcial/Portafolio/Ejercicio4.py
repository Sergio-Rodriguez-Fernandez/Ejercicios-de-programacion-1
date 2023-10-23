from guizero import App, TextBox, PushButton, Text

def calcular_suma():
    num1 = float(input_numero1.value)
    num2 = float(input_numero2.value)
    num3 = float(input_numero3.value)
    
    if num1 < 0 or num2 < 0 or num3 < 0:
        resultado_text.value = "Error: Ingresa números mayores o iguales a 0"
    else:
        suma = num1 + num2 + num3
        resultado_text.value = f"La suma es: {suma}"

app = App("Suma de Números")

Text(app, "Ingresa tres números distintos:")
input_numero1 = TextBox(app)
input_numero2 = TextBox(app)
input_numero3 = TextBox(app)
resultado_text = Text(app, "")

calcular_button = PushButton(app, text="Calcular Suma", command=calcular_suma)

app.display()