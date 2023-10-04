class Color: 
    def __init__(self, red: float = 0.0, green: float = 0.0, blue: float = 0.0):
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

    def multiply_color(self, color):
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

    def scale(self, scalar: float) -> 'Color':
        return Color(self.red * scalar, self.green * scalar, self.blue * scalar)

    def __str__(self):
        return f"Color({self.red}, {self.green}, {self.blue})"
