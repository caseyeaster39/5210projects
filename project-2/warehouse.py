import math
import random

from project_utils import path_trace


# WAREHOUSE MAIN FLOOR
class Node:
    def __init__(self, num, is_parent, left=None, right=None):
        # Warehouse info
        self.num = num                                                  # Reference number
        self.depth = math.floor(math.log2(num))                         # Depth
        self.root_path = path_trace(num)                                # Path from node to root

        # Children edges (if any) in tuple form (node, weight)
        self.is_parent = is_parent                                      # Has children
        self.left = left
        self.right = right

        # Parent node (except for root)
        self.parent = num // 2 if num > 1 else None                     # Parent node


def floor_gen():
    node_list = list()

    # Node list hard-coded in due to nature of tree.
    node_list.append(Node(1, is_parent=True, left=(2, 20), right=(3, 20)))
    node_list.append(Node(2, is_parent=True, left=(4, 20), right=(5, 30)))
    node_list.append(Node(3, is_parent=True, left=(6, 40), right=(7, 10)))
    node_list.append(Node(4, is_parent=True, left=(8, 10), right=(9, 20)))
    node_list.append(Node(5, is_parent=True, left=(10, 30), right=(11, 20)))
    node_list.append(Node(6, is_parent=True, left=(12, 30), right=(13, 20)))
    node_list.append(Node(7, is_parent=True, left=(14, 20), right=(15, 20)))
    node_list.append(Node(8, is_parent=False))
    node_list.append(Node(9, is_parent=False))
    node_list.append(Node(10, is_parent=False))
    node_list.append(Node(11, is_parent=False))
    node_list.append(Node(12, is_parent=False))
    node_list.append(Node(13, is_parent=False))
    node_list.append(Node(14, is_parent=False))
    node_list.append(Node(15, is_parent=False))

    return node_list


class Warehouse:
    def __init__(self):
        self.node_list = floor_gen()                                    # Generate Warehouse tree


# WAREHOUSE DIVISION
def generate_tree(max_node=63):
    node_list = list()                                                  # Division generator
    i = 1
    while i <= max_node:
        if i <= max_node // 2:                                          # Nodes with children
            left_child = (i * 2, 1)                                     # Generate left child
            right_child = (i * 2 + 1, 1)                                # Generate right child
            node_list.append(Node(i, True, left_child, right_child))    # Create Node based on info and add to list
        else:
            node_list.append(Node(i, False))                            # Create a leaf Node and add to list
        i += 1
    max_depth = math.floor(math.log2(max_node))                         # Leaf depth
    return node_list, max_depth


class Division:
    def __init__(self):
        self.node_list, self.max_depth = generate_tree()                # Generate Division tree


# ORDER GENERATION
class Order:
    def __init__(self, rand=True, shelves=None, div=None):
        if rand:                                                        # Random generator if rand
            self.shelves = random.sample(range(1, 63), random.randint(1, 3))
            self.div = random.randint(1, 15)
        else:                                                           # Pass in parameters if not rand
            self.shelves = shelves
            self.div = div
