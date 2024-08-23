#####################################################
#   _     _       _            _   _     _     _    #
#  | |   (_)_ __ | | _____  __| | | |   (_)___| |_  #
#  | |   | | '_ \| |/ / _ \/ _` | | |   | / __| __| #
#  | |___| | | | |   <  __/ (_| | | |___| \__ \ |_  #
#  |_____|_|_| |_|_|\_\___|\__,_| |_____|_|___/\__| #
#                                                   #
#####################################################

import random

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        else:
            curr_node = self.root
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def print_list(self, root=None):
        if root is None:
            root = self.root
        while root is not None:
            print(root.val)
            root = root.next
        
if __name__ == "__main__":

    linked_list = LinkedList()

    num_list = [num for num in range(1, 7)]
    random.shuffle(num_list)
    print(num_list)

    for num in num_list:
        linked_list.insert(num)
    

    linked_list.print_list()
    