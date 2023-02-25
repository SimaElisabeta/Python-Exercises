# EX 1
# Regex validate PIN code


def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)


# EX 2
# Number of People in the Bus

# V1
def number(bus_stops):
    people_in = 0
    people_out = 0
    for bus_stop in bus_stops:
        people_in += bus_stop[0]
        people_out += bus_stop[1]
    return people_in - people_out


# V2
def number_v2(bus_stops):
    get_in, get_off = zip(*bus_stops)
    print(list(zip(*bus_stops)))
    print(get_in)
    print(get_off)
    return sum(get_in) - sum(get_off)


bus = [[10, 0], [3, 5], [5, 8]]

print(number(bus))
print(number_v2(bus))


# EX 3
# Counting Duplicates

def duplicate_count(text):
    max_count = 0
    text_lower = text.lower()
    found_duplicate = ''
    for char in text_lower:
        if text_lower.count(char) > 1 and char not in found_duplicate:
            found_duplicate += char
            max_count += 1
    return max_count


# EX 4
# String ends with?

def solution(text, ending):
    check_last = len(text) - len(ending)
    return ending in text[check_last:]


# EX 5
# Noisy Cell Counts

def cleaned_counts(data):
    result = []
    curr_max_nr = data[0]
    for i in range(len(data)):
        if data[i] >= curr_max_nr:
            curr_max_nr = data[i]
            result.append(curr_max_nr)
        else:
            result.append(curr_max_nr)
    return result


# EX 6
"""
def construct_submatrix(matrix, rows_to_delete, cols_to_delete):
    new_matrix = []
    for row in range(len(matrix)):
        for nr in rows_to_delete:
            if nr != row:
                new_matrix.append(matrix[row])

    if len(rows_to_delete) == 0:
        new_matrix = matrix.copy()

    for row in new_matrix:
        row_source_copy = row.copy()
        for c_i in range(len(row_source_copy) - 1, -1, -1):
            if c_i in cols_to_delete:
                row.pop(c_i)
    return new_matrix


matrix = [
    [1, 0, 0, 2],
    [0, 5, 0, 1],
    [0, 0, 3, 5]
]
rowsToDelete = [1]
columnsToDelete = [0, 2]

print(construct_submatrix(matrix, rowsToDelete, columnsToDelete))
"""
