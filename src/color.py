class Color: 
    def __init__(self, red: float, green: float, blue:float):
        self.red = red
        self.green = green
        self.blue = blue

    def truncate(self):
        if self.red < 0:
            self.red = 0
        elif self.red > 255:
            self.red = 255

        if self.green < 0:
            self.green = 0
        elif self.green > 255:
            self.green = 255

        if self.blue < 0:
            self.blue = 0
        elif self.blue > 255:
            self.blue = 255

    def multiply_color(self,color):
        self.red = self.red * color.red
        self.green = self.green * color.green
        self.blue = self.blue * color.blue
        self.truncate()

    def sum_color(self, color):
        self.red = self.red + color.red
        self.green = self.green + color.green
        self.blue = self.blue + color.blue
        self.truncate()

    def multiply_value(self, value):
        self.red = self.red * value
        self.green = self.green * value
        self.blue = self.blue * value
        self.truncate()

    