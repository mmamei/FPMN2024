from guizero import App, Slider, PushButton, Text, CheckBox, Box

def toggle_buzzer():
    if buzzer_button.text == "on":
        buzzer_button.text = "off"
    elif buzzer_button.text == "off":
        buzzer_button.text = "beep"
    else:
        buzzer_button.text = "on"

# Creazione della finestra principale
app = App("Traffic HAT controller", layout="grid")

# Sezione luci
Text(app, text="Lights", grid=[0, 0], align="left")

Text(app, text="Red", grid=[0, 1], align="left")
red_slider = Slider(app, start=0, end=3, grid=[1, 1], horizontal=False)

Text(app, text="Amber", grid=[2, 1], align="left")
amber_slider = Slider(app, start=0, end=3, grid=[3, 1], horizontal=False)

Text(app, text="Green", grid=[4, 1], align="left")
green_slider = Slider(app, start=0, end=3, grid=[5, 1], horizontal=False)

# Sezione buzzer
Text(app, text="Buzzer", grid=[0, 2], align="left")
buzzer_button = PushButton(app, command=toggle_buzzer, text="on", grid=[1, 2])

# Sezione pulsante
Text(app, text="Button", grid=[0, 3], align="left")
pushed_checkbox = CheckBox(app, text="Pushed", grid=[1, 3])
held_checkbox = CheckBox(app, text="Held", grid=[2, 3])

# Esecuzione dell'applicazione
app.display()
