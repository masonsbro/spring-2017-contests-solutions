from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def add_to_bin_tree(root, val):
    if val < root.val:
        if root.left is None:
            root.left = Node(val)
        else:
            add_to_bin_tree(root.left, val)
    else:
        if root.right is None:
            root.right = Node(val)
        else:
            add_to_bin_tree(root.right, val)

def build_bin_tree(values):
    gen = iter(values)

    root_node = Node(next(gen))
    for val in gen:
        add_to_bin_tree(root_node, val)
    return root_node

for _ in range(0, int(input())):
    input()
    tree = [int(x) for x in input().split()]
    root = build_bin_tree(tree)
    cols = {}
    bounds = [0, 0]
    queue = deque([(0, root)])
    while queue:
        k, node = queue.popleft()
        if k < bounds[0]:
            bounds[0] = k
        if k > bounds[1]:
            bounds[1] = k

        if k not in cols:
            cols[k] = []
        cols[k].append(node)
        if node.left:
            queue.append((k-1, node.left))
        if node.right:
            queue.append((k+1, node.right))

    out = []
    for i in range(bounds[0], bounds[1] + 1):
        for node in cols[i]:
            out.append(str(node.val))
    print(' '.join(out))
