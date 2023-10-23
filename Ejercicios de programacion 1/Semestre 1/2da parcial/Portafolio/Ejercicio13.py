from guizero import App, Box, Text, PushButton, TextBox, error, info

def calcular_edad():
    try:
        año_nacimiento = int(entrada_año_nacimiento.value)

        if año_nacimiento < 0:
            error("Error", "El año de nacimiento no puede ser menor que 0.")
        else:
            año_actual = 2023

            if año_nacimiento > año_actual:
                error("Error", "El año de nacimiento no puede ser mayor que el año actual.")
            else:
                edad = año_actual - año_nacimiento + 1

                if edad == 1:
                    mensaje = "Edad el año siguiente: 1 año"
                else:
                    mensaje = f"Edad el año siguiente: {edad} años"

                info("Resultado", mensaje)
    except ValueError:
        error("Error", "Ingresa un año de nacimiento válido.")

app = App("Calculadora de Edad")
box = Box(app, layout="grid")

etiqueta_descriptiva = Text(box, text="Calculadora de Edad para el Año Siguiente", grid=[0, 0, 3, 1])

etiqueta_año_nacimiento = Text(box, text="Año de nacimiento:", grid=[0, 1])
entrada_año_nacimiento = TextBox(box, grid=[1, 1])

boton_calcular = PushButton(box, text="Calcular", command=calcular_edad, grid=[2, 1])

app.display()