from guizero import App, Text, TextBox, PushButton, info, error

n = None
entradas = []

def calcular_promedio():
    años_de_nacimiento = []
    for entrada in entradas:
        valor = entrada.value
        if valor:
            try:
                año = int(valor)
                if año < 0:
                    raise ValueError("Año de nacimiento negativo")
                años_de_nacimiento.append(año)
            except ValueError:
                error("Error", "Ingresa solo números enteros no negativos en los años de nacimiento.")
                return
        else:
            error("Error", "Dejaste una casilla en blanco. Ingresa los años de nacimiento.")
            return

    if años_de_nacimiento:
        edades = [2023 - año for año in años_de_nacimiento]
        promedio = sum(edades) / len(edades)
        resultado = f"La edad promedio es de: {promedio:.2f} años"
        info("Resultado", resultado)
    else:
        error("Error", "No se ingresaron años de nacimiento válidos.")

def aceptar_numero_personas():
    global n
    try:
        n = int(entrada_n_personas.value)
        if n < 1:
            raise ValueError("Número de personas no válido")
        entrada_n_personas.disable()
        boton_n_personas.disable()
        Text(app, "Ingresa los años de nacimiento:")
        for _ in range(n):
            entrada = TextBox(app)
            entrada.width = 5  
            entradas.append(entrada)
        calcular_btn.enabled = True
    except ValueError:
        error("Error", "El número de personas debe ser un número entero mayor o igual a 1.")
        entrada_n_personas.clear()

app = App("Calculadora de Edad Promedio", width=400, height=300)

Text(app, "Ingrese el número de personas (mínimo 1):")

entrada_n_personas = TextBox(app)
boton_n_personas = PushButton(app, text="Aceptar", command=aceptar_numero_personas)
calcular_btn = PushButton(app, text="Calcular Promedio", command=calcular_promedio)
calcular_btn.enabled = False

app.display()