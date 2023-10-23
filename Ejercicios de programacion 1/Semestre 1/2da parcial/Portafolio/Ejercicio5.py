from guizero import App, Box, Text, PushButton, TextBox, info

def calcular_edad():
    try:
        año_actual = int(input_año_actual.value)
        año_nacimiento = int(input_año_nacimiento.value)

        if año_actual >= 0 and año_nacimiento >= 0 and año_nacimiento <= año_actual:
            edad = año_actual - año_nacimiento
            info("Resultado", f"Tu edad es: {edad} años")
        else:
            if año_actual < 0:
                info("Error", "El año actual debe ser mayor o igual a 0.")
            elif año_nacimiento < 0:
                info("Error", "El año de nacimiento debe ser mayor o igual a 0.")
            else:
                info("Error", "Por favor, ingresa valores válidos.")
    except ValueError:
        info("Error", "Por favor, ingresa valores numéricos.")

app = App("Calculadora de Edad", width=300, height=150)

box = Box(app, layout="grid")

texto_año_actual = Text(box, "Año actual:", grid=[0, 0])
input_año_actual = TextBox(box, grid=[1, 0])
texto_año_nacimiento = Text(box, "Año de nacimiento:", grid=[0, 1])
input_año_nacimiento = TextBox(box, grid=[1, 1])

calcular_button = PushButton(box, calcular_edad, text="Calcular Edad", grid=[1, 2])

app.display()