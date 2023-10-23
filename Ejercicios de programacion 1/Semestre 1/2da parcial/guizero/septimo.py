from guizero import App, Text, TextBox, PushButton

def generar_cuadrado():
    message.value = str(int(name.value)**2)

app= App(title="ICI App")

message = Text(app, text="Dame un número")
name = TextBox(app, width=20)
button= PushButton(app, text="Calcular el cuadrado", command=generar_cuadrado)
message_cuadrado= Text(app, text="")
app.display()