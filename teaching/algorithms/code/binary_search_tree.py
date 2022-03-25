"""Binary Search Tree implementations."""

# Binary Search tree implementation

def insert(root, key, balance_fn = lambda node: node):
    if root:
        root_key, left, right, *_ = root
        if key < root_key:
            result = (root_key, insert(left, key, balance_fn), right, -1)
        elif key > root_key:
            result = (root_key, left, insert(right, key, balance_fn), -1)
        else:
            result = root
    else:
        result = (key, None, None, 0)
    # new node
    return balance_fn(result)


def search(root, key):
    if root is None:
        return None
    root_key, left, right, *_ = root
    if key < root_key:
        return search(left, key)
    if key > root_key:
        return search(right, key)
    return root


# utility functions

def to_string(root):
    """Convert a tree to a string."""
    if root is None:
        return "_"
    root_key, left, right, *extra = root
    left = to_string(left)
    right = to_string(right)
    return f"({root_key}{extra if extra else ''} {left} {right})"


# AVL implementation

def avl_insert(node):
    """Ensure a node is a valid AVL node."""
    if node is None:
        return None
    diff = height_diff(node)
    return update_height(node if abs(diff) <= 1 else avl_fix(node, diff))



def avl_fix(node, diff):
    """Fix an invalid AVL tree."""
    assert node is not None, "Cannot fix a null AVL node."
    k, left, right, height = node
    if diff > 0:  # pylint: disable=no-else-return
        # left is heavier
        ldiff = height_diff(node[1])
        if ldiff < 0:
            left = rotate_left(node[1])
        return rotate_right((k, left, right, height))
    else:
        # right is heavier
        rdiff = height_diff(node[2])
        if rdiff > 0:
            right = rotate_right(node[2])
        return rotate_left((k, left, right, height))

# Tree rotation

def rotate_left(node):
    """Rotate a tree to the left."""
    if node is None:
        return None
    k, left, root, _ = node
    root_key, j, right, _ = root
    return update_height((root_key, update_height((k, left, j, -1)), right, -1))

def rotate_right(node):
    """Rotate a tree to the right."""
    if node is None:
        return None
    k, root, right, _ = node
    root_key, left, j, _ = root
    return update_height((root_key, left, update_height((k, j, right, -1)), -1))


# Node height functions

def node_height(node):
    """Retrieve node height based on a "height cache" stored on the node."""
    return -1 if node is None else node[-1]


def update_height(node):
    """Update node height."""
    if node is None:
        return None
    k, left, right, _ = node
    return (k, left, right, 1 + max(node_height(left), node_height(right)))


def height_diff(node):
    """Compute height difference between left and right subtrees of a node."""
    if node is None:
        return 0
    _, left, right, _ = node
    return node_height(left) - node_height(right)


# Binary tree traversals.

def pre_order(root, visit):
    """Binary tree pre-order traversal."""
    if root:
        _, left, right, *_ = root
        visit(root)
        pre_order(left, visit)
        pre_order(right, visit)


def in_order(root, visit):
    """Binary tree in-order traversal."""
    if root:
        _, left, right, *_ = root
        in_order(left, visit)
        visit(root)
        in_order(right, visit)


def post_order(root, visit):
    """Binary tree post-order traversal."""
    if root:
        _, left, right, *_ = root
        post_order(left, visit)
        post_order(right, visit)
        visit(root)


# Just a test script...

if __name__ == "__main__":
    def main():
        """Example program entry point."""
        elements = [1,2,3,4,5,6,7,8,9,11,10,12]
        tree = None
        for elem in elements:
            tree = insert(tree, elem, avl_insert)

        def print_node(node):
            k, *_ = node
            print(f"{k} ", end="")

        in_order(tree, print_node)
        print()
        print(to_string(tree))
        print(search(tree, 11))

    main()