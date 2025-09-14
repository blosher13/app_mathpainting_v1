import numpy as np
from PIL import Image
from unittest import mock

# bg_width = 100
# bg_height = 100
# bg_color = 'white'

# x_coord = 25
# y_coord = 25
# s_width = 75
# s_height = 75
# s_red = 200
# s_green = 0
# s_blue = 0

class Canvas:
    def __init__(self, bg_height, bg_width, bg_color):
        self.bg_height = bg_height
        self.bg_width = bg_width
        self.bg_color = bg_color

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
    def __init__(self, x_coord, y_coord, s_height, s_width, r_color, g_color, b_color):
        self.x_cord = x_coord
        self.y_cord = y_coord
        self.s_height = s_height
        self.s_width = s_width
        self.r_color = r_color
        self.g_color = g_color
        self.b_color = b_color
    
    def paint_shape(self, background_image):

        background_image[self.x_cord:self.s_height, self.y_cord:self.s_width] = [self.r_color, self.g_color, self.b_color]
        print(self.x_cord, self.y_cord, self.r_color, self.g_color, self.b_color)
        # print(background_image)
        return background_image
    
class Photo:
    def __init__(self, image_array):
        self.image_array = image_array

    def generate_image(self, filename):
        image = Image.fromarray(self.image_array, 'RGB')
        return image.save(filename)
    
print('Welcome to Math Paint! \nLets start by creating a background image')    
bg_width = int(input('Enter canvas width: '))
bg_height = int(input('Enter canvas height: '))
bg_color = input('Enter canvas color (black or white): ').strip().lower()

canvas = Canvas(bg_height, bg_width, bg_color).generate_canvas()
while True:
    shape_list = []
    shape = input('What would you like to draw? Enter quit to quit. ')
    if shape == 'quit': 
        break
    x_coord = int(input(f'Enter x of the {shape}: '))
    y_coord = int(input(f'Enter y of the {shape}: '))
    s_width = int(input(f'Enter the width of the {shape}'))
    s_height = int(input(f'Enter the height of the {shape}'))
    s_red = input(f'How much red: ')
    s_green = input(f'How much green: ')
    s_blue = input(f'How much blue: ')

    shape = Shape(x_coord, y_coord, s_height, s_width, s_red, s_green, s_blue).paint_shape(canvas)
    canvas = Shape(x_coord, y_coord, s_height, s_width, s_red, s_green, s_blue).paint_shape(canvas)
    # shape_list.append(shape)
    photo = Photo(shape).generate_image('test1.png')


