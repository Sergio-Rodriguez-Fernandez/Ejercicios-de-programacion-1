from guizero import App, TextBox, PushButton, Text, info, error

def generar_secuencia():
    try:
        repeticiones = int(entrada_repeticiones.value)
        if repeticiones < 1:
            error("Error", "Por favor, ingrese un número mayor o igual a 1")
            entrada_repeticiones.value = ""  
            return
        secuencia = ''.join(['01'[i % 2] for i in range(repeticiones)])
        info("Resultado", secuencia)
        entrada_repeticiones.clear()  # Limpiar la casilla de entrada
    except ValueError:
        error("Error", "Por favor, ingrese un número válido")
        entrada_repeticiones.value = ""  

app = App("Generador de Secuencia 0 y 1", width=350, height=200)

Text(app, "Repeticiones:")
entrada_repeticiones = TextBox(app, "")

boton_generar = PushButton(app, text="Generar Secuencia", command=generar_secuencia)

app.display()