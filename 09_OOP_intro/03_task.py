class Queue:
    def __init__(self, fifo = [], lifo = []):
        self.fifo = fifo
        self.lifo = lifo


    def show(self):
        print('Queue --->', self.fifo)

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self,item):
        self.fifo.append(item)

    def get(self):
        return self.fifo.pop(0)

    def get_last(self):
        return self.fifo.pop()



def main():
    fifo_1 = Queue([3,2,7,6,'txt'])
    lifo = Queue([3,2,42,3,'txt'])
    lifo.show()
    lifo.put('Adam')
    lifo.show()
    lifo.get_last()
    lifo.show()
    # fifo_1.show()
    # fifo_1.put('Rita')
    # fifo_1.show()
    # x = fifo_1.get()
    # print('Extracted --->', x)
    # fifo_1.show()
    # x2 = fifo_1.get_last()
    # fifo_1.show()



if __name__ == '__main__':
    main()
