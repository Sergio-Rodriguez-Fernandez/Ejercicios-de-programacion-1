from guizero import App, Box, PushButton, Text, TextBox, error, info, yesno

alumnos_compras = []  
total_alumnos = 0
alumno_actual = 1
finalizar_dia = None  
alumnos_atendidos = 1 

def mostrar_resumen():
    resumen_text.clear()
    resumen_text.append("Resumen de compras:")
    for producto, cantidad in alumnos_compras[alumno_actual - 1].items():
        if cantidad == 1:
            resumen_text.append(f"{producto}: {cantidad} comprado")
        else:
            resumen_text.append(f"{producto}: {cantidad} comprados")
    resumen_text.append(f"Total de alumnos atendidos: {alumnos_atendidos}")

def comprar_producto(producto):
    confirmar_compra = yesno("Confirmar Compra", f"¿El {alumno_actual}º alumno compró {producto.lower()}?")
    if confirmar_compra:
        alumnos_compras[alumno_actual - 1][producto] += 1  
        mensaje_compra.value = f"¡Compra registrada: {producto.lower()}!"
        mostrar_resumen()
        mostrar_compra(producto)
        app.after(3000, limpiar_mensaje_compra)

def limpiar_mensaje_compra():
    mensaje_compra.value = ""

def mostrar_compra(producto):
    info("Compra del Alumno", f"El {alumno_actual}º alumno compró un(a) {producto.lower()}")

def iniciar_compras():
    global alumno_actual, finalizar_dia, alumnos_atendidos
    if alumno_actual < total_alumnos:
        mensaje_compra.value = ""
        pregunta_alumno.value = f"¿Qué va a comprar el {alumno_actual + 1}º alumno?"
        for producto, boton in botones_compra.items():
            boton.enable()
        mostrar_resumen()
        if alumno_actual == total_alumnos - 1:  
            finalizar_dia = PushButton(ventas_box, text="Finalizar Día", command=finalizar_compras, grid=[6, 9, 2, 1])
            siguiente_alumno.hide()
        alumno_actual += 1
        alumnos_atendidos += 1  
    else:
        mensaje_compra.value = "No hay más alumnos para atender."

def finalizar_compras():
    mensaje_ventas = "Resumen de ventas del día:"
    total_vendidos = 0  

    for producto, cantidad in alumnos_compras[alumno_actual - 1].items():
        mensaje_ventas += f"\n{producto}: {cantidad} vendidos"
        total_vendidos += cantidad  

    mensaje_ventas += f"\nTotal de alumnos atendidos: {alumnos_atendidos}"
    mensaje_ventas += f"\nTotal de productos vendidos en el día: {total_vendidos}"  

    if yesno("Resumen de Ventas", mensaje_ventas + "\n\n¿Desea finalizar el día?"):
        reiniciar_aplicacion()

def mostrar_alumno_anterior():
    global alumno_actual, finalizar_dia, alumnos_atendidos
    if alumno_actual > 1:
        alumno_actual -= 1
        alumnos_atendidos -= 1  
        mensaje_compra.value = ""
        pregunta_alumno.value = f"¿Qué va a comprar el {alumno_actual}º alumno?"
        siguiente_alumno.show()  

        if finalizar_dia is not None and finalizar_dia.visible:
            finalizar_dia.hide()

        if total_alumnos == 1:
            finalizar_dia.hide()  
    else:
        error("Error", "No hay alumnos anteriores.")
        if total_alumnos == 1:
            finalizar_dia.hide()  

def reiniciar_compra():
    confirmar_reinicio = yesno("Confirmar Reinicio", "¿Seguro que desea reiniciar la compra actual?")
    if confirmar_reinicio:
        for producto in productos_comprados:
            productos_comprados[producto] = 0
        mensaje_compra.value = ""
        mostrar_resumen()

