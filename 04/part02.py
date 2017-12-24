
valid_passphrase_count = 0
with open('input') as input_file:
    for line in input_file:
        sorted_words = [''.join(sorted(w)) for w in line.split()]
        if len(sorted_words) == len(set(sorted_words)):
            # If there was a duplicate word, the set form would have rejected it, resulting in a lower length
            valid_passphrase_count += 1
        else:
            print(sorted_words)

print( valid_passphrase_count )
