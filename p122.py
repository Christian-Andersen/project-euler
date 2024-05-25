# Efficient Exponentiation


class Tree:
    def __init__(self, data, parent) -> None:
        self.data = data
        self.parent = parent
        self.children = []


tree = Tree(1, None)


def deepen_tree(node, path):
    path = [node.data]
    if not node.children:
        pass
    else:
        for child in node.children:
            deepen_tree(child)
