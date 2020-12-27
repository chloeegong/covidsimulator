import AdjacencyList
import ArrayList
import random
import matplotlib.pyplot as plt
import time


class Covid:

    class Node:
        def __init__(self, i):
            self.state = None
            self.recover = None
            self.index = i

    def __init__(self, interactions):
        self.n = 10000
        self.ALPHA = 0.01
        self.RECOVERY_DAYS = 14
        self.TRANSMISSION_RATE = 0.015
        self.FATALITY_RATE = 0.03
        self.INITIAL_SETTING = 0.01
        self.INTERACTIONS = interactions

        self.CLEAN = 0
        self.INFECTED = 1
        self.DEAD = 2
        self.RECOVERED = 3

        self.Nodes = ArrayList.ArrayList()

        for i in range(self.n):
            self.Nodes.append(self.Node(i))

        for v in self.Nodes:
            if random.uniform(0, 1) < self.INITIAL_SETTING:
                v.state = self.INFECTED
                v.recover = self.RECOVERY_DAYS
            else:
                v.state = self.CLEAN

        self.g = self.getInteractionGraph()

    def getInteractionGraph(self):
        g = AdjacencyList.AdjacencyList(self.n)

        for repeats in range(self.INTERACTIONS):
            for j in range(self.n):
                i = self.Nodes.get(random.randint(0, j))
                if random.uniform(0, 1) < self.ALPHA:
                    g.add_edge(j, i)
                else:
                    ngh = g.out_edges(i.index)
                    if ngh.size() > 0:
                        k = random.choice(ngh)
                        g.add_edge(j, k)
                    else:
                        k = i
                        g.add_edge(j, k)

        for v in self.Nodes:
            v.adj = g.out_edges(v.index)

        return g

    def simulation(self, day: int):
        start_time = time.time()
        day_pl = []
        clean_pl = []
        infected_pl = []
        dead_pl = []
        recover_pl = []

        for x in range(day):
            infected = 0
            dead = 0
            clean = 0
            recover = 0
            for nodes in self.Nodes:
                if nodes.state == self.INFECTED:
                    infected += 1
                elif nodes.state == self.DEAD:
                    dead += 1
                elif nodes.state == self.CLEAN:
                    clean += 1
                else:
                    recover += 1

            day_pl.append(x)
            clean_pl.append(clean)
            infected_pl.append(infected)
            dead_pl.append(dead)
            recover_pl.append(recover)
            print("Day: ", x, "Infected: ", infected, "Dead: ", dead, "Alive: ", clean + recover)

            for v in self.Nodes:
                if v.state == self.INFECTED:
                    ngh = self.g.out_edges(v.index)
                    for w in ngh:
                        if w.state == self.CLEAN and random.uniform(0, 1) < self.TRANSMISSION_RATE:
                            self.Nodes.get(w.index).state = self.INFECTED
                            self.Nodes.get(w.index).recover = self.RECOVERY_DAYS
                    v.recover -= 1
                    if v.recover == 0:
                        if random.uniform(0, 1) < self.FATALITY_RATE:
                            # v.state = self.DEAD
                            v.state = 2
                        else:
                            # v.state = self.RECOVERED
                            v.state = 3

        # creates plot

        # plt.plot(day_pl, clean_pl, 'b')
        plt.plot(day_pl, infected_pl, 'r')
        plt.plot(day_pl, dead_pl, 'k')
        # plt.plot(day_pl, recover_pl, 'g')
        plt.legend(['Infected', 'Dead'], loc='upper right')
        # plt.legend(['Clean', 'Infected', 'Dead', 'Recovered'], loc='upper right')

        plt.suptitle('Covid-19 Simulation')
        plt.xlabel('Days')
        plt.ylabel('People (nodes)')

        elapsed_time = time.time() - start_time

        # footer
        print()
        print(f"Simulation for {day} days completed in {elapsed_time} seconds")

        # view plot
        plt.show()
        plt.clf()
        plt.close()
