import math

from src.point import Point
from src.vector import Vector


class Camera:
    def __init__(
            self,
            c: Point,
            m: Point,
            vup: Vector,
            distance_to_screen: float,
            screen_height: int,
            screen_width: int,
    ):
        self.c = c  # Camera position
        self.m = m  # Camera target
        self.vup = vup
        self.distance_to_screen = distance_to_screen
        self.screen_height = screen_height
        self.screen_width = screen_width
        # Base vectors
        self.w, self.u, self.v = self.calculate_base()
        # Center of the screen
        self.target_point = self.calculate_target_point()
        # FOV
        self.horizontal_fov = 2 * math.atan((self.screen_width / 2) / self.distance_to_screen)
        self.vertical_fov = 2 * math.atan((self.screen_height / 2) / self.distance_to_screen)
        self.pixel_size_x = self.screen_width / (2 * math.tan(self.horizontal_fov / 2))
        self.pixel_size_y = self.screen_height / (2 * math.tan(self.vertical_fov / 2))

    def calculate_base(self) -> tuple[Vector, Vector, Vector]:
        w = self.m.difference(self.c).normalize()
        u = w.cross(self.vup).normalize()
        v = u.cross(w)
        print('w:', w, '\nu:', u, '\nv:', v)
        return w, u, v

    def calculate_target_point(self) -> Point:
        return self.c.translate(self.w.scale(self.distance_to_screen))

    def calculate_pixel_position(self) -> list[list[Point]]:
        pixel_positions = []
        for y in range(self.screen_height):
            row = []
            for x in range(self.screen_width):
                screen_x = (x + 0.5) / self.screen_width * 2 - 1
                screen_y = (y + 0.5) / self.screen_height * 2 - 1
                u_factor = self.u.scale(screen_x * self.pixel_size_x)
                v_factor = self.v.scale(-screen_y * self.pixel_size_y)
                pixel_position = self.target_point.translate(u_factor).translate(v_factor)

                row.append(pixel_position)
            pixel_positions.append(row)
        return pixel_positions


if __name__ == '__main__':
    camera = Camera(
        c=Point(0, 0, 0),
        m=Point(0, 1, 0),
        vup=Vector(0, 0, 1),
        distance_to_screen=1,
        screen_height=10,
        screen_width=10,
    )
