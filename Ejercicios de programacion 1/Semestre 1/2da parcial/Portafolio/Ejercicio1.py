from guizero import App, Text, PushButton, error, TextBox, info

def procesar_numero():
    try:
        numero = int(input_box.value)
        if numero < 0:
            error("Error", "Ingresa un número mayor o igual a cero.")
        else:
            resultado = 0 if numero % 2 == 0 else 1
            for _ in range(numero):

                info("Resultado", f"Variable: {resultado}")
    except ValueError:
        error("Error", "Ingresa un número válido.")

app = App("Verificador Par/Impar", width=300, height=150)

Text(app, "¿Qué numero quieres ingresar?:")
input_box = TextBox(app, width=5)

button = PushButton(app, procesar_numero, text="Procesar")

app.display()