from guizero import App, Text, TextBox, PushButton

import pyttsx3

engine = pyttsx3.init()



def mensaje_cuadrado():
    resultado  = str(int(name.value)**2)
    cadena = f"El cuadrado de {name.value} es {resultado}"
    engine.say(cadena)
    engine.runAndWait()
   

app= App(title="ICI App")

message = Text(app, text="Dame un número")
name = TextBox(app, width=20)
button= PushButton(app, text="Calcular el cuadrado", command= mensaje_cuadrado)
message_cuadrado= Text(app, text="")
app.display()