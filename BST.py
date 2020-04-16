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
            if root.left_node is None:
                root.left_node = node
            else:
                binary_insert(root.left_node, node)
        else:
            if root.right_node is None:
                root.right_node = node
            else:
                binary_insert(root.right_node, node)


def search_tree(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search_tree(root.left_node, value)
    else:
        return search_tree(root.right_node, value)

def search_bst(data, root):
    for i in data:
        search_tree (root, i)
    return 0


def in_order_print(root):
    if root:
        in_order_print(root.left_node)
        print(root.value,end=" ")
        in_order_print(root.right_node)

def pre_order_print(root):
    if root:
        print(root.value,end=" ")
        pre_order_print(root.left_node)
        pre_order_print(root.right_node)


def post_order_print(root):
    if root:
        post_order_print(root.left_node)
        post_order_print(root.right_node)
        print(root.value,end=" ")


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

def create_bst(data, root = None):
    root = insert_to_tree(None, data[0])
    for i in data[1:]:
        insert_to_tree(root, i)
    return root

def remove_bst(data, root):
    for i in data[::-1]:
        delete_last_node(root, i)
    return 0


def find_height(root):
    if root is None:
        return 0
    else:
        left_height = find_height(root.left_node)
        right_height = find_height(root.right_node)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

def find_min_value(root):
    temp_node = root
    while temp_node.left_node is not None:
        temp_node = temp_node.left_node
    return temp_node.value

def find_max_value(root):
    temp_node = root
    while temp_node.right_node is not None:
        temp_node = temp_node.right_node
    return temp_node.value

def in_order_list(root,io_list):
    if not root:
        return
    in_order_list(root.left_node,io_list)
    io_list.append(root.value)
    in_order_list(root.right_node,io_list)


def create_bst_from_io_list(io_list):
    if not io_list:
        return None
    m = int(len(io_list) / 2)
    root = Node(io_list[m])
    root.left_node = create_bst_from_io_list(io_list[:m])
    root.right_node = create_bst_from_io_list(io_list[m + 1:])
    return root

if __name__ == "__main__":
    export_data_to_file(2,3,"data/wynik.txt", createList)
    shuffled_list = generate_unordered_list(10, 0, 22)
    print(shuffled_list)
    root = insert_to_tree(None, shuffled_list[0])

    for i in shuffled_list[1:]:
        insert_to_tree(root, i)
    print(find_height(root))
    lista =[]
    in_order_list(root,lista)
    print(lista)
    root_avl=create_bst_from_io_list(lista)
    print(find_height(root_avl))

    for i in shuffled_list[::-1]:
        print("--------")
        delete_last_node(root, i)
