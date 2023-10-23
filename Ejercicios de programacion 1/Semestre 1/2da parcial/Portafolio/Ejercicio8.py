from guizero import App, Text, PushButton, TextBox, error, info

calificaciones = []
current_alumno = 1
max_alumnos = 26

def ingresar_calificacion():
    global current_alumno
    try:
        calificacion = float(input_calificacion.value)
        if 0.0 <= calificacion <= 10.0:
            calificaciones.append(calificacion)
            input_calificacion.clear()
            if current_alumno < max_alumnos:
                current_alumno_text.value = f"Calificación para Alumno {current_alumno + 1}:"
                current_alumno += 1
            if current_alumno == max_alumnos:
                boton_calcular_aprobados.enable()
                boton_ingresar_calificacion.disable()
                boton_ver_calificaciones.enable()
                input_calificacion.disable()
            if current_alumno >= max_alumnos:
                current_alumno_text.value = "Ingresaste todas las calificaciones."
        else:
            error("Error", "Ingresa una calificación válida (número decimal entre 0 y 10).")
            input_calificacion.clear()  
    except ValueError:
        error("Error", "Ingresa una calificación válida (número decimal entre 0 y 10).")
        input_calificacion.clear()  

def contar_aprobados():
    calificacion_aprobatoria = 7.0
    aprobados = sum(1 for calificacion in calificaciones if calificacion >= calificacion_aprobatoria)
    resultado.value = f"Alumnos aprobados: {aprobados}"
    info("Resultado Final", f"Alumnos aprobados: {aprobados}")

def ver_calificaciones():
    calificaciones_str = '\n'.join([f"Alumno {i + 1}: {calificacion:.2f}" for i, calificacion in enumerate(calificaciones)])
    info("Calificaciones de Alumnos", calificaciones_str)

def reiniciar_valores():
    global current_alumno
    calificaciones.clear()
    current_alumno = 1
    current_alumno_text.value = f"Calificación para Alumno {current_alumno}:"
    input_calificacion.clear()
    resultado.value = "Alumnos aprobados: "
    boton_calcular_aprobados.disable()
    boton_ingresar_calificacion.enable()
    boton_ver_calificaciones.disable()
    input_calificacion.enable()

app = App("Contador de Aprobados")

current_alumno_text = Text(app, text=f"Calificación para Alumno {current_alumno}:")
input_calificacion = TextBox(app, width=5)
boton_ingresar_calificacion = PushButton(app, text="Ingresar Calificación", command=ingresar_calificacion)
resultado = Text(app, text="Alumnos aprobados: ")
boton_calcular_aprobados = PushButton(app, text="Calcular Aprobados", command=contar_aprobados, enabled=False)
boton_ver_calificaciones = PushButton(app, text="Ver Calificaciones", command=ver_calificaciones, enabled=False)
boton_reiniciar_valores = PushButton(app, text="Reiniciar Valores", command=reiniciar_valores)

app.display()