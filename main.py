from canvas import Canvas

def menu(options):
    print("")
    print("==== MENU ===")
    for option in options:
        print("{} - {}".format(option, options[option]))
    print("")
    return input("Escolha: ")

canvas = Canvas(400,400)

while(True):
    key = canvas.draw()
    if(key == 32):
        menu_choice = None
        menu_options = {1: 'Desenhar forma', 2: 'Manipular forma', 3: 'Apagar forma', 4: 'Limpar'}
        while(not(menu_choice in menu_options)):
            menu_choice = menu(menu_options)
        if(menu_choice == 1):
            shape_choice = None
            shape_types = {1: 'triangle', 2: 'square', 3: 'hexagon'}
            shape_options = {1: 'Triângulo', 2: 'Quadrado', 3: 'Hexágono'}
            while(not(menu_choice in menu_options)):
                shape_choice = menu(shape_options)
            
            canvas.addShape(shape_types[shape_choice])
            pass        
        elif(menu_choice == 2):
            pass
        elif(menu_choice == 3):
            pass
        elif(menu_choice == 4):
            pass
        
        pass
    
