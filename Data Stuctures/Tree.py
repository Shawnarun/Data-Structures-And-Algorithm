class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children
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
