import random


def generate_unordered_list(number, start=0, end=100):
    step = int((end - start) / number)
    output = [x for x in range(start, end + 1, step)]
    random.shuffle(output)
    return output


class Node:
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def add_right_node(self, right_node):
        self.right_node = right_node

    def add_right_node(self, left_node):
        self.left_node = left_node


def insert_to_tree(root, value):
    if root is None:
        root = Node(value)
        return root
    if value < root.value:
        root.left_node = insert_to_tree(root.left_node, value)
    else:
        root.right_node = insert_to_tree(root.right_node, value)
    return root


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)


def search_tree(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left_nod, value)
    else:
        return search(root.right_node, value)


def in_order_print(root):
    if not root:
        return
    in_order_print(root.left_node)
    print(root.value)
    in_order_print(root.right_node)


def pre_order_print(root):
    if not root:
        return
    print(root.value)
    pre_order_print(root.left_node)
    pre_order_print(root.right_node)


def delete_last_node(root, value):
    if root.value == value:
        root.value = None
        return
    if value < root.value:
        if value == root.left_node.value:
            root.left_node = None
        else:
            delete_last_node(root.left_node, value)
    if value > root.value:
        if value == root.right_node.value:
            root.right_node = None
        else:
            delete_last_node(root.right_node, value)


shuffled_list = generate_unordered_list(5, 0, 15)
print(shuffled_list)
root = insert_to_tree(None, shuffled_list[0])
for i in shuffled_list[1:]:
    insert_to_tree(root, i)
in_order_print(root)
for i in shuffled_list[::-1]:
    print("--------")
    delete_last_node(root, i)
    in_order_print(root)
