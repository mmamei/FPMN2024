from guizero import App, Text, PushButton,Slider, CheckBox

def pushed(t):
    t1.value = t

def slider():
    r = str(slider_red.value)
    r = r if len(r) == 2 else '0'+r
    g = str(slider_green.value)
    g = g if len(g) == 2 else '0'+g
    b = str(slider_blue.value)
    b = b if len(b) == 2 else '0'+b
    app.bg = f'#{r}{g}{b}'

app = App(title="Traffic", layout='grid')
t1 = Text(app, text="Lights", grid=(1,1))
Text(app, text="Red", grid=(2,1))
Text(app, text="Green", grid=(3,1))
Text(app, text="Blue", grid=(4,1))

slider_red, slider_blue,slider_green = None,None,None

slider_red = Slider(app, horizontal=False, grid=(2,2), height=150, start=99, end=0, command=slider)
slider_green = Slider(app, horizontal=False, grid=(3,2), height=150, start=99, end=0, command=slider)
slider_blue = Slider(app, horizontal=False, grid=(4,2), height=150, start=99, end=0, command=slider)

slider_red.value = 99
slider_green.value = 99
slider_blue.value = 99

Text(app, text="Buzzer", grid=(1,3))
PushButton(app, grid=(2,3), text='On', command=pushed, args=['On']) 
PushButton(app, grid=(3,3), text = 'Off', command=pushed, args=['Off']) 
PushButton(app, grid=(4,3), text='Beep', command=pushed, args=['Beep'])

Text(app, text="Buzzer", grid=(1,4))
CheckBox(app,text='Pushed',grid=(2,4))
CheckBox(app,text='Held',grid=(3,4))

app.display()