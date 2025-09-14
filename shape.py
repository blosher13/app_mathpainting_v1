import numpy as np

class Canvas:
    def __init__(self, bg_height, bg_width, bg_color):
        self.bg_height = bg_height
        self.bg_width = bg_width
        self.bg_color = bg_color
    
        self.bg_nparray = np.zeros((self.bg_height, self.bg_width, 3), dtype=np.uint8)

        if self.bg_color == 'white':
            self.bg_nparray[:] = [255, 255, 255]
        elif self.bg_color == 'black':
            self.bg_nparray[:] = [0, 0, 0]
        else:
            print('invalid background color')

        
class Shape:
    def __init__(self, x_coord, y_coord, s_height, s_width, r_color, g_color, b_color):
        self.x_cord = x_coord
        self.y_cord = y_coord
        self.s_height = s_height
        self.s_width = s_width
        self.r_color = r_color
        self.g_color = g_color
        self.b_color = b_color
    
    def paint_shape(self, background_image):
        new_height = self.x_cord + self.s_height
        new_width = self.y_cord + self.s_width
        new_shape = background_image.bg_nparray[self.x_cord: new_height, self.y_cord: new_width] = [self.r_color, self.g_color, self.b_color]
        return new_shape