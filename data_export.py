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


if __name__ == "__main__":
    export_data_to_file(2,3,"data/wynik.txt", createList)
