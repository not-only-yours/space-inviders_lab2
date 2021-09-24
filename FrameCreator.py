import GlobalVariables as gv
import Algorytms

def updateFrame(): # оновлення фрейму

    gv.WINDOW.blit(gv.BACKGROUND_PNG, (0, 0))

    lives_label = gv.MAIN_FONT.render(f"Lives: {gv.LIVES}", 1, (255, 255, 255))
    level_label = gv.MAIN_FONT.render(f"Level: {gv.LEVEL}", 1, (255, 255, 255))
    score_label = gv.MAIN_FONT.render(f"Score: {gv.SCORE}", 1, (255, 255, 255))
    gv.WINDOW.blit(lives_label, (10, 10))
    gv.WINDOW.blit(level_label, (gv.WIDTH - level_label.get_width() - 10, 10))
    gv.WINDOW.blit(score_label,(10,40))
    for enemy in gv.ENEMIES:
        enemy.draw(gv.WINDOW)
    for asteroid in gv.ASTEROIDS:
        asteroid.draw()
    if gv.RANDOM_LIB.randrange(0, 2000) == 1:
        gv.ShipCreator.create_asteroids()

    gv.GOOD_SHIP.draw(gv.WINDOW)

    if gv.LOST:  # програш
        lost_label = gv.LOST_FONT.render(f"YOU LOST!", 1, (255, 255, 255))
        score_label = gv.LOST_FONT.render(f"YOUR SCORE IS: {gv.SCORE}", 1, (255, 255, 255))
        gv.WINDOW.blit(lost_label, (gv.WIDTH / 2 - lost_label.get_width() / 2, 250))
        gv.WINDOW.blit(score_label, (gv.WIDTH / 2 - score_label.get_width() / 2, 350))

    Algorytms.arrayOfPath = []
    Algorytms.createVisitMatrix(Algorytms.matrix)
    Algorytms.fillMatrix(Algorytms.matrix)
    # for i in Algorytms.matrix:
    #     print(*i)
    while Algorytms.enemyArray:
        Algorytms.emptyMatrix(Algorytms.lenMatrix, Algorytms.startPoint)
        Algorytms.markThree(Algorytms.matrix)
        # for i in lenMatrix:
        #     print(*i)
        Algorytms.path = []
        Algorytms.astar(Algorytms.curr)
        # print(path)
        Algorytms.enemyArray.remove(Algorytms.enemyArray[0])
        Algorytms.arrayOfPath.append(Algorytms.path)
        for i in Algorytms.lenMatrix:
            print(*i)
    if gv.GOOD_SHIP and Algorytms.arrayOfPath:
        if not gv.GOOD_SHIP.y == Algorytms.arrayOfPath[0][0][0]:
            gv.GOOD_SHIP.y = Algorytms.arrayOfPath[0][0][0] * 50
            Algorytms.curr = [Algorytms.arrayOfPath[0][0][0], int(gv.GOOD_SHIP.x / 50)]
        if not gv.GOOD_SHIP.x == Algorytms.arrayOfPath[0][0][1]:
            gv.GOOD_SHIP.x = Algorytms.arrayOfPath[0][0][1] * 50
            Algorytms.curr = [int(gv.GOOD_SHIP.y / 50), Algorytms.arrayOfPath[0][0][1]]
        Algorytms.arrayOfPath = []
    # print(len(Algorytms.arrayOfPath))


    gv.PG_LIB.display.update()
    # for k in gv.dfsArrayOfPath:
    #     for i in range(len(k)):
    #         for j in range(len(k)):
    #             if k[i][j] == 1 or k[i][j] == 4:
    #                 gv.WINDOW.set_at((i,j), (255,0,0))


    # print(gv.enemyCount)



    # print(len(Algorytms.Matrix))
    # print(gv.currPoint)


