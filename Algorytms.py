import GlobalVariables as gv
import numpy

# empty = 0
# current = 1
# enemy = 2
# asteroids = 3

matrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
lenMatrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
pointToResp = [600, 350]
path = []
numofEnemy = 9
startPoint = [13, 7]
curr = [13, 7]
enemyArray = []
arrayOfPath = []

def createVisitMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                enemyArray.append([i, j])

def emptyMatrix(matr, cur):
    global curr
    for i in range(0, len(matr) - 1):
        for j in range(0, len(matr[i]) - 1):
            if not matr[i][j] == 0:
                matr[i][j] = 0
    matr[cur[0]][cur[1]] = 1
    # for i in matr:
    #     print(*i)
#TODO: add baricades(3)

def lenToFromPointtoPoint(cur, startPoiint):
    distance = 0
    if cur[0] > startPoiint[0]:
        distance += cur[0] - startPoiint[0]
    else:
        distance += startPoiint[0] - cur[0]
    if cur[1] > startPoiint[1]:
        distance += cur[1] - startPoiint[1]
    else:
        distance += startPoiint[1] - cur[1]
    return distance


def lenFinal(curr):
    return lenToFromPointtoPoint(curr, startPoint) + lenToFromPointtoPoint(curr, enemyArray[0]) * 10


# print(lenToFromPointtoPoint([12, 5], [1, 7]))
# print(enemyArray)


def isEnemyClose(cur):
    if lenMatrix[cur[0] + 1][cur[1] + 1] == -1:
        return True
    elif lenMatrix[cur[0] - 1][cur[1] - 1] == -1:
        return True
    elif lenMatrix[cur[0] + 1][cur[1] - 1] == -1:
        return True
    elif lenMatrix[cur[0] - 1][cur[1] + 1] == -1:
        return True
    elif lenMatrix[cur[0]][cur[1] + 1] == -1:
        return True
    elif lenMatrix[cur[0] + 1][cur[1]] == -1:
        return True
    elif lenMatrix[cur[0]][cur[1] - 1] == -1:
        return True
    elif lenMatrix[cur[0] - 1][cur[1]] == -1:
        return True
    else:
        return False


def markPoints(cur):
    if 0 < cur[0] + 1 < len(lenMatrix) and 0 < cur[1] + 1 < len(lenMatrix) and not lenMatrix[cur[0] + 1][cur[1] + 1] == 999:
        lenMatrix[cur[0] + 1][cur[1] + 1] = lenFinal([cur[0] + 1, cur[1] + 1])
    if 0 < cur[0] - 1 < len(lenMatrix) and 0 < cur[1] - 1 < len(lenMatrix) and not lenMatrix[cur[0] - 1][cur[1] - 1] == 999:
        lenMatrix[cur[0] - 1][cur[1] - 1] = lenFinal([cur[0] - 1, cur[1] - 1])
    if 0 < cur[0] + 1 < len(lenMatrix) and 0 < cur[1] - 1 < len(lenMatrix) and not lenMatrix[cur[0] + 1][cur[1] - 1] == 999:
        lenMatrix[cur[0] + 1][cur[1] - 1] = lenFinal([cur[0] + 1, cur[1] - 1])
    if 0 < cur[0] - 1 < len(lenMatrix) and 0 < cur[1] + 1 < len(lenMatrix) and not lenMatrix[cur[0] - 1][cur[1] + 1] == 999:
        lenMatrix[cur[0] - 1][cur[1] + 1] = lenFinal([cur[0] - 1, cur[1] + 1])
    if 0 < cur[0] < len(lenMatrix) and 0 < cur[1] + 1 < len(lenMatrix) and not lenMatrix[cur[0]][cur[1] + 1] == 999:
        lenMatrix[cur[0]][cur[1] + 1] = lenFinal([cur[0], cur[1] + 1])
    if 0 < cur[0] + 1 < len(lenMatrix) and 0 < cur[1] < len(lenMatrix) and not lenMatrix[cur[0] + 1][cur[1]] == 999:
        lenMatrix[cur[0] + 1][cur[1]] = lenFinal([cur[0] + 1, cur[1]])
    if 0 < cur[0] < len(lenMatrix) and 0 < cur[1] - 1 < len(lenMatrix) and not lenMatrix[cur[0]][cur[1] - 1] == 999:
        lenMatrix[cur[0]][cur[1] - 1] = lenFinal([cur[0], cur[1] - 1])
    if 0 < cur[0] - 1 < len(lenMatrix) and 0 < cur[1] < len(lenMatrix) and not lenMatrix[cur[0] - 1][cur[1]] == 999:
        lenMatrix[cur[0] - 1][cur[1]] = lenFinal([cur[0] - 1, cur[1]])
    if 0 < cur[0] < len(lenMatrix) and 0 < cur[1] < len(lenMatrix) and not lenMatrix[cur[0]][cur[1]] == 999:
        lenMatrix[cur[0]][cur[1]] = lenFinal([cur[0], cur[1]])

def moveEnemy():
    for i in gv.ENEMIES:
        if i.x == gv.GOOD_SHIP.x and 700 > i.x > 50:
            buf = gv.RANDOM_LIB.randrange(0, 1)
            if buf == 0:
                i.x += 50
            else:
                i.x -= 50

def getCoordsOfSmallest(matrix):
    value = 9999
    currentVay = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if not matrix[i][j] == -1 and matrix[i][j] > 0:
                if matrix[i][j] < value:
                    value = matrix[i][j]
                    currentVay = [i, j]
    return currentVay


def astar(curr):
    lenMatrix[enemyArray[0][0]][enemyArray[0][1]] = -1
    if not isEnemyClose(curr):
        markPoints(curr)
        path.append(curr)
        curr = getCoordsOfSmallest(lenMatrix)
        #print(curr)
        astar(curr)

def markThree(matr):
    for i in range(0, len(matr)):
        for j in range(0, len(matr[i])):
            if matr[i][j] == 3:
                lenMatrix[i][j] = 999


def fillMatrix(matrix):
    for i in gv.ENEMIES:
        if 0 < int(i.y / 50) < 15 and 0 < int(i.x / 50) < 15:
            matrix[int(i.y / 50)][int(i.x / 50)] = 2
    for i in gv.ASTEROIDS:
        if 0 < int(i.y / 50) < 15 and 0 < int(i.x / 50) < 15:
            matrix[int(i.y / 50)][int(i.x / 50)] = 3