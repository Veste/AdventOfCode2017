
#input_file_name = 'test_input'
input_file_name = 'input'

registers = dict()


def increment_register(register_name, value):
    registers[register_name] += value


def decrement_register(register_name, value):
    registers[register_name] -= value


def greater_than(register_name, value):
    return registers[register_name] > value


def less_than(register_name, value):
    return registers[register_name] < value


def equal_to(register_name, value):
    return registers[register_name] == value


def not_equal_to(register_name, value):
    return not equal_to(register_name, value)


def greater_than_or_equal_to(register_name, value):
    return greater_than(register_name, value) or equal_to(register_name, value)


def less_than_or_equal_to(register_name, value):
    return less_than(register_name, value) or equal_to(register_name, value)


operation_dictionary = {
    'inc': increment_register,
    'dec': decrement_register,
    '>': greater_than,
    '<': less_than,
    '>=': greater_than_or_equal_to,
    '<=': less_than_or_equal_to,
    '==': equal_to,
    '!=': not_equal_to
}

# Our registers default to 0, so if they all end up negative, 0 is the right answer
# for part 2
max_register_value = 0
with open(input_file_name) as input_file:
    for line in input_file:
        line_split = line.split()

        register_to_modify = line_split[0]
        if register_to_modify not in registers.keys():
            registers[register_to_modify] = 0
        # end if

        condition_register = line_split[4]
        if condition_register not in registers.keys():
            registers[condition_register] = 0
        # end if

        condition_operator = line_split[5]
        condition_value = int(line_split[6])
        if not operation_dictionary[condition_operator](condition_register, condition_value):
            continue
        # end if

        # If we didn't continue above, our test condition passed, so perform the
        # register change operation here
        register_change_operator = line_split[1]
        register_change_value = int(line_split[2])
        operation_dictionary[register_change_operator](register_to_modify, register_change_value)
        max_register_value = max(max_register_value, registers[register_to_modify])
    # end for
# end with

print(max(registers.values()))
print(max_register_value)
