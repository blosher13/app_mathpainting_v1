import numpy as np
from PIL import Image

class Canvas:
    def __init__(self, bg_color, bg_height, bg_width):
        self.bg_color = bg_color
        self.bg_height = bg_height
        self.bg_width = bg_width

    def generate_canvas(self):
        background_image = np.zeros((self.bg_height, self.bg_width, 3), dtype=np.uint8)
        if self.bg_color == 'white':
            background_image[:] = [255, 255, 255]
        elif self.bg_color == 'black':
            background_image[:] = [0, 0, 0]
        else:
            print('invalid background color')
        return background_image
        
class Shape:
    def __init__(self, x_coord, y_coord, r_color, g_color, b_color):
        self.x_cord = x_coord
        self.y_cord = y_coord
        self.r_color = r_color
        self.g_color = g_color
        self.b_color = b_color
    
    def paint_shape(self, background_image):
        background_image[self.x_cord:self.y_cord] = [self.r_color, self.g_color, self.b_color]
        shape = Image.fromarray(background_image, 'RGB')
        return background_image
    
class Photo:
    def __init__(self, image_array):
        self.image_array = image_array

    def generate_image(self):
        image = Image.fromarray(self.image_array, 'RGB')
        return image

