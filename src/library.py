def sort(ars):
    return sorted(
        [[arr, len(arr)] for arr in ars],
        key=lambda data: data[1],
        reverse=True
    )


def rar(*ars):
    if len(ars) == 1:
        return ars

    ars_with_lens = sort(ars)

    ars = [data[0] for data in ars_with_lens]
    lens = [data[1] for data in ars_with_lens]

    new_arr = [[None for i in range(len(ars))] for i in range(lens[0])]

    for index, y in enumerate(ars[0]):
        new_arr[index][0] = y

    arr_index: int = 1

    for arr in ars[1:]:
        for index, y in enumerate(arr):
            new_arr[index][arr_index] = y

        y_index_in_new_arr = lens[arr_index]
        y_index_in_arr = 0

        while y_index_in_new_arr != lens[0]:
            if y_index_in_arr == lens[arr_index]:
                y_index_in_arr = 0

            new_arr[y_index_in_new_arr][arr_index] = arr[y_index_in_arr]

            y_index_in_arr += 1
            y_index_in_new_arr += 1

        arr_index += 1

    return new_arr
