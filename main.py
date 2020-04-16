from BST import *
from data_export import *
from lists import *

def generate(n: int):
    #losuje n niepowtarzalnych liczb z zakresu 0 do 1,5n
    data = random.sample(range(int(1.5*n)), n)
    return data

def main():
    filenames = ["data/listCreate.txt", "data/listSearch.txt", "data/listRemove.txt", "data/BSTcreate.txt", "data/BSTsearch.txt", "data/BSTremove.txt" ]
    for n in range(1000, 10000, 200):
        data = generate(n)
        head = export_data_to_file(data, filenames[0], createList)
        export_data_to_file(data, filenames[1], searchList, head)
        export_data_to_file(data, filenames[2], removeList, head)
        root = export_data_to_file(data, filenames[3], create_bst)
        export_data_to_file(data, filenames[4], search_bst, root)
        export_data_to_file(data, filenames[5], remove_bst, root)

def test(filename):
    input_file = open(filename, "r")
    content=input_file.readlines()
    data = [ int(x) for x in content]
    print(data)
    root = create_bst(data)
    print("height = ", find_height(root))
    print("Leftmost node = ",find_min_value(root))
    print("In order:")
    in_order_print(root)
    print("\nPre-order: ")
    pre_order_print(root)
    print("\nPost-order: ")
    post_order_print(root)

if __name__ == '__main__':
    #main()
    test("data/example.txt")
