from abc import abstractmethod

from src.point import Point
from src.vector import Vector
from src.color import Color


class Shape:
    def __init__(
            self,
            color: Color,
            kd: float = 0.5,
            ks: float = 0.5,
            ka: float = 0.5,
            kr: float = 0.5,
            kt: float = 0.5,
            n: float = 3,
    ):
        self.color = color
        self.kd = kd  # Coeficiente difuso
        self.ks = ks  # Coeficiente especular
        self.ka = ka  # Coeficiente ambiental
        self.kr = kr  # Coeficiente de reflexão
        self.kt = kt  # Coeficiente de transmissão
        self.n = n    # Coeficiente de rugosidade

    @abstractmethod
    def intersect(self, ray_origin: Point, ray_direction: Vector) -> tuple[bool, float]:
        pass

    @abstractmethod
    def get_normal(self, interception_point: Point) -> Vector:
        pass
