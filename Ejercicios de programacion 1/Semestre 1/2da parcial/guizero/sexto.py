from guizero import App, Text, TextBox

app = App(title="ICI App")

message =  Text(app,text="Dame tu nombre")
name = TextBox(app, width=20)

app.display()
