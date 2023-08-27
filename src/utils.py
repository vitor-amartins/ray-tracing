def scale_color(value):
    return int(255 * value)


def save_ppm(image_matrix, filename):
    height = len(image_matrix)
    width = len(image_matrix[0])

    with open(filename, 'w') as f:
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        f.write('255\n')

        for row in image_matrix:
            for color in row:
                r, g, b = scale_color(color.x), scale_color(color.y), scale_color(color.z)
                f.write(f'{r} {g} {b} ')
            f.write('\n')
