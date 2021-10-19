import cv2
import uuid
import numpy as np
import hashlib
from numpy.lib.function_base import blackman


class Shape():
    def __init__(self, type):
        # self.uuid = uuid.uuid4()
        self.uuid = int(hashlib.sha1((str(uuid.uuid4())).encode("utf-8")).hexdigest(), 16) % (10 ** 4)
        self.angle = 0
        self.border = 3
        self.position = (200, 200)
        self.scale = 1
        self.type = type
        self.points = []
        self.image = None

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

    def scaleShape(self, scale):
        self.scale = scale
        pass

    def setAngle(self, angle, overwrite = False):
        if(angle > 360):
            angle = angle % 360
        elif(angle < 0):
            angle = angle % -360
            angle += 360
                
        if(overwrite):
            self.angle = angle
        else:
            self.angle += angle

        if(self.angle > 360):
            self.angle = self.angle % 360

        pass


    def rotateShape(self, degrees):
        self.setAngle(degrees)
        pass

    def rotate_image(self, mat, angle):
        """
        Rotates an image (angle in degrees) and expands image to avoid cropping
        """

        height, width = mat.shape[:2] # image shape has 3 dimensions
        image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

        rotation_mat = cv2.getRotationMatrix2D(image_center, angle, self.scale)

        # rotation calculates the cos and sin, taking absolutes of those.
        abs_cos = abs(rotation_mat[0,0]) 
        abs_sin = abs(rotation_mat[0,1])

        # find the new width and height bounds
        bound_w = int(height * abs_sin + width * abs_cos)
        bound_h = int(height * abs_cos + width * abs_sin)

        # subtract old image center (bringing image back to origo) and adding the new image center coordinates
        rotation_mat[0, 2] += bound_w/2 - image_center[0]
        rotation_mat[1, 2] += bound_h/2 - image_center[1]

        # rotate image with the new bounds and translated rotation matrix
        rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
        self.image = rotated_mat
        return rotated_mat
    def rotateRender(self):
        if(not(self.image is None)):
            height, width = self.image.shape[:2] # image shape has 3 dimensions
            image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

            rotation_mat = cv2.getRotationMatrix2D(image_center, self.angle, 1.)

            # rotation calculates the cos and sin, taking absolutes of those.
            abs_cos = abs(rotation_mat[0,0]) 
            abs_sin = abs(rotation_mat[0,1])

            # find the new width and height bounds
            bound_w = int(height * abs_sin + width * abs_cos)
            bound_h = int(height * abs_cos + width * abs_sin)

            # subtract old image center (bringing image back to origo) and adding the new image center coordinates
            rotation_mat[0, 2] += bound_w/2 - image_center[0]
            rotation_mat[1, 2] += bound_h/2 - image_center[1]

            # rotate image with the new bounds and translated rotation matrix
            rotated_mat = cv2.warpAffine(self.image, rotation_mat, (bound_w, bound_h))
            return rotated_mat
    

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

    def _renderShape(self, uuid):
        shape = self.shapes[uuid]
        default_size = 100
        blank_image = self.blankImage((default_size + int(shape.border * 2) ,default_size + int(shape.border * 2)))
        if(shape.type == 'square'):
            pt1 = (0+shape.border, 0+shape.border)
            pt2 = (0+shape.border, 100+shape.border)
            pt3 = (100+shape.border, 100+shape.border)
            pt4 = (100+shape.border, 0+shape.border)
            square_cnt = np.array( [pt1, pt2, pt3, pt4] )

            draw_base_shape = cv2.drawContours(blank_image, [square_cnt], 0, (0,255,0,255), 3)            

            pass
        elif(shape.type == 'triangle'):
           
            pt1 = (0+shape.border, 0+shape.border)
            pt2 = (100+shape.border, 0+shape.border)
            pt3 = (50+shape.border,100+shape.border)
            triangle_cnt = np.array( [pt2, pt1, pt3] )

            draw_base_shape = cv2.drawContours(blank_image, [triangle_cnt], 0, (0,255,0,255), 3)
            
            pass
        elif(shape.type == 'hexagon'):
            pt1 = (0+shape.border, 25+shape.border)
            pt2 = (0+shape.border, 75+shape.border)
            pt4 = (50+shape.border, 100+shape.border)
            pt6 = (100+shape.border,75+shape.border)
            pt5 = (100+shape.border, 25+shape.border)
            pt3 = (50+shape.border, 0+shape.border)

            hexagon_cnt = np.array([pt1,pt2,pt4,pt6,pt5,pt3])
            draw_base_shape = cv2.drawContours(blank_image, [hexagon_cnt], 0, (0,255,0,255), 3)
            pass
        elif(shape.type == 'irregular'):
            polygon_cnt = np.array(shape.points)
            draw_base_shape = cv2.drawContours(blank_image, [polygon_cnt], 0, (0,255,0,255), 2)
            pass

        shape.image = draw_base_shape
        # shape.rotateRender()
        shape.rotate_image(shape.image,shape.angle)

        
        
        
        
        return shape.image

    def getShapes(self):
        return self.shapes

    def clear(self):
        self.shapes = {}
    
    def blankImage(self, dimensions = None, white = False):
        if(dimensions):
            width , height = dimensions
        else:
            width , height = self.width, self.height 
        blank_image = np.zeros((height,width,4), np.uint8)
        if(white):
            blank_image[:] = [255,255,255,255]
        else:
            blank_image[:] = [0,0,0,0]
        return blank_image

    def addShape(self, type, vertices = None):
        shape = Shape(type)

        self.shapes[shape.uuid] = shape

        return shape

    def removeShape(self, uuid):
        del self.shapes[int(uuid)]
        pass

    def shapeOptions(self, uuid):
        pass

    def rotateShape(self, uuid, degrees):
        if(uuid in self.shapes):
            shape = self.shapes[uuid]
            shape.rotateShape(degrees)
    def scaleShape(self, uuid, ratio):
        if(uuid in self.shapes and ratio and ratio > 0):
            shape = self.shapes[uuid]
            shape.scaleShape(ratio)

    def drawShapeOnCanvas(self,shape_uuid,background):
        #get position and crop pasting area if needed
        shape = self.shapes[shape_uuid]
        foreground = shape.image
        x = shape.position[0] - int(shape.image.shape[0]/2)
        y = shape.position[1] - int(shape.image.shape[1]/2)
        bgWidth = background.shape[0]
        bgHeight = background.shape[1]
        frWidth = foreground.shape[0]
        frHeight = foreground.shape[1]
        width = bgWidth-x
        height = bgHeight-y
        if frWidth<width:
            width = frWidth
        if frHeight<height:
            height = frHeight
        # normalize alpha channels from 0-255 to 0-1
        alpha_background = background[x:x+width,y:y+height,3] / 255.0
        alpha_foreground = foreground[:width,:height,3] / 255.0
        # set adjusted colors
        for color in range(0, 3):
            fr = alpha_foreground * foreground[:width,:height,color]
            bg = alpha_background * background[x:x+width,y:y+height,color] * (1 - alpha_foreground)
            background[x:x+width,y:y+height,color] = fr+bg
        # set adjusted alpha and denormalize back to 0-255
        background[x:x+width,y:y+height,3] = (1 - (1 - alpha_foreground) * (1 - alpha_background)) * 255
        return background
    

    def draw(self):

        blank_image = self.blankImage(white=True)

        canvas = blank_image



        for shape_uuid in self.shapes:            
            self._renderShape(shape_uuid)
            canvas = self.drawShapeOnCanvas(shape_uuid, canvas)
            
        canvas = cv2.rotate(canvas,cv2.ROTATE_180)
        cv2.imshow("Window", canvas)
        key = cv2.waitKey(1)
        return key
        pass
