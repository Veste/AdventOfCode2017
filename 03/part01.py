import math

input_number = 325489
#input_number = 61

ring = 0
num_squares = 1

while num_squares < input_number:
    ring += 1
    num_squares += (8 * ring)

# now 'ring' is the ring that our number is in
triangle_number_of_ring = int((ring * (ring - 1)) / 2)
first_number_in_ring = (8 * triangle_number_of_ring) + 2

# edge length is always odd... (i.e. 3, 5, 7, etc.)
# distance from the first number to the right-hand side center axis is ring number - 1
right_hand_axis = first_number_in_ring + ring - 1
increment_for_other_axes = ring * 2

modulo_6_mapped = (input_number - first_number_in_ring) % (ring * 2)
thing = math.fabs( modulo_6_mapped - (ring - 1) )
print( thing + ring )
