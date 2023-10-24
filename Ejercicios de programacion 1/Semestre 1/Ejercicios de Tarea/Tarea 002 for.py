from guizero import App, TextBox, PushButton, Text
def mostrar_secuencia():
    n = int(entrada.value)
    secuencia = [i for i in range(n, n + 10, 1)]
    resultado.value = f"Secuencia: {', '.join(map(str, secuencia))}"

app = App("Secuencia (n) i = 1 ")

entrada = TextBox(app, text="2")
resultado = Text(app, text="Secuencia: ")

boton_mostrar = PushButton(app, text="Mostrar Secuencia", command=mostrar_secuencia)

app.display()

         