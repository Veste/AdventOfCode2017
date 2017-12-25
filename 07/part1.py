# For part 1, we don't need to actually construct the tree (I assume part 2 will probably require it...)
# We just need to find the name that shows up in none of the right-hand-side lists.
# So! Let's iterate on our input and build sets of seen and unseen names. We should end up with
# a single unseen-on-the-right item.

input_file_name = 'input'
#input_file_name = 'test_input'

seen_right_hand_names = set()
seen_left_hand_names = set()
with open(input_file_name) as input_file:
    for input_line in input_file:
        input_line_split = input_line.split()

        seen_left_hand_names.add(input_line_split[0])

        # If there's a name with no right-hand side we can arbitrarily drop it; it's only relevant
        # if our input is malformed.
        if len(input_line_split) != 2:
            for right_hand_name in input_line_split[3::]:
                if right_hand_name[-1] == ',':
                    seen_right_hand_names.add(right_hand_name[:-1:])
                else:
                    seen_right_hand_names.add(right_hand_name)
            # end for
        # end if
    # end for
# end with

difference = seen_left_hand_names - seen_right_hand_names
print(difference)
