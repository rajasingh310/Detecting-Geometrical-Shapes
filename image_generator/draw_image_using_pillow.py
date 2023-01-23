from random import randint
from PIL import Image, ImageDraw


def color():
    return randint(0, 250), randint(0, 250), randint(0, 250)


def positions(resolution_image):
    x = randint(0, resolution_image[0])
    y = randint(0, resolution_image[1])
    return x, y


class DrawGeometricalShapes:

    def __init__(self, resolution_image=(500, 500), background_color=(255, 255, 255)):
        # Create a new image with a black background
        self.resolution_image = resolution_image
        self.background_color = background_color
        self.image = Image.new('RGB', self.resolution_image, self.background_color)
        self.draw = ImageDraw.Draw(self.image)

    def conics(self):
        self.r = randint(5, int(self.resolution_image[0] / 2)) - 1  # Smallest radius value  5
        self.x = randint(self.r, self.resolution_image[0] - self.r)
        self.y = randint(self.r, self.resolution_image[1] - self.r)

        self.coordinate = [self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r]

        self.draw.ellipse(self.coordinate,
                          outline=color(),
                          width=2)

    def quadrilateral(self):
        x_0, y_0 = positions(self.resolution_image)
        x_1, y_1 = positions(self.resolution_image)
        self.coordinate = (x_0, y_0, x_1, y_1)

        self.draw.rectangle(self.coordinate,
                            outline=color(),
                            width=2)

    def line(self):
        x_0, y_0 = positions(self.resolution_image)
        x_1, y_1 = positions(self.resolution_image)
        self.coordinate = [x_0, y_0, x_1, y_1]

        self.draw.line(self.coordinate,
                       fill=color(), width=2)

    def polygon(self):
        x_0, y_0 = positions(self.resolution_image)
        x_1, y_1 = positions(self.resolution_image)
        x_2, y_2 = positions(self.resolution_image)
        self.coordinate = [x_0, y_0, x_1, y_1, x_2, y_2]

        self.draw.polygon(self.coordinate,
                          outline=color(),
                          width=2)