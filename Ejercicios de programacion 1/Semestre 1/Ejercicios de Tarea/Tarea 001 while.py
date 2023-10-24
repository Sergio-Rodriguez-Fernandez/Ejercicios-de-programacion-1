from guizero import App, TextBox, PushButton, Text
def mostrar_secuencia():
    n = int(entrada.value)
    i = 0
    secuencia = []

    while i < 10:
        secuencia.append(2 * (n + i * 2))
        i += 1

    resultado.value = f"Secuencia: {', '.join(map(str, secuencia))}"

app = App("Secuencia 2(n)")
entrada = TextBox(app, text="2")
resultado = Text(app, text="Secuencia: ")
boton_mostrar = PushButton(app, text="Mostrar Secuencia", command=mostrar_secuencia)

app.display()
