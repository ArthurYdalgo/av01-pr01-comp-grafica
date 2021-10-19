from canvas import Canvas

canvas = Canvas(400,400)

# canvas.addShape('hexagon')
# canvas.draw()

shape = canvas.addShape('square')
canvas.rotateShape(shape.uuid,30)
canvas.scaleShape(shape.uuid, 2)
canvas.addShape('triangle')
canvas.draw()
