
valid_passphrase_count = 0
with open('input') as input_file:
    for line in input_file:
        words = line.split()
        if len(words) == len(set(words)):
            # If there was a duplicate word, the set form would have rejected it, resulting in a lower length
            valid_passphrase_count += 1

print( valid_passphrase_count )
