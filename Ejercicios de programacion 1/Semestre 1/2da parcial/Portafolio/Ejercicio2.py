from guizero import App, Box, TextBox, PushButton, info

def calcular_minutos_totales():
    try:
        horas = int(txt_horas.value)
        minutos = int(txt_minutos.value)
        segundos = int(txt_segundos.value)

        if horas < 0 or minutos < 0 or segundos < 0:
            info("Error", "No se pueden ingresar valores negativos.")
        else:
            minutos_totales = (horas * 60) + minutos + (segundos / 60)
            mensaje = f"Minutos totales: {minutos_totales:.2f} minutos"
            info("Resultado", mensaje)
    except ValueError:
        info("Error", "Ingresa un valor numérico válido para horas, minutos y segundos.")

app = App("Calculadora de Tiempo")

box = Box(app, layout="grid")

txt_horas_label = TextBox(box, text="Horas:", grid=[0, 0])
txt_horas = TextBox(box, grid=[1, 0])

txt_minutos_label = TextBox(box, text="Minutos:", grid=[0, 1])
txt_minutos = TextBox(box, grid=[1, 1])

txt_segundos_label = TextBox(box, text="Segundos:", grid=[0, 2])
txt_segundos = TextBox(box, grid=[1, 2])

btn_calcular = PushButton(box, text="Calcular", command=calcular_minutos_totales, grid=[0, 3, 2, 1])

app.display()