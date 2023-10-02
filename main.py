from src.camera import Camera
from src.plane import Plane
from src.point import Point
from src.scene import Scene
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
        point=Point(0, 0, 0),
        normal=Vector(0, 0, 1),
        color=GREEN,
    )

    shapes = [sphere1,sphere2]
    light_1 = Light((Point(0,10,3)),Color(1,1,1))
    # light_2 = Light((Point(20,0,3)),Color(1,1,1))
    scene = Scene(
        ambient_color=BLACK,
        lights=[light_1],
    )

    camera = Camera(
        c=Point(0, 0, 0),
        m=Point(0, 0, 1),
        vup=Vector(0, 1, 0),
        distance_to_screen=1,
        screen_height=200,
        screen_width=200,
    )
    def reflexion_vector(n,L):
        ctc = n.dot(L)*2
        n.scale(ctc)
        auxVet = Vector(n.x - L.x, n.y - L.y, n.z - L.z)
        return auxVet

    def phong(Ka,Od,Kd,ray_direction,ray_origin,t,normal,Ks,V,n):
        #ambient component
        color = Color(0,0,0)
        color.multiply_value(Ka)
        
        for light in scene.lights:
            #diffuse component
            diffuse = Color(0,0,0)
            diffuse.sum_color(Od)
            diffuse.multiply_color(light.color)
            diffuse.multiply_value(Kd)
            L = Vector()
            vetor = ray_direction.scale(t)
            interception_point = ray_origin.translate(vetor)
            L = interception_point.difference(light.position)
            L.normalize()
            normal.normalize()
            zero = 0

            diffuse.multiply_value(max(zero,L.dot(normal)))
            color.sum_color(diffuse)
            #Specular component

            # specular = Color(0,0,0)
            # specular = light.color
            # specular.multiply_value(Ks)
            # R = reflexion_vector(normal,L)
            # R.normalize()
            # specular.multiply_value(pow(0,R.dot(V),n))

            # color.sum_color(specular)
            


        return color
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
                    V = Vector()
                    
                    vetor = ray_direction.scale(t)
                    interception_point = ray_origin.translate(vetor)
                    V = interception_point.difference(ray_origin)
                    V.normalize()
                    if hasattr(shape,'radius'):
                        pixel_color = phong(shape.ka,shape.color,shape.kd,ray_direction,ray_origin,t,shape.center.difference(interception_point),shape.ks,V,shape.n)
                        min_t = t
                    else:
                        pixel_color = phong(shape.ka,shape.color,shape.kd,ray_direction,ray_origin,t,shape.normal,shape.ks,V,shape.n)
                        min_t = t

            pixel_row.append(pixel_color)

        pixel_colors.append(pixel_row)

    save_ppm(pixel_colors, 'outputs/012.ppm')
