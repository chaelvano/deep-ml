def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    transpose = []

    for i in range(len(a[0])):
        new_row = []

        for j in range(len(a)):
            new_row.append(a[j][i])

        transpose.append(new_row)

    return transpose