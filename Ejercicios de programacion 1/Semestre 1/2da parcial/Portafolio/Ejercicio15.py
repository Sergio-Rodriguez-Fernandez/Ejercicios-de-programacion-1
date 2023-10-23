from guizero import App, Box, PushButton, Text, TextBox, error, yesno

ventanas_empleados = {}
ventana_actual = None
contador_empleados = 1

def calcular_sueldo(empleado):
    sueldo_base_text = sueldo_base_inputs[empleado].value
    if not sueldo_base_text:
        error("Error", "Por favor, ingrese el sueldo base.")
    else:
        try:
            sueldo_base = float(sueldo_base_text)
            if sueldo_base < 0:
                error("Error", "El sueldo base no puede ser menor que 0.")
                sueldo_base_inputs[empleado].clear()
            else:
                canasta_basica = 0.05 * sueldo_base
                primas_antiguedad = 0.03 * sueldo_base
                deducciones = 0.2 if sueldo_base <= 10000 else 0.3
                impuesto = deducciones * sueldo_base
                sueldo_total = sueldo_base + canasta_basica + primas_antiguedad - impuesto
                resultado_labels[empleado].value = f"Sueldo Total: ${sueldo_total:.2f}\nImpuesto a pagar: ${impuesto:.2f}"
                sueldo_base_inputs[empleado].disable()
                restablecer_botones[empleado].enable()
                calcular_botones[empleado].disable()
        except ValueError:
            error("Error", "Por favor, ingrese un valor numérico válido para el sueldo base.")
            sueldo_base_inputs[empleado].clear()
            calcular_botones[empleado].disable()

def restablecer_sueldo(empleado):
    sueldo_base_inputs[empleado].enable()
    sueldo_base_inputs[empleado].clear()
    resultado_labels[empleado].value = ""
    calcular_botones[empleado].enable()
    restablecer_botones[empleado].disable()

def eliminar_empleado(empleado):
    if yesno("Eliminar Empleado", "¿Estás seguro de que deseas eliminar este empleado?"):
        ventanas_empleados[empleado].destroy()
        del ventanas_empleados[empleado]
        restablecer_empleados()
        actualizar_numeros_empleados()

def restablecer_empleados():
    global contador_empleados
    for empleado in ventanas_empleados.keys():
        ventanas_empleados[empleado].title = f"Calculadora de Sueldo - Empleado {empleado}"
    contador_empleados = len(ventanas_empleados) + 1

def actualizar_numeros_empleados():
    for empleado in ventanas_empleados.keys():
        calcular_botones[empleado].args = [empleado]
        restablecer_botones[empleado].args = [empleado]
        eliminar_botones[empleado].args = [empleado]

def encontrar_numero_empleado_disponible():
    empleados_actuales = ventanas_empleados.keys()
    for i in range(1, contador_empleados + 1):
        if i not in empleados_actuales:
            return i
    return contador_empleados + 1

def agregar_empleado():
    global ventana_actual, contador_empleados
    numero_empleado = encontrar_numero_empleado_disponible()
    nueva_ventana = App("Calculadora de Sueldo - Empleado " + str(numero_empleado), width=400, height=400)
    nueva_ventana.when_closed = lambda: eliminar_empleado(numero_empleado)
    ventanas_empleados[numero_empleado] = nueva_ventana
    ventana_actual = nueva_ventana
    empleado_container = Box(ventana_actual, layout="grid")
    empleado_label = Text(empleado_container, f"Empleado {numero_empleado}", grid=[0, 0])
    sueldo_base_label = Text(empleado_container, "Sueldo base:", grid=[0, 1])
    sueldo_base_input = TextBox(empleado_container, grid=[1, 1])
    sueldo_base_inputs[numero_empleado] = sueldo_base_input
    resultado_label = Text(empleado_container, "", grid=[0, 2])
    resultado_labels[numero_empleado] = resultado_label

    botones_box = Box(empleado_container, layout="grid", grid=[0, 3])
    calcular_button = PushButton(botones_box, text="Calcular", args=[numero_empleado], grid=[0, 0], command=calcular_sueldo)
    restablecer_button = PushButton(botones_box, text="Restablecer", args=[numero_empleado], grid=[1, 0], command=restablecer_sueldo)
    eliminar_button = PushButton(botones_box, text="Eliminar", args=[numero_empleado], grid=[2, 0], command=eliminar_empleado)
    restablecer_button.disable()
    restablecer_botones[numero_empleado] = restablecer_button
    calcular_botones[numero_empleado] = calcular_button
    eliminar_botones[numero_empleado] = eliminar_button

    contador_empleados = max(contador_empleados, numero_empleado + 1)

app = App("Calculadora de Sueldo - Empleado 1", width=400, height=400)

titulo = Text(app, "Cálculo de Sueldo y Deducciones")

sueldo_base_inputs = {}
resultado_labels = {}
restablecer_botones = {}
calcular_botones = {}
eliminar_botones = {}

agregar_empleado_button = PushButton(app, text="Agregar Empleado", command=agregar_empleado)

app.display()
