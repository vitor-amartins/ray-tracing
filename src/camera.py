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
                u = ((2 * x) / self.screen_width) - 1
                v = 1 - ((2 * y) / self.screen_height)

                pixel_position = self.target_point.translate(self.u.scale(u)).translate(self.v.scale(v))

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
