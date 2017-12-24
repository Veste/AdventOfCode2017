import math

input_num = 325489

# the numbers have to constantly grow, so we can conservatively cap our array size at
# our input number
matrix_dimsize = int(math.ceil(math.sqrt(input_num)))
matrix = [[0 for _ in range(matrix_dimsize)] for _ in range(matrix_dimsize)]

matrix_halfdim = int(matrix_dimsize / 2)

matrix_index = [matrix_halfdim, matrix_halfdim]
matrix[matrix_index[0]][matrix_index[1]] = 1

increment_amount = 1
first_increment = True
increment_type = 0

finished = False
while True:
    for _ in range(increment_amount):
        if increment_type == 0:
            matrix_index[0] += 1
        elif increment_type == 1:
            matrix_index[1] += 1
        elif increment_type == 2:
            matrix_index[0] -= 1
        elif increment_type == 3:
            matrix_index[1] -= 1
        # endif

        index1 = matrix[matrix_index[0] + 1][matrix_index[1] + 1]
        index2 = matrix[matrix_index[0] + 1][matrix_index[1] + 0]
        index3 = matrix[matrix_index[0] + 1][matrix_index[1] - 1]

        index4 = matrix[matrix_index[0] - 1][matrix_index[1] + 1]
        index5 = matrix[matrix_index[0] - 1][matrix_index[1] + 0]
        index6 = matrix[matrix_index[0] - 1][matrix_index[1] - 1]

        index7 = matrix[matrix_index[0] + 0][matrix_index[1] + 1]
        index8 = matrix[matrix_index[0] + 0][matrix_index[1] - 1]

        matrix[matrix_index[0]][matrix_index[1]] = (index1 + index2 + index3 + index4 + index5 + index6 + index7 + index8)

        if matrix[matrix_index[0]][matrix_index[1]] > input_num:
            print( matrix[matrix_index[0]][matrix_index[1]] )
            finished = True
            break
        # endif
    # end for

    if finished is True:
        break

    increment_type += 1
    increment_type %= 4

    if first_increment is True:
        first_increment = False
    else:
        first_increment = True
        increment_amount += 1
    # endif
