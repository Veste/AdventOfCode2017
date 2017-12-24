
checksum = 0

with open('input') as input_file:
    for line in input_file:
        numbers_as_strings = line.split()
        numbers = [int(n) for n in numbers_as_strings]
        max_number_in_line = max(numbers)
        min_number_in_line = min(numbers)
        checksum += (max_number_in_line - min_number_in_line)

print(checksum)