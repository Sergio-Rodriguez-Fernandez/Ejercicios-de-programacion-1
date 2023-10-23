from guizero import App, Box, TextBox, PushButton, error, info

def realizar_operacion(operacion):
    try:
        num1 = float(txt_num1.value)
        num2 = float(txt_num2.value)

        if num1 < 0 or num2 < 0:
            error("Error", "Los números no pueden ser menores a 0.")
            return

        resultado = 0

        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2
        elif operacion == "Dividir":
            if num2 == 0:
                error("Error", "No se puede dividir por cero.")
                return
            resultado = num1 / num2

        info("Resultado", f"El resultado de la operación {operacion} es {resultado:.2f}")
    except ValueError:
        error("Error", "Ingresa valores numéricos válidos para los números.")

app = App("Calculadora de Números", width=600, height=400)

box = Box(app, layout="grid", width="fill", height="fill")

txt_num1_label = TextBox(box, text="Primer número:", grid=[0, 0], width=20,enabled=False)  
txt_num1 = TextBox(box, grid=[1, 0], width=20)  

txt_num2_label = TextBox(box, text="Segundo número:", grid=[0, 1], width=20,enabled=False)
txt_num2 = TextBox(box, grid=[1, 1], width=20)  

btn_sumar = PushButton(box, text="Sumar", args=["Sumar"], command=realizar_operacion, grid=[0, 2], width=10)
btn_restar = PushButton(box, text="Restar", args=["Restar"], command=realizar_operacion, grid=[1, 2], width=10)
btn_multiplicar = PushButton(box, text="Multiplicar", args=["Multiplicar"], command=realizar_operacion, grid=[0, 3], width=10)
btn_dividir = PushButton(box, text="Dividir", args=["Dividir"], command=realizar_operacion, grid=[1, 3], width=10)

app.display()