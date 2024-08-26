##########################################################
#   ____  _                          _____               #
#  | __ )(_) __ _ _ __  _ __ _   _  |_   _| __ ___  ___  #
#  |  _ \| |/ _` | '_ \| '__| | | |   | || '__/ _ \/ _ \ #
#  | |_) | | (_| | | | | |  | |_| |   | || | |  __/  __/ #
#  |____/|_|\__,_|_| |_|_|   \__, |   |_||_|  \___|\___| #
#                            |___/                       #
##########################################################

import random

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val=0):
        if self.root is None:
            self.root = Node(val)
            return
        else:
            self.insert_rec(val, self.root)

    def insert_rec(self, val, root):
        if val < root.val:
            if root.left is not None:
                self.insert_rec(val, root.left)
            else:
                root.left = Node(val)
        elif val > root.val:
            if root.right is not None:
                self.insert_rec(val, root.right)
            else:
                root.right = Node(val)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)     
            print(root.val)
            self.inorder(root.right)   


if __name__ == "__main__":

    tree = Tree()

    num_list = [num for num in range(1, 7)]
    random.shuffle(num_list)
    print(num_list)

    for num in num_list:
        tree.insert(num)

    tree.inorder(tree.root)