import GlobalVariables as gv
import numpy

# empty = 0
# current = 1
# enemy = 2
# asteroids = 3

Matrix = numpy.full((int(750 / 50), int(750 / 50)), 0)




def createStartMatrix():
    for i in gv.ASTEROIDS:
        for j in range(int((i.x - 20) / 50), int((i.x + 20) / 50)):
            for k in range(int((i.y - 20) / 50), int((i.y + 20) / 50)):
                if 0 < j < len(Matrix) and 0 < k < len(Matrix):
                    Matrix[j][k] = 3
                    gv.VisitMatrix[j][k] = 1
    for i in gv.ENEMIES:
        for j in range(int((i.x - 20) / 50), int((i.x + 20) / 50)):
            for k in range(int((i.y - 20) / 50), int((i.y + 20) / 50)):
                if 0 < j < len(Matrix) and 0 < k < len(Matrix):
                    Matrix[j][k] = 2
                    gv.VisitMatrix[j][k] = 1

    Matrix[0][0] = 0
    Matrix[int(gv.currPoint[1])][int(gv.currPoint[0])] = 1
    gv.VisitMatrix[int(gv.currPoint[1])][int(gv.currPoint[0])] = 1


def dfs():
    #print(gv.path)
    turn = False
    if not gv.End:
        if 0 <= gv.currPoint[1] - 1 < len(Matrix) and Matrix[gv.currPoint[1] - 1][gv.currPoint[0]] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1] - 1, gv.currPoint[0]].copy())
            gv.dfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[0] - 1 < len(Matrix) and Matrix[gv.currPoint[1]][gv.currPoint[0] - 1] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1],gv.currPoint[0] - 1].copy())
            gv.dfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[0] + 1 < len(Matrix) and Matrix[gv.currPoint[1]][gv.currPoint[0] + 1] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1], gv.currPoint[0] + 1].copy())
            gv.dfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[1] + 1 < len(Matrix) and Matrix[gv.currPoint[1] + 1][gv.currPoint[0]] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1] + 1,gv.currPoint[0]].copy())
            gv.dfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[1] + 1 < len(Matrix) and gv.VisitMatrix[gv.currPoint[1] + 1][gv.currPoint[0]] == 0:
            gv.path.append(gv.currPoint.copy())
            gv.VisitMatrix[gv.currPoint[1] + 1][gv.currPoint[0]] = 1

            turn = True
            gv.currPoint[1] = gv.currPoint[1] + 1
            dfs()
        elif 0 <= gv.currPoint[0] + 1 < len(Matrix) and gv.VisitMatrix[gv.currPoint[1]][gv.currPoint[0] + 1] == 0:
            gv.path.append(gv.currPoint.copy())
            gv.VisitMatrix[gv.currPoint[1]][gv.currPoint[0] + 1] = 1

            turn = True
            gv.currPoint[0] = gv.currPoint[0] + 1
            dfs()
        elif 0 <= gv.currPoint[0] - 1 < len(Matrix) and gv.VisitMatrix[gv.currPoint[1]][gv.currPoint[0] - 1] == 0:
            gv.path.append(gv.currPoint.copy())
            gv.VisitMatrix[gv.currPoint[1]][gv.currPoint[0] - 1] = 1

            turn = True
            gv.currPoint[0] = gv.currPoint[0] - 1
            dfs()
        elif 0 <= gv.currPoint[1] - 1 < len(Matrix) and gv.VisitMatrix[gv.currPoint[1] - 1][gv.currPoint[0]] == 0:
            gv.path.append(gv.currPoint.copy())
            gv.VisitMatrix[gv.currPoint[1] - 1][gv.currPoint[0]] = 1

            turn = True
            gv.currPoint[1] = gv.currPoint[1] - 1
            dfs()
        elif not turn:
            gv.currPoint = gv.path[-1]
            Matrix[gv.currPoint[1]][gv.currPoint[0]] = 0
            gv.path.remove(gv.path[-1])


def bfs():
    turn = False
    if not gv.End:
        if 0 <= gv.currPoint[1] - 1 < len(Matrix) and Matrix[gv.currPoint[1] - 1][gv.currPoint[0]] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1] - 1, gv.currPoint[0]].copy())
            gv.bfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[0] - 1 < len(Matrix) and Matrix[gv.currPoint[1]][gv.currPoint[0] - 1] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1], gv.currPoint[0] - 1].copy())
            gv.bfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[0] + 1 < len(Matrix) and Matrix[gv.currPoint[1]][gv.currPoint[0] + 1] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1], gv.currPoint[0] + 1].copy())
            gv.bfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[1] + 1 < len(Matrix) and Matrix[gv.currPoint[1] + 1][gv.currPoint[0]] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1] + 1, gv.currPoint[0]].copy())
            gv.bfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[0] + 1 < len(Matrix) and Matrix[gv.currPoint[1]][gv.currPoint[0] + 1] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1], gv.currPoint[0] + 1].copy())
            gv.bfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[1] + 1 < len(Matrix) and Matrix[gv.currPoint[1] + 1][gv.currPoint[0]] == 2:
            gv.End = True
            turn = True
            gv.findedPoints.append([gv.currPoint[1] + 1, gv.currPoint[0]].copy())
            gv.bfsArrayOfPath.append(gv.path.copy())
        elif 0 <= gv.currPoint[1] + 1 < len(Matrix) and gv.VisitMatrix[gv.currPoint[1] + 1][gv.currPoint[0]] == 0:
            gv.path.append(gv.currPoint.copy())
            gv.VisitMatrix[gv.currPoint[1] + 1][gv.currPoint[0]] = 1
            Matrix[gv.currPoint[1] + 1][gv.currPoint[0]] = 1
            turn = True
            gv.currPoint[1] = gv.currPoint[1] + 1
            bfs()
        elif 0 <= gv.currPoint[0] + 1 < len(Matrix) and gv.VisitMatrix[gv.currPoint[1]][gv.currPoint[0] + 1] == 0:
            gv.path.append(gv.currPoint.copy())
            gv.VisitMatrix[gv.currPoint[1]][gv.currPoint[0] + 1] = 1
            Matrix[gv.currPoint[1]][gv.currPoint[0] + 1] = 1
            turn = True
            gv.currPoint[0] = gv.currPoint[0] + 1
            bfs()
        elif 0 <= gv.currPoint[0] - 1 < len(Matrix) and gv.VisitMatrix[gv.currPoint[1]][gv.currPoint[0] - 1] == 0:
            gv.path.append(gv.currPoint.copy())
            gv.VisitMatrix[gv.currPoint[1]][gv.currPoint[0] - 1] = 1
            Matrix[gv.currPoint[1]][gv.currPoint[0] - 1] = 1
            turn = True
            gv.currPoint[0] = gv.currPoint[0] - 1
            bfs()
        elif 0 <= gv.currPoint[1] - 1 < len(Matrix) and gv.VisitMatrix[gv.currPoint[1] - 1][gv.currPoint[0]] == 0:
            gv.path.append(gv.currPoint.copy())
            gv.VisitMatrix[gv.currPoint[1] - 1][gv.currPoint[0]] = 1
            Matrix[gv.currPoint[1] - 1][gv.currPoint[0]] = 1
            turn = True
            gv.currPoint[1] = gv.currPoint[1] - 1
            bfs()
        elif not turn:
            gv.currPoint = gv.path[-1]
            Matrix[gv.currPoint[1]][gv.currPoint[0]] = 0
            gv.path.remove(gv.path[-1])
