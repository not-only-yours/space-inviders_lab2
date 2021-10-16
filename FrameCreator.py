import time

import GlobalVariables as gv
import Algorytms


def updateFrame():  # оновлення фрейму
    Tre = None
    gv.WINDOW.blit(gv.BACKGROUND_PNG, (0, 0))

    lives_label = gv.MAIN_FONT.render(f"Lives: {gv.LIVES}", 1, (255, 255, 255))
    level_label = gv.MAIN_FONT.render(f"Level: {gv.LEVEL}", 1, (255, 255, 255))
    score_label = gv.MAIN_FONT.render(f"Score: {gv.SCORE}", 1, (255, 255, 255))
    enemyType1 = gv.MAIN_FONT.render(f"Enemy type 1: {len(gv.ENEMIES)}", 1, (255, 255, 255))
    enemyType2 = gv.MAIN_FONT.render(f"Enemy type 2: 1", 1, (255, 255, 255))
    gv.WINDOW.blit(lives_label, (10, 10))
    gv.WINDOW.blit(enemyType1, (10, 70))
    gv.WINDOW.blit(enemyType2, (10, 100))
    gv.WINDOW.blit(level_label, (gv.WIDTH - level_label.get_width() - 10, 10))
    gv.WINDOW.blit(score_label, (10, 40))
    for enemy in gv.ENEMIES:
        enemy.draw(gv.WINDOW)
    for asteroid in gv.ASTEROIDS:
        asteroid.draw()
    # if gv.RANDOM_LIB.randrange(0, 2000) == 1:
    #     gv.ShipCreator.create_asteroids()

    gv.GOOD_SHIP.draw(gv.WINDOW)

    if gv.LOST:  # програш
        lost_label = gv.LOST_FONT.render(f"YOU LOST!", 1, (255, 255, 255))
        score_label = gv.LOST_FONT.render(f"YOUR SCORE IS: {gv.SCORE}", 1, (255, 255, 255))
        gv.WINDOW.blit(lost_label, (gv.WIDTH / 2 - lost_label.get_width() / 2, 250))
        gv.WINDOW.blit(score_label, (gv.WIDTH / 2 - score_label.get_width() / 2, 350))

    Algorytms.createVisitMatrix(Algorytms.matrix)
    Algorytms.fillMatrix(Algorytms.matrix)
    for i in Algorytms.matrix:
        print(*i)

    if Algorytms.enemyArray:
        Algorytms.emptyMatrix(Algorytms.visited, [int(gv.GOOD_SHIP.y / 50), int(gv.GOOD_SHIP.x / 50)])
        Algorytms.emptyMatrix(Algorytms.matrix, [int(gv.GOOD_SHIP.y / 50), int(gv.GOOD_SHIP.x / 50)])
        # print("aaaaaaa")
        # for i in Algorytms.matrix:
        #     print(*i)
        Tre = Algorytms.Tree
        print(Algorytms.enemyArray)
        Tre.createTree(Tre)

        Tre.current = Tre.startNode

        Algorytms.emtyVisitMatrix()

        Tre.setPriceInTree(Tre)

        Tre.current = Tre.startNode
        # for i in Algorytms.matrix:
        #     print(*i)

    Algorytms.moveEnemy()
    Algorytms.enemyArray = []
    gv.PG_LIB.display.update()
    # for k in gv.dfsArrayOfPath:
    #     for i in range(len(k)):
    #         for j in range(len(k)):
    #             if k[i][j] == 1 or k[i][j] == 4:
    #                 gv.WINDOW.set_at((i,j), (255,0,0))

    # print(gv.enemyCount)

    # print(len(Algorytms.Matrix))
    # print(gv.currPoint)
