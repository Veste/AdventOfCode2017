# For part 2, we want to know the difference between the cycle count for the first and
# second appearance of the duplicate. My naive approach is to take the set from part 1,
# and make it a dict instead, storing the cycle count as the value and continuing to
# use a tuple of the block array as the keys.

input_blocks = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
#input_blocks = [0, 2, 7, 0]

# The length of our block array never changes, so we can just calculate it once.
input_block_length = len(input_blocks)

dict_of_permutations = {}


def find_first_max_and_index(test_array):
    # our numbers are going to always be >= 0, so we can just use -1
    max_element = -1
    index_of_max_element = -1
    for i, element in enumerate(test_array):
        if element > max_element:
            max_element = element
            index_of_max_element = i
        # end if
    # end for
    return index_of_max_element, max_element
# end find_first_max_and_index


number_of_cycles = 0
previous_set_length = 0

# Annoyingly, since lists are mutable and python hash structs require immutable keys, we have to convert our list
# into a tuple to put it into a set.
# This is probably faster using a trie... will look into trie solutions if performance is too poor; don't want to
# write my own trie if I don't need to.
dict_of_permutations[tuple(input_blocks)] = 0
while True:
    # We're doing another cycle, so count it!
    number_of_cycles += 1

    # First, find the index and value of the first maximum
    max_element_index, max_element_value = find_first_max_and_index(input_blocks)

    # Reset the value at the max index to 0 to prepare for redistribution; we've already extracted
    # the value, which tells us how much to iterate
    input_blocks[max_element_index] = 0

    # Iterate using a range defined by the max value. Use modulus over the length of the array
    # to avoid index-out-of-range.
    for redistribution_increment in range(max_element_value):
        # We need to increment by 1 first, because redistribution starts at the index AFTER
        # the index of our max value. Probably slightly faster to fold the +1 into the range call,
        # but more ugly, I think...
        redistribution_index = (max_element_index + redistribution_increment + 1) % input_block_length
        input_blocks[redistribution_index] += 1
    # end for

    # Now, our redistribution is complete, check our dict! If we've seen this combo before,
    # break out of our loop.
    tuple_of_blocks = tuple(input_blocks)
    if dict_of_permutations.get(tuple_of_blocks) is None:
        dict_of_permutations[tuple_of_blocks] = number_of_cycles
    else:
        break
# end while

# Using the last-seen tuple_of_blocks value, we can get the previous cycle count, and compare
# against the cycle count that we exited the loop with.
print(number_of_cycles - dict_of_permutations[tuple_of_blocks])
