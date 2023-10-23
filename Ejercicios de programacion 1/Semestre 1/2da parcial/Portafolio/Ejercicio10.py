from guizero import App, Text

def obtener_numeros_pares():
    numeros_pares = [str(num) for num in range(2, 21, 2)]
    resultado.value = "\n".join(numeros_pares)

app = App("Números Pares del 1 al 20")

titulo = Text(app, text="Los números pares entre 1 y 20 son:")

resultado = Text(app, text="")

obtener_numeros_pares()

app.display()