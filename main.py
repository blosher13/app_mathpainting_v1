from shape import Shape, Canvas
from img import Photo
    
print('Welcome to Math Paint! \nLets start by creating a background image')    
bg_width = int(input('Enter canvas width: '))
bg_height = int(input('Enter canvas height: '))
bg_color = input('Enter canvas color (black or white): ').strip().lower()

canvas = Canvas(bg_height, bg_width, bg_color)
while True:
    shape = input('What would you like to draw?\nEnter quit to quit. ')
    if shape == 'quit': 
        break
    x_coord = int(input(f'Enter x of the {shape}: '))
    y_coord = int(input(f'Enter y of the {shape}: '))
    s_width = int(input(f'Enter the width of the {shape}: '))
    s_height = int(input(f'Enter the height of the {shape}: '))
    s_red = input(f'How much red: ')
    s_green = input(f'How much green: ')
    s_blue = input(f'How much blue: ')

    new_shape = Shape(x_coord, y_coord, s_height, s_width, s_red, s_green, s_blue).paint_shape(canvas)

img = Photo(canvas.bg_nparray)
img.generate_image('test1.png')

