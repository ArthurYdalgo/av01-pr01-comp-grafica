from canvas import Canvas
import tkinter

canvas = Canvas(400,400)
new_shape_window = None
shape_select=None
selected_shape = None
main = tkinter.Tk()

def draw():
    canvas.draw()
    main.after(300, draw)
main.after(300, draw)
main.geometry("300x300")
add_shape_dialog = tkinter.Frame()

def addNewShape(type=None, center=None, thickness=None, scale=None, vertices = None):    

    shape = canvas.addShape('hexagon')
    Lb.insert(0,'{}, {}'.format(shape.uuid,shape.type))
 
def confirmShapeSelection():
    
    new_shape_window.destroy()
    pass

def selectNewShape():
    global new_shape_window
    new_shape_window = tkinter.Toplevel(main)
    
    new_shape_window.title("Adicionar forma")
    new_shape_window.geometry("300x100")
    options = ['Triangulo','Hexagono','Quadrado','Poligono irregular']
    global selected_shape
    selected_shape = tkinter.StringVar()
    selected_shape.set(options[3])
    global shape_select
    shape_select = tkinter.OptionMenu(new_shape_window,selected_shape, *options)
    
    confirm_button = tkinter.Button(new_shape_window,text="Confirmar",command=confirmShapeSelection)
    
    shape_select.pack()
    confirm_button.pack()

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
