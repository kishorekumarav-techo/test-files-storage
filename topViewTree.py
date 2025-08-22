from collections import deque

# Binary Tree Node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def top_view(root):
    if not root:
        return []

    # dictionary to store first node at each horizontal distance
    hd_map = {}

    # queue -> stores (node, horizontal_distance)
    q = deque([(root, 0)])

    while q:
        node, hd = q.popleft()

        # store first node for each hd
        if hd not in hd_map:
            hd_map[hd] = node.val

        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    # sort by horizontal distance and return values
    return [hd_map[hd] for hd in sorted(hd_map.keys())]


# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.right = Node(7)

    print("Top View:", top_view(root))
