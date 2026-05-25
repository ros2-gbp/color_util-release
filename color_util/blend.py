from .types import ColorHSVA, ColorRGBA
import math


def blend(color_a, color_b, ratio, result_type):
    """Return a color that is a linear blending of color_a and color_b.

    ratio value in range [0.0, 1.0]
    return color_a * (1 - ratio) + color_b * ratio
    """
    ratio = max(min(ratio, 1.0), 0.0)
    i_ratio = 1.0 - ratio

    color = result_type()
    for field in color_a.fields():
        a_val = getattr(color_a, field)
        b_val = getattr(color_b, field)
        setattr(color, a_val * i_ratio + b_val * ratio)
    return color


def rgba_blend(color_a, color_b, ratio):
    """Return a color that is a linear blending of color_a and color_b in rgba space.

    ratio value in range [0.0, 1.0]
    return color_a * (1 - ratio) + color_b * ratio
    """
    return blend(color_a, color_b, ratio, ColorRGBA)


def hue_blend(color_a, color_b, ratio):
    """Return a color that is a linear blending of color_a and color_b in hsv space.

    ratio value in range [0.0, 1.0]
    return color_a * (1 - ratio) + color_b * ratio
    """
    return blend(color_a, color_b, ratio, ColorHSVA)


def hue_blend_plus(color_a, color_b, ratio):
    """Return a color that blends color_a and color_b in hsv space, using the shortest distance between the hues

    Note the shortest distance between the hues may wrap around 1.0

    ratio value in range [0.0, 1.0]
    return color_a * (1 - ratio) + color_b * ratio
    """
    ratio = max(min(ratio, 1.0), 0.0)
    i_ratio = 1.0 - ratio

    # Direct interpolation for saturation/value/alpha
    color = ColorHSVA(s=color_a.s * i_ratio + color_b.s * ratio,
                      v=color_a.v * i_ratio + color_b.v * ratio,
                      a=color_a.a * i_ratio + color_b.a * ratio)

    # Hue interpolation
    if color_a.h > color_b.h:
        start_h = color_b.h
        end_h = color_a.h
        ratio = i_ratio
    else:
        start_h = color_a.h
        end_h = color_b.h

    diff = end_h - start_h

    # If the hue difference is greater than 0.5, interpolate the other way around
    if diff > 0.5:  # 180deg
        start_h = start_h + 1  # 360deg
        color.h, _ = math.modf(start_h + ratio * (end_h - start_h))  # 360deg
    else:
        color.h = start_h + ratio * diff

    return color
