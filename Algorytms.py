import GlobalVariables as gv
import numpy

matrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
visited = numpy.full((int(750 / 50), int(750 / 50)), 0)
enemyArray = []
startGame = False
max = True


def findEnemies():
    buff = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 2:
                buff.append([i, j])
    return buff


enemies = findEnemies()


class Node():
    point = 0
    nodes = []
    coords = []
    father = []

    def __init__(self, point=0, coords=None, nodes=None):
        self.point = point
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
        if coords is None:
            self.coords = []
        else:
            self.coords = coords

    def addNode(self, el):
        self.nodes.append(el)

    def setPoint(self, num):
        self.point = num


def emtyVisitMatrix():
    for i in range(0, len(visited)):
        for j in range(0, len(visited[i])):
            visited[i][j] = 0


def getStartCoords():
    if startGame and gv.GOOD_SHIP:
        return [int(gv.GOOD_SHIP.y / 50), int(gv.GOOD_SHIP.x / 50)]
    else:
        return [13, 7]


def getNearNodes(coords=None):
    ans = []
    buff = []
    if coords is None:
        coords = getStartCoords()
    buff.append(coords)
    for i in buff:
        if 0 <= i[0] + 1 < len(matrix) and 0 <= i[1] + 1 < len(matrix) and visited[i[0] + 1][i[1] + 1] != 1:
            ans.append([i[0] + 1, i[1] + 1])
        if 0 <= i[0] - 1 < len(matrix) and 0 <= i[1] - 1 < len(matrix) and visited[i[0] - 1][i[1] - 1] != 1:
            ans.append([i[0] - 1, i[1] - 1])
        if 0 <= i[0] + 1 < len(matrix) and 0 <= i[1] - 1 < len(matrix) and visited[i[0] + 1][i[1] - 1] != 1:
            ans.append([i[0] + 1, i[1] - 1])
        if 0 <= i[0] - 1 < len(matrix) and 0 <= i[1] + 1 < len(matrix) and visited[i[0] - 1][i[1] + 1] != 1:
            ans.append([i[0] - 1, i[1] + 1])
        if 0 <= i[0] < len(matrix) and 0 <= i[1] + 1 < len(matrix) and visited[i[0]][i[1] + 1] != 1:
            ans.append([i[0], i[1] + 1])
        if 0 <= i[0] + 1 < len(matrix) and 0 <= i[1] < len(matrix) and visited[i[0] + 1][i[1]] != 1:
            ans.append([i[0] + 1, i[1]])
        if 0 <= i[0] < len(matrix) and 0 <= i[1] - 1 < len(matrix) and visited[i[0]][i[1] - 1] != 1:
            ans.append([i[0], i[1] - 1])
        if 0 <= i[0] - 1 < len(matrix) and 0 <= i[1] < len(matrix) and visited[i[0] - 1][i[1]] != 1:
            ans.append([i[0] - 1, i[1]])
        if 0 <= i[0] < len(matrix) and 0 <= i[1] < len(matrix) and visited[i[0]][i[1]] != 1:
            ans.append([i[0], i[1]])
        for element in buff:
            visited[element[0]][element[1]] = 1
            if element in ans:
                ans.remove(element)
        buffer = []
        for i in ans:
            buffer.append(Node(matrix[i[0]][i[1]], [i[0], i[1]]))
        return buffer


class Tree:
    startNode = Node(1, getStartCoords(), getNearNodes())
    current = startNode
    before = []

    def createTree(self):
        for i in self.current.nodes:
            self.before = self.current
            self.current.father = self.before
            self.current = i
            self.current.nodes = getNearNodes(self.current.coords)
            if self.current.nodes:
                self.createTree(self)

    def isUnvisited(self):
        if self.current.nodes:
            for i in self.current.nodes:
                if visited[i.coords[0]][i.coords[1]] == 1:
                    return False
        return True

    def setPriceInTree(self):
        global max
        checker = True
        if self.current.nodes and self.isUnvisited(self):
            for i in self.current.nodes:
                if matrix[i.coords[0]][i.coords[1]] >= matrix[self.current.coords[0]][self.current.coords[1]] + \
                        self.current.coords[0] * self.current.coords[1]:
                    matrix[i.coords[0]][i.coords[1]] = 0
                    checker = False
                if not [i.coords[0], i.coords[1]] in enemies and checker:
                    if max and matrix[i.coords[0]][i.coords[1]] != 2:
                        matrix[i.coords[0]][i.coords[1]] += (
                                matrix[self.current.coords[0]][self.current.coords[1]] + self.current.coords[0] *
                                self.current.coords[1])
                    elif matrix[i.coords[0]][i.coords[1]] != 2:
                        matrix[i.coords[0]][i.coords[1]] += (
                                matrix[self.current.coords[0]][self.current.coords[1]] + self.current.coords[0] *
                                self.current.coords[1])
                if visited[i.coords[0]][i.coords[1]] != 1:
                    self.before = self.current
                    self.current = i
                    visited[self.current.coords[0]][self.current.coords[1]] = 1
                    if max:
                        max = False
                    else:
                        max = True
                    self.setPriceInTree(self)
        else:
            if max:
                max = False
            else:
                max = True
            self.current = self.before
            checker = True
            # print(self.current.point)

            # print(self.current.point)


