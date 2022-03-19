class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def traverse(root):
    if root:
        print(root.data)
        traverse(root.left)
        traverse(root.right)


def exchange(root):
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp
        traverse(root)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    # traverse(root)
    exchange(root)
