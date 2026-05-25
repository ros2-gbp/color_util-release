from color_util import ColorHSVA, ColorHSVA24, ColorRGBA, ColorRGBA24
from color_util import convert_color_to_float, convert_color_to_int
from color_util import convert_color_to_rgb, convert_color_to_hsv
from color_util import NamedColor, NamedColor24

import pytest


def test_full_color():
    inc = 1  # can increase this to speed up tests

    for i in range(0, 256, inc):
        for j in range(0, 256, inc):
            for k in range(0, 256, inc):
                for a in range(0, 256, 50):  # don't test all alpha values
                    rgba24 = ColorRGBA24(i, j, k, a)
                    hsva24 = ColorHSVA24(i, j, k, a)

                    rgba = convert_color_to_float(rgba24)
                    hsva = convert_color_to_float(hsva24)

                    assert rgba24 == convert_color_to_int(rgba)
                    assert hsva24 == convert_color_to_int(hsva)


def check_conversion(r, g, b, h, s, v, a=0.9, epsilon=0.001):
    rgba = ColorRGBA(r, g, b, a)
    hsva = ColorHSVA(h, s, v, a)

    converted_rgba = convert_color_to_rgb(hsva)

    assert converted_rgba.r == pytest.approx(r, abs=epsilon)
    assert converted_rgba.g == pytest.approx(g, abs=epsilon)
    assert converted_rgba.b == pytest.approx(b, abs=epsilon)
    assert converted_rgba.a == pytest.approx(a, abs=epsilon)

    converted_hsva = convert_color_to_hsv(rgba)
    assert converted_hsva.h == pytest.approx(h, abs=epsilon)
    assert converted_hsva.s == pytest.approx(s, abs=epsilon)
    assert converted_hsva.v == pytest.approx(v, abs=epsilon)
    assert converted_hsva.a == pytest.approx(a, abs=epsilon)


def test_random_color_check():
    # black
    check_conversion(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    # white
    check_conversion(1.0, 1.0, 1.0, 0.0, 0.0, 1.0)

    # red
    check_conversion(1.0, 0.0, 0.0, 0.0, 1.0, 1.0)

    # green
    check_conversion(0.0, 1.0, 0.0, 0.33333, 1.0, 1.0)

    # blue
    check_conversion(0.0, 0.0, 1.0, 0.66667, 1.0, 1.0)

    # cyan
    check_conversion(0.0, 1.0, 1.0, 0.5, 1.0, 1.0)

    # magenta
    check_conversion(1.0, 0.0, 1.0, 0.83333, 1.0, 1.0)

    # yellow
    check_conversion(1.0, 1.0, 0.0, 0.16667, 1.0, 1.0)

    # gray
    check_conversion(0.8, 0.8, 0.8, 0.0, 0.0, 0.8)


def test_named_colors():
    named_colors_ints = list(NamedColor24)
    assert len(named_colors_ints) == 55
    transp = named_colors_ints[0]
    assert transp.a == 0

    red = named_colors_ints[1]
    assert red.r == 0xe6

    assert NamedColor24.RED.r == 0xe6

    named_colors_floats = list(NamedColor)
    transp = named_colors_floats[0]
    assert transp.a == 0.0, transp

    red = named_colors_floats[1]
    assert red.r == pytest.approx(0xe6 / 0xff, abs=0.001)

    assert NamedColor.RED.r == 0xe6 / 0xff
