
# input_file_name = 'test_input1'
input_file_name = 'input'

with open(input_file_name) as input_file:
    for line in input_file:
        input_line = line
    # end for
# end with

group_count = 0
garbage_enabled = False

character_index = 0
total_group_score = 0
total_garbage_characters = 0
while character_index < len(input_line):
    character = input_line[character_index]
    if garbage_enabled is True:
        if character == '!':
            character_index += 1
        elif character == '>':
            garbage_enabled = False
        else:
            total_garbage_characters += 1
        # end if
    else:
        if character == '<':
            garbage_enabled = True
        elif character == '{':
            group_count += 1
        elif character == '}':
            total_group_score += group_count
            group_count -= 1
        # end if
    # end if

    character_index += 1
# end while

print("Group score: " + str(total_group_score))
print("Garbage characters: " + str(total_garbage_characters))