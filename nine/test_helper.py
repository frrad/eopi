import binary_tree
import random


def ex_tree(randseed, size=5, randvals=False):
    return make_tree(binary_tree.BinaryTree, randseed, size, randvals)


def ex_pptree(randseed, size=5, randvals=False):
    return make_tree(binary_tree.BinaryTreePP, randseed, size, randvals)


def rand_leaf(root, seed):
    random.seed(seed)
    while root.left is not None or root.right is not None:
        if random.randint(0, 1) == 0 and root.left is not None:
            root = root.left
            continue
        if root.right is not None:
            root = root.right
            continue
    return root


def make_tree(constr, randseed, size=5, randvals=False):
    values = [random.randint(0, size) for x in xrange(
        size)] if randvals else range(size)
    random.seed(randseed)

    root = constr(values.pop())

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
