# As expected, we probably need to just build the tree now. We should probably just run a recursive
# algorithm.

tree = dict()

seen_right_hand_names = set()
with open('input') as input_file:
    for line in input_file:
        split_line = line.split()

        key_name = split_line[0]

        # Slice off the parentheses for the weight
        weight = int(split_line[1][1:-1])

        children = []
        if len(split_line) > 2:
            for child_name in split_line[3::]:
                if child_name[-1] == ',':
                    children.append(child_name[:-1:])
                else:
                    children.append(child_name)
                # end if
            # end for

            # We'll build a set of seen right-hand values, like in part 1,
            # to more easily determine our root node.
            seen_right_hand_names.update(children)
        # end if

        tree_node = {
            'weight': weight,
            'children': children
        }

        tree[key_name] = tree_node
    # end for
# end with

root = None
for tree_key in tree.keys():
    if tree_key not in seen_right_hand_names:
        root = tree_key
        break
    # end if
# end for


def find_weight_imbalance(root_name):
    node = tree[root_name]
    weight_sum = node['weight']

    if node['children'] == []:
        return weight_sum

    child_weights = []
    for child in node['children']:
        child_weight = find_weight_imbalance(child)
        weight_sum += child_weight
        child_weights.append((child_weight, child))
    # end for

    def weight_access_func(x): return x[0]

    max_child_weight = max(child_weights, key=weight_access_func)
    min_child_weight = min(child_weights, key=weight_access_func)
    if max_child_weight != min_child_weight:
        print(tree[max_child_weight[1]])
        print(max_child_weight)
        print(min_child_weight)
        print("%d - %d = %d" % (max_child_weight[0], min_child_weight[0], max_child_weight[0] - min_child_weight[0]))
        print()
    # end if

    return weight_sum
# end find_weight_imbalance


find_weight_imbalance(root)

