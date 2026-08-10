import colorgram


def extract_colors():

    extracted_colors = colorgram.extract("img.jpg", 60)
    colors = []

    for color in extracted_colors:
        rgb = color.rgb
        rgb_tuple = (rgb.r, rgb.g, rgb.g)
        colors.append(rgb_tuple)

    white = (249, 249, 249)
    white_2 = (250, 248, 248)
    colors.remove(white)
    colors.remove(white_2)

    return colors
