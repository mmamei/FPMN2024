from guizero import App, Picture, PushButton

def avanti():
    index = int(p.image[-5])
    index = (index + 1) % 4
    print(f'img/{index}.png')
    p.image = f'img/{index}.png'

def indietro():
    index = int(p.image[-5])
    index = (index - 1) % 4
    print(f'img/{index}.png')
    p.image = f'img/{index}.png'

def slideshow():
    if b.text == 'stop':
        avanti()
        p.after(1000,slideshow)

def start_slideshow():
    b.text = 'stop' if b.text == 'slideshow' else 'slideshow'
    slideshow()

app = App('picture', layout='grid')
p = Picture(app,image='img/0.png',grid=(0,0,3,1),width=2000, height=800)
PushButton(app,text='avanti',grid=(0,1),command=avanti)
PushButton(app,text='indietro',grid=(1,1),command=indietro)
b=PushButton(app,text='slideshow',grid=(2,1),command = start_slideshow)
app.display()