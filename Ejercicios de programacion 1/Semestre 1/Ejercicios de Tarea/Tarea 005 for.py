from guizero import App, TextBox, PushButton, Text
def calcular_producto():
    num1 = int(entrada_num1.value)
    num2 = int(entrada_num2.value)
    producto = 0

    for _ in range(num2):
        producto += num1

    resultado.value = f"Producto: {producto}"
app = App("Producto mediante Sumas Sucesivas")

entrada_num1 = TextBox(app, text="0")
entrada_num2 = TextBox(app, text="0")
resultado = Text(app, text="Producto: ")

boton_calcular = PushButton(app, text="Calcular Producto", command=calcular_producto)

app.display()
