from cv2 import SimpleBlobDetector
from canvas import Canvas
import tkinter

canvas = Canvas(800,800)
new_shape_window = None
new_shape_options_window = None
shape_select=None
selected_shape = None
main = tkinter.Tk()
x = None
y = None
size = None
options = ['Triangulo','Hexagono','Quadrado','Poligono irregular']

def draw():
    canvas.draw()
    main.after(300, draw)
main.after(300, draw)
main.geometry("300x300")
add_shape_dialog = tkinter.Frame()

def addNewShape(x,y,size):    
    types = {'Triangulo':'triangle','Hexagono':'hexagon','Quadrado':'square','Poligono irregular':'irregular'}
    global selected_shape
    if(selected_shape in types):

        shape = canvas.addShape(types[selected_shape])
        canvas.translateShape(shape.uuid,x,y)
        canvas.scaleShape(shape.uuid,size)
        Lb.insert(0,'{}, {}'.format(shape.uuid,shape.type))
 
def confirmShapeSelection():
    global selected_shape
    print(selected_shape)
    new_shape_window.destroy()
    newShapeOptions()
    

    pass

def cancelShapeSelection():
    global selected_shape
    selected_shape = None
    global new_shape_window
    new_shape_window.destroy()

def confirmShapeOptionsSelection():
    x_value = int(x.get())
    y_value = int(y.get())
    size_value = int(size.get())
    addNewShape(x_value,y_value,size_value)
    global selected_shape
    selected_shape = None
    global new_shape_options_window
    new_shape_options_window.destroy()    

    pass

def cancelShapeOptionsSelection():
    global selected_shape
    selected_shape = None
    global new_shape_options_window
    new_shape_options_window.destroy()
    pass

def validateNumberEntry(value):    
    if value == '' or value == '-':
        return True
    if value:
        try:
            float(value)
            return True
        except ValueError:
            return False
    else:
        return False




def newShapeOptions():
    global new_shape_options_window
    new_shape_options_window = tkinter.Toplevel(main)
    reg = (new_shape_options_window.register(validateNumberEntry),'%P')
    new_shape_options_window.title("Opções da nova forma")
    new_shape_options_window.geometry("300x300")
    global selected_shape

    tkinter.Label(new_shape_options_window, 
         text="X: ").grid(row=0)
    tkinter.Label(new_shape_options_window, 
            text="Y: ").grid(row=1)
    global x,y,size
    x = tkinter.Entry(new_shape_options_window,  validate = 'key', validatecommand=reg)
    y = tkinter.Entry(new_shape_options_window, validate = 'key', validatecommand=reg)
    
    x.grid(row=0, column=1)
    y.grid(row=1, column=1)

    tkinter.Label(new_shape_options_window, 
         text="Tamanho: ").grid(row=2)
    size = tkinter.Entry(new_shape_options_window, validate = 'key', validatecommand=reg)
    size.grid(row=2,column=1)
    if(selected_shape == 'Triangulo'):
        pass
    if(selected_shape == 'Quadrado'):
        pass
    if(selected_shape == 'Hexagono'):
        pass
    if(selected_shape == 'Poligono irregular'):
        pass

    confirm_button = tkinter.Button(new_shape_options_window,text="Confirmar",command=confirmShapeOptionsSelection)
    confirm_button.grid(row=3,column=0)
    cancel_button = tkinter.Button(new_shape_options_window,text="Cancelar",command=cancelShapeOptionsSelection)
    cancel_button.grid(row=3,column=1)

def updateSelectedShape(selection):
    global selected_shape
    selected_shape = selection
    pass

def selectNewShape():
    global new_shape_window
    global selected_shape
    if(not(selected_shape is None)):
        return
    new_shape_window = tkinter.Toplevel(main)
    
    new_shape_window.title("Adicionar forma")
    new_shape_window.geometry("300x100")
    
    
    selected_shape = tkinter.StringVar()
    selected_shape.set(options[0])
    global shape_select
    shape_select = tkinter.OptionMenu(new_shape_window,selected_shape, *options,command=updateSelectedShape)
    selected_shape = options[0]
    confirm_button = tkinter.Button(new_shape_window,text="Confirmar",command=confirmShapeSelection)
    
    shape_select.pack()
    confirm_button.pack()
    cancel_button = tkinter.Button(new_shape_window,text="Cancelar",command=cancelShapeSelection)
    cancel_button.pack()
    pass 

def removeShape():
     
    selected_index = Lb.curselection()

    if selected_index:        
        selected = Lb.get(selected_index)
        selected = selected.split(',')[0]
        canvas.removeShape(selected)
        Lb.delete(selected_index)

        print(selected)
    pass

def editShape():
     
    selected = Lb.get(Lb.curselection())
    selected = selected.split(',')[0]
    

    pass
    
add_shape_button = tkinter.Button(main,text="Adicionar Forma",command=selectNewShape)
edit_shape_button = tkinter.Button(main,text="Editar Forma",command=editShape)
delete_shape_button = tkinter.Button(main,text="Deletar Forma",command=removeShape)

Lb = tkinter.Listbox(main)
add_shape_button.pack()
# Lb.insert(0,'2324, Quadrado')
# Lb.insert(1,'2532, Triangulo')
# Lb.insert(2,'2224, Quadrado')
# Lb.insert(3,'4353, Triangulo')
Lb.pack()
edit_shape_button.pack()
delete_shape_button.pack()
main.mainloop()


# canvas.addShape('hexagon')
# canvas.draw()

# shape = canvas.addShape('triangle')
# canvas.rotateShape(shape.uuid,30)
# canvas.scaleShape(shape.uuid, 2)
# canvas.addShape('triangle')
# canvas.draw()
