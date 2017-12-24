
with open('input') as input_file:
    instruction_array = []
    for line in input_file:
        instruction_array.append(int(line.strip()))

    index = 0
    num_steps = 0
    while index < len(instruction_array):
        # Since our list is numbers, there's an easy way to swap these two values with math instead of a temp varaible
        # But, really, that saves us so little to be confusing...
        t_index = index
        index += instruction_array[index]
        if instruction_array[t_index] > 2:
            instruction_array[t_index] -= 1
        else:
            instruction_array[t_index] += 1

        # And don't forget to count the number of steps!
        num_steps += 1
    # end while
#end with

print(num_steps)