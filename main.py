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

MAX_REFLECTION_DEPTH = 3
RED = Color(1, 0, 0)
GREEN = Color(0, 1, 0)
BLUE = Color(0, 0, 1)
WHITE = Color(1, 1, 1)
BLACK = Color(0, 0, 0)

# Shapes
sphere1 = Sphere(
    center=Point(0, 0, 8),
    radius=2,
    color=RED,
    kr=0,
)
sphere2 = Sphere(
    center=Point(0, 0, 6),
    radius=1,
    color=BLUE,
    kd=2,
    kr=0,
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

# Lights
light_1 = Light(
    position=Point(0, 10, 0),
    color=Color(1, 1, 1),
)
light_2 = Light(
    position=Point(20, 0, 3),
    color=Color(1, 1, 1),
)

# Scene & Shapes
shapes: list[Shape] = [
    sphere1,
    sphere2,
    plane,
]
scene = Scene(
    ambient_color=BLACK,
    lights=[
        light_1,
        light_2,
    ],
)

# Camera
camera = Camera(
    c=Point(4, 0, 0),
    m=Point(4, 0, 1),
    vup=Vector(0, 1, 0),
    distance_to_screen=1,
    screen_height=640,
    screen_width=640,
)


def is_in_shadow(intersection_point: Point, light: Light, shape_index: int) -> bool:
    ray_direction = light.position.difference(intersection_point).normalize()
    ray_origin = intersection_point.translate(ray_direction.scale(0.0001))

    for i, shape_ in enumerate(shapes):
        if i == shape_index:
            continue
        intersect, _ = shape_.intersect(ray_origin, ray_direction)
        if intersect:
            return True
    return False


def phong(
        ka: float,
        od: Color,
        kd: float,
        ray_direction: Vector,
        ray_origin: Point,
        t: float,
        normal: Vector,
        ks: float,
        v: Vector,
        n: float,
        shape_index: int,
):
    intersection_point = ray_origin.translate(ray_direction.scale(t))
    normal.normalize()
    # ambient component
    _I_full = Color()
    _I_amb = Color(od.red, od.green, od.blue)
    _I_amb.multiply_value(ka)
    _I_full.multiply_color(_I_amb)

    for light in scene.lights:
        # Shadow from other objects
        if is_in_shadow(intersection_point, light, shape_index):
            continue
        # Diffuse component
        _L = intersection_point.difference(light.position).normalize()
        _NL_dot = max(0.0, normal.dot(_L))
        coefficient = _NL_dot * kd
        _I_diffuse = Color(od.red, od.green, od.blue).scale(coefficient)
        _I_full.sum_color(_I_diffuse)

        # Specular component
        _R = normal.scale(2 * normal.dot(_L)).subtract(_L).normalize()  # 2 * (N.L) * N - L
        _RV_dot = max(0.0, _R.dot(v))
        if _RV_dot == 0:
            continue
        _I_specular = Color(light.color.red, light.color.green, light.color.blue).scale(_RV_dot ** n).scale(ks)
        _I_full.sum_color(_I_specular)

    return _I_full


def cast(ray_origin: Point, ray_direction: Vector, depth: int = 0) -> Color:
    if depth > MAX_REFLECTION_DEPTH:
        return scene.ambient_color

    min_t = float('inf')
    pixel_color = scene.ambient_color

    for shape in shapes:
        intersect, t = shape.intersect(ray_origin, ray_direction)
        if not intersect or t >= min_t:
            continue
        interception_point = ray_origin.translate(ray_direction.scale(t))
        normal = shape.get_normal(interception_point)
        _V = interception_point.difference(ray_origin).normalize()  # Vetor de visualização
        pixel_color = phong(
            ka=shape.ka,
            od=shape.color,
            kd=shape.kd,
            ray_direction=ray_direction,
            ray_origin=ray_origin,
            t=t,
            normal=normal,
            ks=shape.ks,
            v=_V,
            n=shape.n,
            shape_index=shapes.index(shape),
        )
        min_t = t
        reflected_direction = ray_direction.subtract(normal.scale(2 * ray_direction.dot(normal)))
        reflection_origin = interception_point.translate(reflected_direction.scale(0.0001))
        reflection_color = cast(reflection_origin, reflected_direction, depth + 1)

        pixel_color.sum_color(reflection_color.scale(shape.kr))

    return pixel_color


def main():
    pixel_positions = camera.calculate_pixel_position()
    pixel_colors = []
    for row in pixel_positions:
        pixel_row = []
        for pixel in row:
            ray_origin = camera.c
            ray_direction = pixel.difference(ray_origin).normalize()
            pixel_color = cast(ray_origin, ray_direction)
            pixel_row.append(pixel_color)

        pixel_colors.append(pixel_row)

    save_ppm(pixel_colors, 'outputs/022.ppm')


if __name__ == '__main__':
    main()
