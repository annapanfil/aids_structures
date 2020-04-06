class Record:
    def __init__(self, value: int = 0, next = 0):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

def showList(head):
    print("list:", end=' ')
    record = head
    while record.next!= 0:
        print(record.value, end=' ')
        record = record.next
    print(record.value) # ostatni też

def createList(tab): # tworzy listę jednokierunkową, sortując elementy
    head = 0
    for number in tab:
        flag = 0
        if head == 0:
            #pierwszy element
            newrecord = Record(number)
            head = newrecord
        else:
            #znajduje miejsce do wstawienia
            checkrecord = head
            prevrecord = head

            while checkrecord.value<number:
                if checkrecord.next == 0:
                    newrecord = Record(number, 0) # wstawia na koniec listy
                    checkrecord.next = newrecord
                    flag = 1;
                    break;
                prevrecord = checkrecord
                checkrecord = checkrecord.next
            if flag == 0:
                if prevrecord == checkrecord:
                    newrecord = Record(number, prevrecord)   # wstawia na początku listy
                    head = newrecord
                else:
                    newrecord = Record(number, checkrecord) # wstawia między prevrecord a checkrecord
                    prevrecord.next = newrecord
    return head

def searchList(head, tab):
    for wanted in tab:
        checkrecord = head
        while checkrecord.value != wanted:
            # if checkrecord.next=0:    # w zasadzie niepotrzebne, nasze wartości zawsze będą znalezione
            #     print(value, "not found")
            #     break
            checkrecord = checkrecord.next
        # print(wanted, "found")
    return 0

def removeList(head):  # usuwanie listy - od początku
    removeRecord = head
    while removeRecord.next != 0:
        head = removeRecord.next
        del removeRecord
        removeRecord = head
    return 0


# def main():
#     data = [3, 1 ,2, 7, 5, 4, 8, 9]
#     head = createList(data)
#     showList(head)
#     if searchList(head, data)==0: print("Found everything")
#     if removeList(head) == 0: print("Removed everything")
#
# if __name__ == "__main__":
#     main()
