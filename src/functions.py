import time
from math import sin, cos, pi

from src.output import print_simple_graphic, print_hard_graphic, run_time_hard_print
from src.library import rar


def get_period(delta):
    return round(2 * pi / delta)


def cos_for_graphic(fi: float, x: int, delta: float):
    return cos(fi + x * delta)


def sin_for_graphic(fi: float, x: int, delta: float):
    return sin(fi + x * delta)


def graphic(func, fi: float, delta: float):
    return [func(fi, x, delta) for x in range(get_period(delta))]


def COS(
        k: float = 1.0,
        fi: float = 0.0,
        n: int = 1,
        delay: float = 0.05,
        start_empty_char: str = " ",
        main_char: str = "*"
): print_simple_graphic(
    graphic(cos_for_graphic, fi, k * 0.1),
    n,
    delay,
    start_empty_char,
    main_char
)


def SIN(
        k: float = 1.0,
        fi: float = 0.0,
        n: int = 1,
        delay: float = 0.05,
        start_empty_char: str = " ",
        main_char: str = "*"
):
    print_simple_graphic(
        graphic(sin_for_graphic, fi, k * 0.1),
        n,
        delay,
        start_empty_char,
        main_char
    )


def COS_SIN(
        sin_k: float = 1.0,
        cos_k: float = 1.0,
        sin_fi: float = 0.0,
        cos_fi: float = 0.0,
        n: int = 1,
        delay: float = 0.05,
        start_empty_char: str = " ",
        middle_empty_char: str = " ",
        main_char: str = "*",
):
    if sin_k % cos_k == 0 or cos_k % sin_k == 0:
        print_hard_graphic(
            list(map(
                lambda coord: sorted(coord),
                rar(
                    graphic(sin_for_graphic, sin_fi, sin_k * 0.1),
                    graphic(cos_for_graphic, cos_fi, cos_k * 0.1))
            )),
            n,
            delay,
            [
                start_empty_char,
                middle_empty_char
            ],
            main_char
        )
    else:
        for x in range(get_period(max(sin_k, cos_k) * 0.1) * n):
            run_time_hard_print(
                sorted(
                    [
                        sin_for_graphic(sin_fi, x, sin_k * 0.1),
                        cos_for_graphic(cos_fi, x, cos_k * 0.1),
                    ]
                ),
                [
                    start_empty_char,
                    middle_empty_char
                ],
                main_char
            )
            time.sleep(delay)
