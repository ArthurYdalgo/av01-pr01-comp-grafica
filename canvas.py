import cv2
import uuid
import numpy as np


class Shape():
    def __init__(self, type):
        self.uuid = uuid.uuid4()
        self.angle = 0
        self.position = (0, 0)
        self.scale = 1
        self.type = type

    def setShapeCenterPosition(self, posistion):
        pass

    def setShapeVertices(self, vertices):
        pass

    def setShapeBorderThickness(self, thickness):
        pass

    def mirrorShape(self, axis='vertical'):
        pass

    def translate(self, x_axis, y_axis):
        pass

    def specificShapeScale(self, horizontal_percentage, vertical_percentage):
        pass

    def scaleShape(self, percentage):
        self.specificScale(percentage, percentage)
        pass

    def rotateShape(self, degrees):

        pass

    def shearShape(self, percentage):
        pass


class Canvas():
    def __init__(self, width=200, height=200):
        self.shapes = {}
        self.state = None
        print("Iniciando")
        self.width, self.height = self._validateDimensions(width, height)
        

        pass

    def _validateDimensions(self, width, height):
        if(height <= 0):
            height = 200
        if(width <= 0):
            width = 200

        return width, height

    def _renderShape(self, uuid, canvas):
        shape = self.shapes[uuid]

        if(shape.type == 'square'):
            # cv2.rectangle(canvas, )
            pass
        elif(shape.type == 'triangle'):
            pt1 = (150, 100)
            pt2 = (100, 200)
            pt3 = (200, 200)
            triangle_cnt = np.array( [pt1, pt2, pt3] )

            canvas = cv2.drawContours(canvas, [triangle_cnt], 0, (0,255,0), -1)
            
            pass
        elif(shape.type == 'hexagon'):
            pass
        elif(shape.type == 'irregular'):
            pass
            
        return canvas

    def getShapes(self):
        return self.shapes

    def clear(self):
        self.shapes = {}
    


    def addShape(self, type, vertices = None):
        shape = Shape(type)

        self.shapes[shape.uuid] = shape

    def removeShape(self, uuid):
        pass

    def shapeOptions(self, uuid):
        pass

    def draw(self):

        blank_image = np.zeros((self.height,self.width,3), np.uint8)
        blank_image.fill(255)

        canvas = blank_image

        for shape in self.shapes:
            canvas = self._renderShape(shape, canvas)

        cv2.namedWindow("Window")

        cv2.imshow("Window", canvas)
        key = cv2.waitKey(0)
        return key
        pass