def createVisitMatrix(matrix):
    global enemyArray
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                enemyArray.append([i, j])
    if enemyArray:
        enemyArray = [i for n, i in enumerate(enemyArray) if i not in enemyArray[:n]]


def emptyMatrix(matr, cur):
    for i in range(0, len(matr)):
        for j in range(0, len(matr[i])):
            if not matr[i][j] == 0:
                matr[i][j] = 0
    matr[cur[0]][cur[1]] = 1
    # for i in matr:
    #     print(*i)


def fillMatrix(matrix):
    for i in gv.ENEMIES:
        if 0 < int(i.y / 50) < 15 and 0 < int(i.x / 50) < 15:
            matrix[int(i.y / 50)][int(i.x / 50)] = 2
    for i in gv.ASTEROIDS:
        if 0 < int(i.y / 50) < 15 and 0 < int(i.x / 50) < 15:
            matrix[int(i.y / 50)][int(i.x / 50)] = 3


def moveEnemy():
    global arrayOfPath
    matrix[int(gv.GOOD_SHIP.y / 50)][int(gv.GOOD_SHIP.x / 50)] = 1
    for i in gv.ENEMIES[1:]:
        if gv.RANDOM_LIB.randint(1, 100) == 1 and 600 > i.x > 50:
            buf = gv.RANDOM_LIB.choice([1, 0])
            if buf == 0 and i.x + 50 < 600:
                i.x += 50
            elif i.x - 50 > 50:
                i.x -= 50
    if gv.ENEMIES:
        gv.ENEMIES[0].x = gv.GOOD_SHIP.x
        if gv.ENEMIES[0].x == gv.GOOD_SHIP.x and 600 > gv.ENEMIES[0].x > 50:
            if [int(gv.ENEMIES[0].y / 50), int(gv.ENEMIES[0].x / 50)] in enemyArray:
                enemyArray.remove([int(gv.ENEMIES[0].y / 50), int(gv.ENEMIES[0].x / 50)])
            if [int(gv.ENEMIES[0].x / 50), int(gv.ENEMIES[0].y / 50)] in enemyArray:
                enemyArray.remove([int(gv.ENEMIES[0].x / 50), int(gv.ENEMIES[0].y / 50)])

    if gv.GOOD_SHIP:
        nextTurn = 0
        leftval = 0
        sum = 0
        endl = True
        value = matrix[int(gv.GOOD_SHIP.y / 50)][int(gv.GOOD_SHIP.x / 50)]
        for i in range(0, len(matrix)):
            if matrix[int(gv.GOOD_SHIP.y / 50)][i] != 1 and endl:
                leftval += matrix[int(gv.GOOD_SHIP.y / 50)][i]
                sum = leftval
            else:
                endl = False
                sum += matrix[int(gv.GOOD_SHIP.y / 50)][i]
        if int(gv.GOOD_SHIP.x / 50) - 1 > 0:
            matrix[int(gv.GOOD_SHIP.y / 50)][int(gv.GOOD_SHIP.x / 50) - 1] = leftval
        if int(gv.GOOD_SHIP.x / 50) + 1 < len(matrix) - 1:
            matrix[int(gv.GOOD_SHIP.y / 50)][int(gv.GOOD_SHIP.x / 50) + 1] = sum - leftval
        if 0 <= gv.GOOD_SHIP.x / 50 + 1 < len(matrix) and 0 <= gv.GOOD_SHIP.y / 50 < len(matrix) and \
                matrix[int(gv.GOOD_SHIP.y / 50)][int(gv.GOOD_SHIP.x / 50 + 1)] > value:
            nextTurn = 1
        if 0 <= gv.GOOD_SHIP.x / 50 - 1 < len(matrix) and 0 <= gv.GOOD_SHIP.y / 50 < len(matrix) and \
                matrix[int(gv.GOOD_SHIP.y / 50)][int(gv.GOOD_SHIP.x / 50 - 1)] > value:
            nextTurn = 2
        if nextTurn != 0:
            if nextTurn == 1:
                gv.GOOD_SHIP.x = (gv.GOOD_SHIP.x / 50 + 1) * 50
            else:
                gv.GOOD_SHIP.x = (gv.GOOD_SHIP.x / 50 - 1) * 50
        if gv.ENEMIES and gv.RANDOM_LIB.randrange(1, 60) == 1:
            print(gv.GOOD_SHIP.x, " ", gv.ENEMIES[0].x)
            try:
                gv.GOOD_SHIP.x = gv.ENEMIES[1].x
            except:
                print(len(gv.ENEMIES))
    arrayOfPath = []
    createVisitMatrix(matrix)
    fillMatrix(matrix)
