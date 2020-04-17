import random
import time
from lists import Record
from BST import Node


def export_data_to_file(data: int, filename:str, function, head = 0):

    start = time.clock()
    result = function(data, head)
    end = time.clock()

    duration = end - start

    file = open(filename,"a")
    file.write("{0:02f}\n".format(duration))
    file.close()
    return result

def export_data_h_tree(filename, probes):
    file = open(filename, "w")
    file.write("{}\t{}\t{}\n".format("n","h_bst","h_avl"))
    for n in range(1000, 10000, 200):
        h1=0
        h2=0
        for a in range(probes):
            data=generate(n)
            root_bst=create_bst(data)
            lista =[]
            in_order_list(root_bst,lista)
            root_avl=create_bst_from_io_list(lista)
            h1+=find_height(root_bst)
            h2+=find_height(root_avl)
        h1/=probes
        h2/=probes
        file.write("{}\t{}\t{}\n".format(n, h1, h2))
    file.close()
if __name__ == "__main__":
    export_data_to_file(2,3,"data/wynik.txt", createList)