def ingresar_alumnos():
    num_alumnos = input_alumnos.value
    if not num_alumnos.isdigit() or int(num_alumnos) <= 0:
        error("Error", "Ingrese un número válido de alumnos.")
        return
    global total_alumnos, finalizar_dia, alumnos_compras  
    
    alumnos_compras = [{"Torta": 0, "Taco": 0, "Hot Dog": 0, "Pizza": 0} for _ in range(total_alumnos)]
    
    mensaje_confirmacion = f"¿Asistieron {num_alumnos} alumno(s) a la tienda hoy?"  
    if num_alumnos == "1":
        mensaje_confirmacion = "¿Asistió 1 alumno a la tienda hoy?"  
    if yesno("Verificación", mensaje_confirmacion):
        input_alumnos.disable()
        input_alumnos_button.disable()
        for producto, boton in botones_compra.items():
            boton.show()
        ver_compra.show()
        reiniciar_compra.show()
        pregunta_alumno.value = f"¿Qué va a comprar el 1º alumno?"  
        if total_alumnos == 1:
            siguiente_alumno.hide()
        else:
            siguiente_alumno.show()
        alumno_anterior.show()
        mostrar_resumen()
        if total_alumnos == 1:
            finalizar_dia = PushButton(ventas_box, text="Finalizar Día", command=finalizar_compras, grid=[6, 9, 2, 1])
    else:
        total_alumnos = 0
        input_alumnos.value = ""

import sys
import subprocess

def reiniciar_aplicacion():
    global alumno_actual, finalizar_dia, alumnos_atendidos, total_alumnos
    alumno_actual = 1
    finalizar_dia = None
    mensaje_compra.value = ""
    pregunta_alumno.value = "¿Qué va a comprar el 1º alumno?"
    siguiente_alumno.show()
    alumno_anterior.hide()
    total_alumnos = 0
    alumnos_atendidos = 0
    input_alumnos.enable()
    input_alumnos_button.enable()
    input_alumnos.value = ""
    for alumno_compras in alumnos_compras:
        for producto in alumno_compras:
            alumno_compras[producto] = 0
    for producto, boton in botones_compra.items():
        boton.hide()
    ver_compra.hide()
    reiniciar_compra.hide()
    resumen_text.hide()

    app.destroy()

    subprocess.Popen([sys.executable, __file__])

def ver_compra():
    mensaje_ver_compra = f"Resumen de compras del {alumno_actual}º alumno:"
    for producto, cantidad in alumnos_compras[alumno_actual - 1].items():
        if cantidad > 0:
            mensaje_ver_compra += f"\n{producto}: {cantidad} comprado(s)"
    if mensaje_ver_compra == f"Resumen de compras del {alumno_actual}º alumno:":
        mensaje_ver_compra = f"El {alumno_actual}º alumno no ha realizado compras todavía."
    info(f"Resumen de Compra del Alumno {alumno_actual}", mensaje_ver_compra)

app = App("Tienda 'Brankos'")
ventas_box = Box(app, layout="grid")

input_alumnos_label = Text(ventas_box, text="Ingrese el número de alumnos:", grid=[0, 0, 4, 1])
input_alumnos = TextBox(ventas_box, grid=[4, 0, 2, 1])
input_alumnos_button = PushButton(ventas_box, text="Aceptar", command=ingresar_alumnos, grid=[6, 0, 2, 1])

menu_text = Text(ventas_box, text="Menú: Torta, Taco, Hot Dog, Pizza", grid=[0, 1, 8, 1])

pregunta_alumno = Text(ventas_box, text="", grid=[0, 2, 8, 1])

mensaje_compra = Text(ventas_box, text="", grid=[0, 3, 8, 1])

resumen_text = Text(ventas_box, text="Resumen de compras:", grid=[0, 4, 8, 1])
resumen_text.hide()

productos = ["Torta", "Taco", "Hot Dog", "Pizza"]
botones_compra = {}

for i, producto in enumerate(productos):
    row = i + 5
    boton = PushButton(ventas_box, text=f"Comprar {producto}", command=lambda p=producto: comprar_producto(p), grid=[0, row, 8, 1])
    botones_compra[producto] = boton
    boton.hide()

ver_compra = PushButton(ventas_box, text="Ver Compra", command=ver_compra, grid=[0, 9, 2, 1])
ver_compra.hide()

reiniciar_compra = PushButton(ventas_box, text="Reiniciar Compra", command=reiniciar_compra, grid=[2, 9, 2, 1])
reiniciar_compra.hide()

alumno_anterior = PushButton(ventas_box, text="Alumno Anterior", command=mostrar_alumno_anterior, grid=[4, 9, 2, 1])
alumno_anterior.hide()

siguiente_alumno = PushButton(ventas_box, text="Siguiente Alumno", command=iniciar_compras, grid=[6, 9, 2, 1])
siguiente_alumno.hide()

app.display()
