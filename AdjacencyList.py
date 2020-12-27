"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n: int):
        self.n = n
        self.a = np.zeros(n, object)
        for i in range(self.n):
            self.a[i] = ArrayList.ArrayList()
            
    def new_boolean_array(self, n):
        return np.zeros(n, np.bool_)

    def add_edge(self, i: int, j: int):
        # todo
        self.a[i].append(j)

    def remove_edge(self, i: int, j: int):
        # todo
        for k in range(self.a[i].size()):
            if self.a[i].get(k) == j:
                self.a[i].remove(k)
                return

    def has_edge(self, i: int, j: int) -> bool:
        # todo
        for k in range(self.a[i].size()):
            if self.a[i].get(k) == j:
                return True

        return False

    def out_edges(self, i) -> List:
        # todo
        return self.a[i]

    def in_edges(self, i) -> List:
        # todo
        out = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(j, i):
                out.append(j)

        return out

    def bfs(self, r: int):
        # todo
        seen = self.new_boolean_array(self.n)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            print(i, end=" ")
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True

    def dfs(self, r: int):
        # todo
        seen = self.new_boolean_array(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        while s.size() > 0:
            i = s.pop()
            print(i, end=" ")
            seen[i] = True
            ngh = self.out_edges(i)
            for j in range(ngh.size()):
                if seen[ngh.get(j)] == False:
                    s.push(ngh.get(j))
                else:
                    continue

    # traverses bookCatalog
    def bfs2(self, r: int, k: int):
        seen = np.zeros(self.n, np.bool_)
        q = ArrayQueue.ArrayQueue()
        l = []
        q.add(r)
        l.append(r)
        seen[r] = True
        d = 0
        while q.size() > 0 and d < k:
            i = q.remove()
            # print(i, end=" ")
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    l.append(j)
                    seen[j] = True
            d += 1
        return l

    def dfs2(self, r1: int, r2: int):
        d = np.zeros(self.n)
        seen = np.zeros(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r1)
        d[r1] = 0
        while s.size() > 0:
            i = s.pop()
            if seen[i] == 0:
                seen[i] = 1
                ngh = self.out_edges(i)
                for j in ngh:
                    # if seen[j] == False:
                    if seen[j] != 1:
                        s.push(j)
                        d[j] = d[i] + 1
                        if j == r2:
                            return d[j]
        return -1


    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.a[i].__str__())
        return s


# testing
# g = AdjacencyList(6)
# print(g.remove_edge(3, 5))
# print(g.has_edge(3, 5))
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 4)
# g.add_edge(4, 1)
# g.add_edge(1, 3)
# print('predict: true', g.has_edge(1, 2))
# print('predict: false', g.has_edge(1, 2))
# print('in edges, ', g.in_edges(3))
# print('out edges, ', g.out_edges(1))
# print()
# g.bfs(1)
# print()
# g.dfs(1)
# print()
# print(g)

# g.add_edge(0, 1)
# g.add_edge(0, 3)
# g.add_edge(3, 4)
# g.add_edge(4, 5)
# g.add_edge(1, 4)
# g.add_edge(4, 5)
# print(g.dfs2(0, 5))
