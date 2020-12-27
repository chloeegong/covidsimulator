import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):
    # FIFO first in first out
    def __init__(self):
        self.n = 0  # size of arr
        self.j = 0  # ind of first element in arr
        self.a = self.new_array(1)

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, np.object)

    def resize(self):
        b = self.new_array(max(1, 2 * self.n))

        for k in range(self.n):
            b[k] = self.a[(self.j + k) % len(self.a)]

        self.a = b
        self.j = 0
        return self.a

    def add(self, x: np.object):
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if (self.n + 1) > len(self.a):
            self.resize()

        self.a[(self.j + self.n) % len(self.a)] = x

        self.n += 1
        return True

    def remove(self) -> np.object:
        '''
            remove the first element in the queue
        '''
        # check for valid ind
        if self.n == 0:
            raise IndexError()

        # x = self.a[(self.j + 1) % len(self.a)]
        x = self.a[self.j]

        self.j = (self.j + 1) % len(self.a)
        self.n -= 1

        if len(self.a) >= (3 * self.n):
            self.resize()

        return x

    def size(self):
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x

# testing
# def main():
#     queue = ArrayQueue()
#
#     for i in range(5):
#         queue.add(i)
#
#     print('current arr  ', queue)
#     queue.remove()
#     queue.remove()
#     queue.remove()
#     print('final ', queue)
#
# if __name__ == "__main__":
#     main()
