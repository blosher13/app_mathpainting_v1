from PIL import Image

class Photo:
    def __init__(self, image_array):
        self.image_array = image_array

    def generate_image(self, filename):
        image = Image.fromarray(self.image_array, 'RGB')
        return image.save(filename)