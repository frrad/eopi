import binary_tree
import random


def test_tree(randseed=0, values=range(5)):
    random.seed(randseed)

    root = binary_tree.BinaryTree(values.pop())

    nodes = [root]
    while len(values) > 0:
        x = nodes[random.randint(0, len(nodes) - 1)]
        if random.randint(0, 1) == 1:
            new_node = x.add_left(values[-1])
        else:
            new_node = x.add_right(values[-1])
        if new_node is not None:
            values.pop()
            nodes.append(new_node)

    return root
