from random import randrange
from time import sleep


class Line:
    def __init__(self, pos: int):
        self.__pos = pos
        self.__count = 0

    def get_count(self):
        return self.__count

    def get_pos(self):
        return self.__pos

    def increment(self):
        self.__count += 1


class Animation:
    def __init__(self,
                 max_line_len: int,
                 distance_between_lines_on_y: int,
                 filed_coord: tuple[int, int],
                 delay_before_print: float,
                 **kwargs
                 ):
        super().__init__(**kwargs)

        self.__line_len: int = max_line_len
        self.__distance_y: int = distance_between_lines_on_y
        self.__field_size: tuple = filed_coord
        self.__sleep_time: float = delay_before_print

        self.__empty_char: str = " "
        self.__char: str = "*"

        self.__lines: list[Line] = list()

        self.__max_string_len: int = 0

    def start(self) -> None:
        last_distance_y: int = 0

        self.__max_string_len: int = self.__get_random_pos()

        self.__lines.append(
            Line(self.__max_string_len)
        )

        string: str = self.__get_string(self.__max_string_len)

        while True:
            if last_distance_y == self.__distance_y:
                string = self.__add_new_line(string)

                last_distance_y = 0

            print(string)

            last_distance_y += 1

            sleep(self.__sleep_time)

            string = self.__check_live_loop(string)

    def __get_random_pos(self) -> int:
        return randrange(self.__field_size[0], self.__field_size[1] + 1)

    def __get_string(self, str_len: int) -> str:
        return self.__empty_char * (str_len - 1) + self.__char

    def __check_live_loop(self, string: str) -> str:
        for current_line in self.__lines:

            current_line.increment()

            if current_line.get_count() >= self.__line_len:
                self.__lines.remove(current_line)

                string = string[:current_line.get_pos() - 1] + self.__empty_char + string[current_line.get_pos():]

        return string

    def __add_new_line(self, string: str) -> str:
        line_pos = self.__get_random_pos()

        line = Line(line_pos)

        self.__lines.append(line)

        if line_pos > self.__max_string_len:
            string = string + self.__get_string(line_pos - self.__max_string_len)

            self.__max_string_len = line_pos

        else:
            string = string[:line_pos - 1] + self.__char + string[line_pos:]

        return string


# Ниже зона с настройками анимации

max_line_len: int = 10

distance_between_lines_on_y: int = 2

min_coord_on_field: int = 1
max_coord_on_field: int = 170

delay_before_print: float = .07

# Конец зоны

Animation(
    max_line_len,
    distance_between_lines_on_y,
    (min_coord_on_field, max_coord_on_field),
    delay_before_print
).start()
