from src.light import Light
from src.vector import Vector


class Scene:
    def __init__(self, ambient_color: Vector, lights: list[Light]):
        self.ambient_color = ambient_color
        self.lights = lights
