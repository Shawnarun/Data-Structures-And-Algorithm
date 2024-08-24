class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, parentData=None):
        node = Treenode(data)

        if self.root is None:
            self.root = node
            return

        ParentNode = self.findNode(parentData, self.root)
        if not ParentNode:
            print("Parent Not Found")
            return
        ParentNode.children.append(node)

    def findNode(self, data, node):
        if node.data == data:
            return node

        for child in node.children:
            nodeFound = self.findNode(data, child)
            if nodeFound is not None:
                return nodeFound

        return None

    def display(self, depth=0, node=None):
        if not node:
            node = self.root
        if not node:
            return
        print(" " * depth, node.data)
        for child in node.children:
            self.display(depth + 1, child)


treenode = Treenode(5)
treenode1 = Treenode(7)

tree = Tree()
tree.add(5)
tree.add(8, 5)
tree.add(9, 5)
tree.add(15, 9)
tree.add(22, 9)
tree.add(55, 9)
tree.add(98, 8)
tree.add(36, 8)
tree.add(17, 22)
tree.add(59, 22)
tree.display()
