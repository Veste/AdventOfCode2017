
checksum = 0

with open('input') as input_file:
    for line in input_file:
        numbers = [int(n) for n in line.split()]
        numbers.sort()
        for index in range(len(numbers)):
            smaller_number = numbers[index]
            divisible_found = False
            for larger_number in numbers[:index+1:-1]:
                if smaller_number > larger_number:
                    break
                if (larger_number % smaller_number) == 0:
                    checksum += larger_number / smaller_number
                    divisible_found = True
                    break
            if divisible_found is True:
                break

print(checksum)