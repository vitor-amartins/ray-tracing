from src.camera import Camera
from src.plane import Plane
from src.point import Point
from src.scene import Scene
from src.sphere import Sphere
from src.triangle import Triangle
from src.utils import save_ppm
from src.vector import Vector

RED = Vector(1, 0, 0)
GREEN = Vector(0, 1, 0)
BLUE = Vector(0, 0, 1)
WHITE = Vector(1, 1, 1)
BLACK = Vector(0, 0, 0)

if __name__ == '__main__':
    sphere1 = Sphere(
        center=Point(0, 0, 8),
        radius=2,
        color=RED,
    )
    # sphere2 = Sphere(
    #     center=Point(3, 3, 3),
    #     radius=1,
    #     color=BLUE,
    # )
    triangle = Triangle(
        p0=Point(0, 0, 3),
        p1=Point(1, 1, 3),
        p2=Point(1, 0, 3),
        color=BLUE,
    )
    plane = Plane(
        point=Point(0, 0, 10),
        normal=Vector(0, 0, 1),
        color=GREEN,
    )

    shapes = [sphere1, plane, triangle]

    scene = Scene(
        ambient_color=WHITE,
        lights=[],
    )

    camera = Camera(
        c=Point(0, 0, 0),
        m=Point(0, 0, 1),
        vup=Vector(0, 1, 0),
        distance_to_screen=1,
        screen_height=200,
        screen_width=200,
    )

    pixel_positions = camera.calculate_pixel_position()
    pixel_colors = []
    for row in pixel_positions:
        pixel_row = []
        for pixel in row:
            ray_origin = camera.c
            ray_direction = pixel.difference(ray_origin).normalize()

            min_t: float | None = None
            pixel_color = scene.ambient_color

            if pixel == Point(0, 0, 1):
                print('debug')

            for shape in shapes:
                intersect, t = shape.intersect(ray_origin, ray_direction)
                if intersect and (min_t is None or t < min_t):
                    pixel_color = shape.color
                    min_t = t

            pixel_row.append(pixel_color)

        pixel_colors.append(pixel_row)

    save_ppm(pixel_colors, 'outputs/009.ppm')
