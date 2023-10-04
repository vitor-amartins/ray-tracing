from src.color import Color
from src.light import Light


class Scene:
    def __init__(self, ambient_color: Color, lights: list[Light]):
        self.ambient_color = ambient_color
        self.lights = lights
