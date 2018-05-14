import numpy as np
import matplotlib.pyplot as plt
import random
import pylab
import time
statues = ['road', 'passenger', 'cargo', 'building-1', 'building-2', 'building-3', 'others']
size = 100


class Cell:
    statue = 0
    time_cnt = 0

    def __init__(self, statue):
        self.statue = statue


class CellMap:
    Map = []
    size = 100

    def __init__(self, size):
        self.size = size
        for i in range(0, size):
            self.Map.append([])
            for j in range(0, size):
                self.Map[i].append(Cell(7))

    def init_shahe_road(self):
        for i in range(0, size):
            for j in range(69, 72):
                self.Map[i][j].statue = 0
        for i in range(47, 50):
            for j in range(0, size):
                self.Map[i][j].statue = 0
        for i in range(25, 47):
            for j in range(89, 91):
                self.Map[i][j].statue = 0
        for i in range(23, 25):
            for j in range(72, size):
                self.Map[i][j].statue = 0
        for i in range(23, 50):
            for j in range(17, 19):
                self.Map[i][j].statue = 0
        for i in range(23, 25):
            for j in range(19, 69):
                self.Map[i][j].statue = 0
        for i in range(50, 76):
            for j in range(37, 70):
                self.Map[i][j].statue = 0

    def init_shahe_building1(self):
        for i in range(25, 47):
            for j in range(72, 89):
                self.Map[i][j].statue = 3
        '''building the road'''
        for i in range(36,37):
            for j in range(72,89):
                self.Map[i][j].statue = 0
        for i in range(25, 47):
            for j in range(80,81):
                self.Map[i][j].statue = 0

    def init_shahe_building2(self):
        for i in range(25, 47):
            for j in range(91, size):
                self.Map[i][j].statue = 4

    def init_shahe_building3(self):
        for i in range(50, 74):
            for j in range(39, 69):
                self.Map[i][j].statue = 5
        for i in range(25, 47):
            for j in range(19, 69):
                self.Map[i][j].statue = 5

        for i in range(50, 82):
            for j in range(72, 95):
                self.Map[i][j].statue = 5

        for i in range(58, 59):
            for j in range(59, 90):
                self.Map[i][j].statue = 0

        for i in range(64, 65):
            for j in range(59, 85):
                self.Map[i][j].statue = 0
        for i in range(50, 74):
            for j in range(58, 59):
                self.Map[i][j].statue = 0
        for i in range(66, 74):
            for j in range(49, 58):
                self.Map[i][j].statue = 0


    def init_to_shahe(self):
        self.init_shahe_road()
        self.init_shahe_building1()
        self.init_shahe_building2()
        self.init_shahe_building3()

    def neighbour(self, x:int, y:int):
        res = []
        if x == 0:
            if y == 0:
                res.append(self.Map[0][1])
                res.append(self.Map[1][0])
                res.append(self.Map[1][1])
                return res
            elif y == size -1:
                res.append(self.Map[0][size-2])
                res.append(self.Map[1][size-1])
                res.append(self.Map[1][size-2])
                return res
            else:
                res.append(self.Map[0][y-1])
                res.append(self.Map[0][y+1])
                res.append(self.Map[1][y-1])
                res.append(self.Map[1][y+1])
                res.append(self.Map[1][y])
                return res
        elif x == size-1:
            if y == 0:
                res.append(self.Map[size-2][0])
                res.append(self.Map[size-1][1])
                res.append(self.Map[size-2][1])
                return res
            elif y == size-1:
                res.append(self.Map[size-2][size-1])
                res.append(self.Map[size-1][size-2])
                res.append(self.Map[size-2][size-2])
                return res
            else:
                res.append(self.Map[size-1][y-1])
                res.append(self.Map[size-1][y+1])
                res.append(self.Map[size-2][y-1])
                res.append(self.Map[size-2][y])
                res.append(self.Map[size-2][y+1])
        else:
            if y == 0:
                res.append(self.Map[x-1][y])
                res.append(self.Map[x+1][y])
                res.append(self.Map[x-1][y+1])
                res.append(self.Map[x][y+1])
                res.append(self.Map[x+1][y+1])
                return res
            elif y == size-1:
                res.append(self.Map[x-1][y])
                res.append(self.Map[x+1][y])
                res.append(self.Map[x-1][y-1])
                res.append(self.Map[x][y-1])
                res.append(self.Map[x+1][y-1])
                return res
            else:
                res.append(self.Map[x-1][y])
                res.append(self.Map[x-1][y+1])
                res.append(self.Map[x-1][y-1])
                res.append(self.Map[x][y-1])
                res.append(self.Map[x][y+1])
                res.append(self.Map[x+1][y-1])
                res.append(self.Map[x+1][y])
                res.append(self.Map[x+1][y+1])
                return res


    def show_passenger(self, time):
        statue_map = np.empty([size, size], dtype=int)
        for i in range(size):
            for j in range(size):
                try:
                    statue_map[i][j] = self.Map[i][j].statue
                except:
                    print('i:', i)
                    print('j:', j)
                    print(type(self.Map[i][j]))
        plt.title('Now is '+str(time)+':00')
        plt.imshow(statue_map)
        plt.savefig('results/' + str(time)+':00.png')

    def passenger_rule(self, time):
        p1 = 0.02
        p2 = 0.02
        p3 = 0.02
        p4 = 0.4
        duration = 2

        if time in range(5, 8):
            '''

                p1 refers to the possibility people get out of the dormitory,
                p2 refers to the possibility people get out of the canteen,
                p3 refers to the possibility people get out of the teaching-building and laboratory.
                During 6.a.m and 8.a.m ,students will get out from the dormitory, so
                p1 will get dramatically big.
                Also a small part of students will have breakfast which contributes to
                p2
                '''
            p1 = 0.5 - (time-6)*0.1
            p2 = 0.3 - (time-6)*0.1
            p3 = 0.05*(time-6)
            p4 = 0.5 #the possibility people move
            duration = 2 ##people at most stay outside for 2 hours


        elif time in range(8, 12):
            '''
            During the time of 9.a.m to 11.a.m, people tends to gather around
            building-3
            '''

            p1 = 0.05
            p2 = 0.5 + (time - 8) * 0.1
            p3 = 0.7
            p4 = 0.5
            duration = 2
        elif time in range(12, 14):
            '''
            people tends to get out of the canteen and dormitory,
            
            '''
            p1 = 0.5 - (time-11)*0.2
            p2 = 0.4 - (time-12)*0.2
            p3 = 0.5 - (time -11)*0.1
            p4 = 0.5
            duration = 2
            '''
        elif time in range(0, 5) or time in range(22, 24):
            p_delete = 0.2
            seed = random.random()
            print(seed)
            for i in range(size):
                for j in range(size):
                    if seed < p_delete and self.Map[i][j].statue == 1:
                        print('i:', i)
                        print('j:', j)
                        self.Map[i][j].statue = 0
                        self.Map[i][j].cnt = 0
            '''

        elif time in range(17, 22):
            '''
            people get back to dormitory
            '''
            p1 = 0.1
            p2 = 0.1
            p3 = 0.5 - (time-16)*0.08
            p4 = 0.5
            duration = 2
        else:
            '''
            other time the people very few
            '''
            p1 = 0.02
            p2 = 0.02
            p3 = 0.02
            p4 = 0.4
            duration = 2


        for i in range(0, size):
            for j in range(0, size):
                res = self.neighbour(i, j)
                seed = random.random()
                p = 0
                #people get out from building-1
                if self.Map[i][j].statue == 3:
                    p = p1
                #people get out from bulding-2
                elif self.Map[i][j].statue == 4:
                    p = p2
                #people get out from building-3
                elif self.Map[i][j].statue == 5:
                    p = p3

                if p > 0:
                    for cell in res:
                        if cell.statue == 0:
                            if seed < p1:
                                cell.statue = 1
                                cell.time_cnt += 1
        for i in range(size):
            for j in range(size):
                if self.Map[i][j].statue == 1:
                    if self.Map[i][j].time_cnt >= duration:
                        self.Map[i][j].statue = 0
                        self.Map[i][j].time_cnt = 0
                    else:
                        seed = random.random()
                        res = self.neighbour(i, j)
                        target_list = []
                        for cell in res:
                            if cell.statue == 0:
                                target_list.append(cell)
                        if len(target_list)>0:
                            target = random.choice(target_list)
                            if seed < p4:
                                target.statue = 1
                                target.time_cnt = self.Map[i][j].time_cnt
                                self.Map[i][j].statue = 0
                                self.Map[i][j].time_cnt = 0












if __name__ == '__main__':
    game = CellMap(size)
    game.init_to_shahe()
    #plt.ion()
    for i in range(0, 25):
        game.passenger_rule(i)
        game.show_passenger(i)
        #time.sleep(0.5)
        plt.show()
    #plt.ioff()






