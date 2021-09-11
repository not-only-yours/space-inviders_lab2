import GlobalVariables as gv
import numpy
import sys

sys.setrecursionlimit(5000)
# empty = 0
# current = 1
# enemy = 2
# asteroids = 3

Matrix = numpy.full((gv.WIDTH, gv.HEIGHT), 0)


def createStartMatrix():
    for j in range(gv.currPoint[0] - 25, gv.currPoint[0] + 25):
        for k in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
            if 0 < j < len(Matrix) and 0 < k < len(Matrix):
                Matrix[j][k] = 1

    for i in gv.ASTEROIDS:
        for j in range(i.x - 20, i.x + 20):
            for k in range(i.y - 20, i.y + 20):
                if 0 < j < len(Matrix) and 0 < k < len(Matrix):
                    Matrix[j][k] = 3

    for i in gv.ENEMIES:
        for j in range(i.x - 20, i.x + 20):
            for k in range(i.y - 20, i.y + 20):
                if 0 < j < len(Matrix) and 0 < k < len(Matrix):
                    Matrix[j][k] = 2


def dfs():
    # for line in Matrix:
    #     print(*line)
    print(gv.path)
    print(gv.currPoint[0])
    if not gv.End:
        if isThereEnd() or len(gv.path) == 0:
            print(1)
            gv.dfsArrayOfPath.append(Matrix)
            gv.End = True
        elif canGoUp():
            gv.path.append("Up")
            moveUp()
            dfs()
        elif canGoLeft():
            gv.path.append("Left")
            moveLeft()
            dfs()
        elif canGoRight():
            gv.path.append("Right")
            moveRight()
            dfs()
        elif canGoDown():
            gv.path.append("Down")
            moveDown()
            dfs()
        elif gv.path[-1] == "Up":
            gv.path.remove(gv.path[-1])
            baskMoveFromUp()
        elif gv.path[-1] == "Down":
            gv.path.remove(gv.path[-1])
            baskMoveFromDown()
        elif gv.path[-1] == "Left":
            gv.path.remove(gv.path[-1])
            baskMoveFromLeft()
        elif gv.path[-1] == "Right":
            gv.path.remove(gv.path[-1])
            baskMoveFromRight()
        elif gv.path[-1] == "StartPoint":
            gv.path.remove(gv.path[-1])


def moveUp():
    for k in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
        if 0 < gv.currPoint[0] + 26 < len(Matrix) and 0 < k < len(Matrix):
            Matrix[gv.currPoint[0] + 26][k] = 1
    gv.currPoint = [gv.currPoint[0] + 1, gv.currPoint[1]]


def moveDown():
    for k in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
        if 0 < gv.currPoint[0] - 26 < len(Matrix) and 0 < k < len(Matrix):
            Matrix[gv.currPoint[0] - 26][k] = 1
    gv.currPoint = [gv.currPoint[0] - 1, gv.currPoint[1]]


def moveLeft():
    for j in range(gv.currPoint[0] - 25, gv.currPoint[0] + 25):
        if 0 < j < len(Matrix) and 0 < gv.currPoint[1] - 26 < len(Matrix):
            Matrix[j][gv.currPoint[1] - 26] = 1
    gv.currPoint = [gv.currPoint[0], gv.currPoint[1] - 1]


def moveRight():
    for j in range(gv.currPoint[0] - 25, gv.currPoint[0] + 25):
        if 0 < j < len(Matrix) and 0 < gv.currPoint[1] + 26 < len(Matrix):
            Matrix[j][gv.currPoint[1] + 26] = 1
    gv.currPoint = [gv.currPoint[0], gv.currPoint[1] + 1]


def baskMoveFromUp():
    for k in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
        if 0 < gv.currPoint[0] + 26 < len(Matrix) and 0 < k < len(Matrix):
            Matrix[gv.currPoint[0] + 26][k] = 4
    gv.currPoint = [gv.currPoint[0] - 1, gv.currPoint[1]]


def baskMoveFromDown():
    for k in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
        if 0 < gv.currPoint[0] - 26 < len(Matrix) and 0 < k < len(Matrix):
            Matrix[gv.currPoint[0] - 26][k] = 4
    gv.currPoint = [gv.currPoint[0] + 1, gv.currPoint[1]]


def baskMoveFromLeft():
    for j in range(gv.currPoint[0] - 25, gv.currPoint[0] + 25):
        if 0 < j < len(Matrix) and 0 < gv.currPoint[1] - 26 < len(Matrix):
            Matrix[j][gv.currPoint[1] - 26] = 4
    gv.currPoint = [gv.currPoint[0], gv.currPoint[1] + 1]


def baskMoveFromRight():
    for j in range(gv.currPoint[0] - 25, gv.currPoint[0] + 25):
        if 0 < j < len(Matrix) and 0 < gv.currPoint[1] + 26 < len(Matrix):
            Matrix[j][gv.currPoint[1] + 26] = 4
    gv.currPoint = [gv.currPoint[0], gv.currPoint[1] - 1]


def canGoUp():
    for i in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
        if 0 <= gv.currPoint[0] + 26 < 750 and 0 <= gv.currPoint[1] - 25 < 750:
            if Matrix[gv.currPoint[0] + 26][i] == 0:
                return True
    return False


def canGoDown():
    for i in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
        if 0 <= gv.currPoint[0] - 26 < 750 and 0 <= gv.currPoint[1] + 25 < 750:
            if Matrix[gv.currPoint[0] - 26][i] == 0:
                return True
    return False


def canGoLeft():
    for i in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
        if 0 <= gv.currPoint[0] < 750 and 0 <= gv.currPoint[1] + 26 < 750:
            if Matrix[i][gv.currPoint[1] - 26] == 0:
                return True
    return False


def canGoRight():
    for i in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
        if 0 <= gv.currPoint[0] + 26 < 750 and 0 <= gv.currPoint[1] - 25 < 750:
            if Matrix[i][gv.currPoint[1] + 26] == 0:
                return True
    return False


def isThereEnd():
    for i in range(gv.currPoint[1] - 25, gv.currPoint[1] + 25):
        if 0 <= gv.currPoint[0] + 26 < 750 and 0 <= gv.currPoint[1] - 25 < 750:
            if Matrix[gv.currPoint[1] + 26][i] == 2:
                return True
        if 0 <= gv.currPoint[0] - 26 < 750 and 0 <= gv.currPoint[1] + 25 < 750:
            if Matrix[gv.currPoint[1] - 26][i] == 2:
                return True
        if 0 <= gv.currPoint[0] - 26 < 750 and 0 <= gv.currPoint[1] + 25 < 750:
            if Matrix[i][gv.currPoint[0] - 26] == 2:
                return True
        if 0 <= gv.currPoint[0] + 26 < 750 and 0 <= gv.currPoint[1] - 25 < 750:
            if Matrix[gv.currPoint[1] + 26][i] == 2:
                return True
    return False
