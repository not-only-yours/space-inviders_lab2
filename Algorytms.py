import GlobalVariables as gv
import numpy

# empty = 0
# current = 1
# enemy = 2
# asteroids = 3

matrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
visitMatrix = numpy.full((int(750 / 50), int(750 / 50)), 0)
path = [[14, 6]]
numofEnemy = 1 # TODO: get num from matrix
arrOfPath = []
listOfVisited = [[14, 6]]
arrOfList = []
arrBeforePath = []



def createStartMatrix():
    for i in gv.ASTEROIDS:
        for j in range(int((i.x - 20) / 50), int((i.x + 20) / 50)):
            for k in range(int((i.y - 20) / 50), int((i.y + 20) / 50)):
                if 0 < j < len(matrix) and 0 < k < len(matrix):
                    matrix[j][k] = 3
                    gv.VisitMatrix[j][k] = 1
    for i in gv.ENEMIES:
        for j in range(int((i.x - 20) / 50), int((i.x + 20) / 50)):
            for k in range(int((i.y - 20) / 50), int((i.y + 20) / 50)):
                if 0 < j < len(matrix) and 0 < k < len(matrix):
                    matrix[j][k] = 2
                    gv.VisitMatrix[j][k] = 1

    matrix[0][0] = 0
    matrix[int(gv.currPoint[1])][int(gv.currPoint[0])] = 1
    gv.VisitMatrix[int(gv.currPoint[1])][int(gv.currPoint[0])] = 1




def createVisitMatrix(matrix, visitMatrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                visitMatrix[i][j] = 1
            else:
                visitMatrix[i][j] = 0


def dfs(matrix, visitMatrix, curX=path[-1][0], curY=path[-1][1]):
    # print(path)
    # for i in visitMatrix:
    #     print(*i)
    visitMatrix[curX][curY] = 1
    while len(path) > 0:
        curX = path[-1][0]
        curY = path[-1][1]
        if curX + 1 < len(matrix) and matrix[curX + 1][curY] == 2:
            path.append([curX + 1, curY])
            break
        elif curY + 1 < len(matrix) and matrix[curX][curY + 1] == 2:
            path.append([curX, curY + 1])
            break
        elif curX - 1 >= 0 and matrix[curX - 1][curY] == 2:
            path.append([curX - 1, curY])
            break
        elif curY - 1 >= 0 and matrix[curX][curY - 1] == 2:
            path.append([curX, curY - 1])
            break

        step = False
        # print(path)
        # for i in visitMatrix:
        #     print(*i)
        if curX + 1 < len(matrix) and visitMatrix[curX + 1][curY] == 0 and not step:
            visitMatrix[curX + 1][curY] = 1
            path.append([curX + 1, curY])
            step = True
        if curY + 1 < len(matrix) and visitMatrix[curX][curY + 1] == 0 and not step:
            visitMatrix[curX][curY + 1] = 1
            path.append([curX, curY + 1])
            step = True
        if curY - 1 >= 0 and visitMatrix[curX][curY - 1] == 0 and not step:
            visitMatrix[curX][curY - 1] = 1
            path.append([curX, curY - 1])
            step = True
        if curX - 1 >= 0 and visitMatrix[curX - 1][curY] == 0 and not step:
            visitMatrix[curX - 1][curY] = 1
            path.append([curX - 1, curY])
            step = True
        if not step:
            path.remove(path[-1])


def bfs(matrix, visitMatrix, curX=listOfVisited[-1][0], curY=listOfVisited[-1][1]):
    listOfVisited.append([curX, curY])
    while len(listOfVisited) > 0:
        #print(listOfVisited)
        # for i in visitMatrix:
        #     print(*i)
        curX = listOfVisited[0][0]
        curY = listOfVisited[0][1]
        if curX + 1 < len(matrix) and matrix[curX + 1][curY] == 2:
            listOfVisited.append([curX + 1, curY])
            break
        elif curY + 1 < len(matrix) and matrix[curX][curY + 1] == 2:
            listOfVisited.append([curX, curY + 1])
            break
        elif curX - 1 >= 0 and matrix[curX - 1][curY] == 2:
            listOfVisited.append([curX - 1, curY])
            break
        elif curY - 1 >= 0 and matrix[curX][curY - 1] == 2:
            listOfVisited.append([curX, curY - 1])
            break
        step = False
        # print(path)
        # for i in visitMatrix:
        #     print(*i)
        if curX + 1 < len(matrix) and visitMatrix[curX + 1][curY] == 0:
            visitMatrix[curX + 1][curY] = 1
            listOfVisited.append([curX + 1, curY])

        if curY + 1 < len(matrix) and visitMatrix[curX][curY + 1] == 0:
            visitMatrix[curX][curY + 1] = 1
            listOfVisited.append([curX, curY + 1])

        if curY - 1 >= 0 and visitMatrix[curX][curY - 1] == 0:
            visitMatrix[curX][curY - 1] = 1
            listOfVisited.append([curX, curY - 1])

        if curX - 1 >= 0 and visitMatrix[curX - 1][curY] == 0:
            visitMatrix[curX - 1][curY] = 1
            listOfVisited.append([curX - 1, curY])
        arrBeforePath.append(path[-1])
        listOfVisited.remove(listOfVisited[0])

