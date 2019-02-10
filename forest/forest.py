#!/usr/bin/env python3

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def gen_flag(self, string):
        traversal = string.split('D')
        return ''.join(self._gen_flag(self.root, trav) for trav in traversal)

    def _gen_flag(self, node, trav):
        if trav == '':
            return node.data
        if trav[0] == 'L':
            return self._gen_flag(node.left, trav[1:])
        elif trav[0] == 'R':
            return self._gen_flag(node.right, trav[1:])
        raise ValueError

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

tree = Tree()
key = 'yuoteavpxqgrlsdhwfjkzi_cmbn'
string = 'DLLDLDLLLLLDLLLLRLDLLDLDLLLRRDLLLLRDLLLLLDLLRLRRRDLLLDLLLDLLLLLDLLRDLLLRRLDLLLDLLLLLDLLLRLDLLDLLRLRRDLLLDLLRLRRRDLLRDLLLLLDLLLRLDLLDLLRLRRDLLLLLDLLRDLLLRRLDLLLDLLLLLDLLRDLLRLRRDLLLDLLLDLLRLRRRDLLLLLDLLLLRLDLLLRRLRRDDLLLRRDLLLRRLRDLLLRLDLRRDDLLLRLDLLLRRRDLLRLRRRDLRRLD'
for char in key:
    tree.insert(char)
flag = tree.gen_flag(string)
print(flag)
