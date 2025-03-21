import time


def get_string_space_len(y):
    return round((1 + y) * 80)


def create_string(string_space_len: int, empty_char: str, main_char: str):
    return empty_char * string_space_len + main_char


def run_time_simple_print(y: float, start_empty_char: str, main_char: str):
    print(create_string(
        get_string_space_len(y),
        start_empty_char,
        main_char
    ))


def run_time_hard_print(
        coord: list,
        empty_chars: list[str],
        main_char: str
):
    last_string_space_len = get_string_space_len(coord[0])

    string = create_string(
        last_string_space_len,
        empty_chars[0],
        main_char
    )

    empty_char_index = 1

    for y in coord[1:]:
        current_string_space_len = get_string_space_len(y)

        if current_string_space_len - last_string_space_len != 0:
            string += create_string(
                current_string_space_len - last_string_space_len,
                empty_chars[empty_char_index],
                main_char
            )

            empty_char_index += 1

        last_string_space_len = current_string_space_len

    print(string)


def print_hard_graphic(
        tup: list[list],
        n: int, delay: float,
        empty_chars: list[str],
        main_char: str
):
    for _ in range(n):
        for coord in tup:
            run_time_hard_print(
                coord,
                empty_chars,
                main_char
            )

            time.sleep(delay)


def print_simple_graphic(
        tup: list,
        n: int,
        delay: float,
        empty_char: str,
        main_char: str
):
    for _ in range(n):
        for y in tup:
            run_time_simple_print(
                y,
                empty_char,
                main_char
            )

            time.sleep(delay)
