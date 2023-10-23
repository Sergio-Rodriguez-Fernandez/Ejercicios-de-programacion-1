from guizero import App, Text, PushButton, TextBox, error, info

def mostrar_dia_semana():
    entrada = textbox_numero.value
    
    try:
        numero = int(entrada)
        if 1 <= numero <= 7:
            resultado = f"El {obtener_numero_ordinal(numero)} día de la semana es el {obtener_dia_semana(numero)}."
            info("Resultado", resultado)
            textbox_numero.clear()
        else:
            raise ValueError("Número fuera de rango")
    except ValueError:
        error("Error", "Entrada no válida. Por favor, ingrese un número entero del 1 al 7.")
        textbox_numero.clear()

def obtener_numero_ordinal(numero):
    if 1 <= numero <= 7:
        ordinales = ["primer", "segundo", "tercer", "cuarto", "quinto", "sexto", "séptimo"]
        return ordinales[numero - 1]
    return ""

def obtener_dia_semana(numero):
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    return dias_semana[numero - 1]

app = App("Día de la Semana", width=350, height=250)

texto_ingresar_numero = Text(app, "Ingrese el número del día de la semana (1-7):")
textbox_numero = TextBox(app, width=5)
boton_mostrar = PushButton(app, text="Mostrar", command=mostrar_dia_semana)

app.display()
