from src.camera import Camera
from src.plane import Plane
from src.point import Point
from src.scene import Scene
from src.shape import Shape
from src.sphere import Sphere
from src.triangle import Triangle
from src.utils import save_ppm
from src.vector import Vector
from src.color import Color
from src.light import Light

RED = Color(1, 0, 0)
GREEN = Color(0, 1, 0)
BLUE = Color(0, 0, 1)
WHITE = Color(1, 1, 1)
BLACK = Color(0, 0, 0)

if __name__ == '__main__':
    sphere1 = Sphere(
        center=Point(0, 0, 8),
        radius=2,
        color=RED,
    )
    sphere2 = Sphere(
        center=Point(0, 0, 6),
        radius=1,
        color=BLUE,
    )
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
        n=1.8,
    )

    shapes: list[Shape] = [
        sphere1,
        sphere2,
        plane,
    ]
    light_1 = Light(
        position=Point(0, 10, 0),
        color=Color(1, 1, 1),
    )
    # light_2 = Light(
    #     position=Point(20, 0, 3),
    #     color=Color(1, 1, 1),
    # )

    scene = Scene(
        ambient_color=BLACK,
        lights=[
            light_1,
            # light_2,
        ],
    )

    camera = Camera(
        c=Point(0, 0, 0),
        m=Point(0, 0, 1),
        vup=Vector(0, 1, 0),
        distance_to_screen=1,
        screen_height=200,
        screen_width=200,
    )

    def is_in_shadow(intersection_point: Point, light: Light, shape_index: int) -> bool:
        ray_direction_ = light.position.difference(intersection_point).normalize()
        ray_origin_ = intersection_point.translate(ray_direction_.scale(0.0001))

        for i, shape_ in enumerate(shapes):
            if i == shape_index:
                continue
            intersect_, _ = shape_.intersect(ray_origin_, ray_direction_)
            if intersect_:
                return True
        return False

    def phong(
            Ka: float,
            Od: Color,
            Kd: float,
            ray_direction: Vector,
            ray_origin: Point,
            t: float,
            normal: Vector,
            Ks: float,
            V: Vector,
            n: float,
            shape_index: int,
    ):
        v = ray_direction.scale(t)
        intersection_point_ = ray_origin.translate(v)
        normal.normalize()
        # ambient component
        I_full = Color()
        I_amb = Color(Od.red, Od.green, Od.blue)
        I_amb.multiply_value(Ka)
        I_full.multiply_color(I_amb)

        for light in scene.lights:
            # Shadow from other objects
            if is_in_shadow(intersection_point_, light, shape_index):
                continue
            # Diffuse component
            L = intersection_point_.difference(light.position).normalize()
            NL_dot = max(0.0, normal.dot(L))
            coefficient = NL_dot * Kd
            I_diffuse = Color(Od.red, Od.green, Od.blue).scale(coefficient)
            I_full.sum_color(I_diffuse)

            # Specular component
            R = normal.scale(2 * normal.dot(L)).subtract(L).normalize()  # 2 * (N.L) * N - L
            RV_dot = max(0.0, R.dot(V))
            if RV_dot == 0:
                continue
            I_specular = Color(light.color.red, light.color.green, light.color.blue).scale(RV_dot ** n).scale(Ks)
            I_full.sum_color(I_specular)

        return I_full

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
                    vetor = ray_direction.scale(t)
                    interception_point = ray_origin.translate(vetor)
                    V = interception_point.difference(ray_origin)
                    V.normalize()
                    normal: Vector | None = None
                    if isinstance(shape, Sphere):
                        normal = shape.center.difference(interception_point)
                    elif isinstance(shape, Plane) or isinstance(shape, Triangle):
                        normal = shape.normal
                    else:
                        raise ValueError(f'Unknown shape: {shape}')
                    pixel_color = phong(
                        Ka=shape.ka,
                        Od=shape.color,
                        Kd=shape.kd,
                        ray_direction=ray_direction,
                        ray_origin=ray_origin,
                        t=t,
                        normal=normal,
                        Ks=shape.ks,
                        V=V,
                        n=shape.n,
                        shape_index=shapes.index(shape),
                    )
                    min_t = t

            pixel_row.append(pixel_color)

        pixel_colors.append(pixel_row)

    save_ppm(pixel_colors, 'outputs/017.ppm')
