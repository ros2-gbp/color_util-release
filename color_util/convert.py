from std_msgs.msg import ColorRGBA as ColorRGBAMsg
from .types import ColorHSVA, ColorHSVA24, ColorRGBA, ColorRGBA24


# Single number calculations
def int24_to_float(n):
    return n / 255.0


def float_to_int24(n):
    return int(n * 255.0)


# Numeric color conversion
def convert_color_to_float(int_color):
    if isinstance(int_color, ColorRGBA24):
        float_color = ColorRGBA()
    elif isinstance(int_color, ColorHSVA24):
        float_color = ColorHSVA()
    else:
        raise TypeError(f'Cannot call convert_color_to_float with type {type(int_color)}')

    for field in int_color.__dataclass_fields__:
        int_val = getattr(int_color, field)
        setattr(float_color, field, int24_to_float(int_val))

    return float_color


def convert_color_to_int(float_color):
    if isinstance(float_color, ColorRGBA):
        int_color = ColorRGBA24()
    elif isinstance(float_color, ColorHSVA):
        int_color = ColorHSVA24()
    else:
        raise TypeError(f'Cannot call convert_color_to_int with type {type(float_color)}')

    for field in float_color.__dataclass_fields__:
        float_val = getattr(float_color, field)
        setattr(int_color, field, float_to_int24(float_val))

    return int_color


# Colorspace conversions
# based on
# https://stackoverflow.com/questions/3018313/algorithm-to-convert-rgb-to-hsv-and-hsv-to-rgb-in-range-0-255-for-both
def convert_color_to_hsv(rgba, epsilon=0.00001):
    if isinstance(rgba, ColorRGBA24):
        return convert_color_to_int(convert_color_to_hsv(convert_color_to_float(rgba)))

    out = ColorHSVA()

    # Alpha channel
    out.a = rgba.a

    # Three way max/min
    min_v = rgba.r if rgba.r < rgba.g else rgba.g
    min_v = min_v if min_v < rgba.b else rgba.b

    max_v = rgba.r if rgba.r > rgba.g else rgba.g
    max_v = max_v if max_v > rgba.b else rgba.b

    # Value Channel
    out.v = max_v

    delta = max_v - min_v
    if max_v == 0.0 or delta < epsilon:
        # Grayscale
        out.s = 0.0
        out.h = 0.0  # undefined hue
        return out

    # Saturation Channel (note max_v!=0)
    out.s = (delta / max_v)

    if rgba.r >= max_v:  # > is invalid for valid input
        out.h = (rgba.g - rgba.b) / delta  # between yellow & magenta
    elif rgba.g >= max_v:
        out.h = 2.0 + (rgba.b - rgba.r) / delta  # between cyan & yellow
    else:
        out.h = 4.0 + (rgba.r - rgba.g) / delta  # between magenta & cyan

    out.h *= 60.0  # convert to degrees

    if out.h < 0.0:  # convert to positive degrees
        out.h += 360.0
    out.h /= 360.0  # convert to be [0, 1]

    return out


def convert_color_to_rgb(hsva, epsilon=0.00001):
    if isinstance(hsva, ColorHSVA24):
        return convert_color_to_int(convert_color_to_rgb(convert_color_to_float(hsva)))

    if hsva.s <= 0.0:  # < is invalid for valid input
        # Grayscale
        return ColorRGBA(hsva.v, hsva.v, hsva.v, hsva.a)

    hh = hsva.h * 360.0
    if hh >= 360.0:
        hh = 0.0
    hh /= 60.0

    i = int(hh)
    ff = hh - i
    p = hsva.v * (1.0 - hsva.s)
    q = hsva.v * (1.0 - (hsva.s * ff))
    t = hsva.v * (1.0 - (hsva.s * (1.0 - ff)))

    if i == 0:
        return ColorRGBA(hsva.v, t, p, hsva.a)
    elif i == 1:
        return ColorRGBA(q, hsva.v, p, hsva.a)
    elif i == 2:
        return ColorRGBA(p, hsva.v, t, hsva.a)
    elif i == 3:
        return ColorRGBA(p, q, hsva.v, hsva.a)
    elif i == 4:
        return ColorRGBA(t, p, hsva.v, hsva.a)
    else:  # if i == 5:
        return ColorRGBA(hsva.v, p, q, hsva.a)


# To ROS Msg
def convert_color_to_msg(color):
    if isinstance(color, ColorRGBA):
        msg = ColorRGBAMsg()
        msg.r = color.r
        msg.g = color.g
        msg.b = color.b
        msg.a = color.a
        return msg
    elif isinstance(color, ColorRGBA24):
        return convert_color_to_msg(convert_color_to_float(color))
    elif isinstance(color, (ColorHSVA, ColorHSVA24)):
        return convert_color_to_msg(convert_color_to_rgb(color))
    else:
        raise TypeError(f'Cannot call convert_color_to_msg with type {type(color)}')
