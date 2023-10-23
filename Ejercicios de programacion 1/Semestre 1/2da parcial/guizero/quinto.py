from guizero import App, Text, PushButton

def change_message():
    message.value ="Arriba el América!!! prrros!!!"
app = App(title="ICI App")

message =  Text(app,text="Welcome to ICI World")

button = PushButton(app,text="Click here", command=change_message)
app.display() 