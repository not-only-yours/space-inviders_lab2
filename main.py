import GlobalVariables as gv
import Algorytms
import time

def main():
    gv.CAN_EDIT = True
    gv.PG_LIB.display.set_caption("Space Invaders") # Назва застосунку

    run = True
    clock = gv.PG_LIB.time.Clock()
    while run:
        clock.tick(gv.FPS)  #Виставлено кількість оновлень у секунду

        gv.FrameCreator_LIB.updateFrame()
        if gv.LIVES <= 0 or gv.GOOD_SHIP.health <= 0: # умови програшу
            gv.LOST = True
            gv.LOST_COUNT += 1

        if gv.LOST:         # час показання екрану програшу
            if gv.LOST_COUNT > gv.FPS * 3:
                run = False

            else:
                continue
        if len(gv.ENEMIES) == 0:  # збільшення рівня складності
            gv.LEVEL += 1
            gv.WAVE_LENGTH += 5
            for i in range(gv.WAVE_LENGTH):         # створення масиву з ворогів
                enemy = gv.ShipCreator.Enemy(gv.RANDOM_LIB.randrange(0, 4) * 150,
                                             gv.RANDOM_LIB.randrange(-1500, -100),
                                             gv.RANDOM_LIB.choice(["red", "blue", "purple"])) # створення місця та колір ворога
                gv.ENEMIES.append(enemy)
        for event in gv.PG_LIB.event.get():
            if event.type == gv.PG_LIB.QUIT:
                run = False

        keys = gv.PG_LIB.key.get_pressed()   # рух корабля по натиску на клавішу та стрільба
        if keys[gv.PG_LIB.K_a] and gv.GOOD_SHIP.x - gv.PLAYER_VEL > 0:  # left
            gv.GOOD_SHIP.x -= gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_d] and gv.GOOD_SHIP.x + gv.PLAYER_VEL + gv.GOOD_SHIP_SIZEX < gv.WIDTH:  # right
            gv.GOOD_SHIP.x += gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_w] and gv.GOOD_SHIP.y - gv.PLAYER_VEL > 0:  # up
            gv.GOOD_SHIP.y -= gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_s] and gv.GOOD_SHIP.y + gv.PLAYER_VEL + gv.GOOD_SHIP_SIZEY < gv.HEIGHT:  # down
            gv.GOOD_SHIP.y += gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_SPACE]:
            gv.GOOD_SHIP.shoot()

        if keys[gv.PG_LIB.K_z]:
            gv.work = True
            if gv.currAlg == "dfs":
                print("current alg bfs")
                gv.currAlg = "bfs"
            elif gv.currAlg == "bfs":
                print("current alg ucs")
                gv.currAlg = "ucs"
            elif gv.currAlg == "ucs":
                print("current alg dfs")
                gv.currAlg = "dfs"
            # if len(Algorytms.path) > 0:
            #     for i in Algorytms.path:
            #         Algorytms.path.remove(i)
            # if len(Algorytms.listOfVisited) > 0:
            #     for i in Algorytms.listOfVisited:
            #         Algorytms.listOfVisited.remove(i)
            # if len(Algorytms.ucsListOfVisited) > 0:
            #     for i in Algorytms.ucsListOfVisited:
            #         Algorytms.ucsListOfVisited.remove(i)


        if keys[gv.PG_LIB.K_x]:
            if gv.work == True:
                Algorytms.createStartMatrix()
                print(Algorytms.matrix)
                if gv.currAlg == "dfs":
                    gv.work = False
                    start_time = time.time()

                    while Algorytms.numofEnemy > 0:
                        if len(Algorytms.path) > 1:
                            Algorytms.matrix[Algorytms.path[-1][0]][Algorytms.path[-1][1]] = 3
                            Algorytms.arrOfPath.append(Algorytms.path)
                            Algorytms.path = [Algorytms.arrOfPath[0][0]]
                            Algorytms.numofEnemy -= 1
                            Algorytms.createVisitMatrix(Algorytms.matrix, Algorytms.visitMatrix)
                        Algorytms.dfs(Algorytms.matrix, Algorytms.visitMatrix)
                    for i in Algorytms.arrOfPath:
                        print(*i)
                    print("--- %s seconds ---" % (time.time() - start_time))

                if gv.currAlg == "bfs":
                    start_time = time.time()
                    gv.work = False
                    while Algorytms.numofEnemy > 0:
                        # print(path)
                        if len(Algorytms.listOfVisited) > 1:
                            Algorytms.matrix[Algorytms.listOfVisited[-1][0]][Algorytms.listOfVisited[-1][1]] = 3
                            # print(arrBeforePath)
                            Algorytms.arrOfList.append(Algorytms.arrBeforePath)
                            Algorytms.arrOfList.append(Algorytms.listOfVisited)
                            listOfVisited = [Algorytms.arrOfList[0][0]]
                            Algorytms.numofEnemy -= 1
                            Algorytms.createVisitMatrix(Algorytms.matrix, Algorytms.visitMatrix)
                        Algorytms.bfs(Algorytms.matrix, Algorytms.visitMatrix)

                    for i in Algorytms.arrOfList:
                        print(*i)
                    print("--- %s seconds ---" % (time.time() - start_time))

                if gv.currAlg == "ucs":
                    start_time = time.time()
                    gv.work = False
                    while Algorytms.numofEnemy > 0:
                        # print(path)
                        if len(Algorytms.ucsListOfVisited) > 1:
                            Algorytms.matrix[Algorytms.ucsListOfVisited[-1][0]][Algorytms.ucsListOfVisited[-1][1]] = 3
                            # print(arrBeforePath)
                            Algorytms.arrOfList.append(Algorytms.arrBeforePath)
                            Algorytms.arrOfList.append(Algorytms.ucsListOfVisited)
                            Algorytms.ucsListOfVisited = [Algorytms.arrOfList[0][0]]
                            Algorytms.numofEnemy -= 1
                            Algorytms.createVisitMatrix(Algorytms.matrix, Algorytms.visitMatrix)
                        Algorytms.ucs(Algorytms.matrix, Algorytms.visitMatrix)
                    Algorytms.findEnemyCoords(Algorytms.matrix)

                    for i in Algorytms.lenMatrix:
                        print(*i)
                    print("Enemy array:")
                    print(Algorytms.enemyCoords)
                    for i in Algorytms.enemyCoords:
                        curr = i
                        minimum = 10000
                        next = []
                        while minimum != 1:
                            Algorytms.ucsList.append(curr)
                            if curr[0] - 1 >= 0 and 0 < Algorytms.lenMatrix[curr[0] - 1][curr[1]] < minimum:
                                minimum = Algorytms.lenMatrix[curr[0] - 1][curr[1]]
                                next = [curr[0] - 1, curr[1]]
                            if curr[1] - 1 >= 0 and 0 < Algorytms.lenMatrix[curr[0]][curr[1] - 1] < minimum:
                                minimum = Algorytms.lenMatrix[curr[0]][curr[1] - 1]
                                next = [curr[0], curr[1] - 1]
                            if curr[0] + 1 < 15 and 0 < Algorytms.lenMatrix[curr[0] + 1][curr[1]] < minimum:
                                minimum = Algorytms.lenMatrix[curr[0] + 1][curr[1]]
                                next = [curr[0] + 1, curr[1]]
                            if curr[1] + 1 < 15 and 0 < Algorytms.lenMatrix[curr[0]][curr[1] + 1] < minimum:
                                minimum = Algorytms.lenMatrix[curr[0]][curr[1] + 1]
                                next = [curr[0], curr[1] + 1]
                            curr = next

                        Algorytms.arrUcsList.append(Algorytms.ucsList)
                        Algorytms.ucsList = []
                        print("--- %s seconds ---" % (time.time() - start_time))
                    # print(arrUcsList)
                    print("Distance matrix")


                    print("path to enemies:")
                    for i in Algorytms.arrUcsList:
                        print(*i)

                    if len(Algorytms.path) > 0:
                        gv.pixelPath = []
                        for i in Algorytms.path:
                            pix = gv.ShipCreator.Pixel(int(i[0] * 50), int(i[1] * 50))
                            gv.pixelPath.append(pix)

                    if len(Algorytms.listOfVisited) > 0:
                        gv.pixelPath = []
                        for i in Algorytms.listOfVisited:
                            pix = gv.ShipCreator.Pixel(int(i[0] * 50), int(i[1] * 50))
                            gv.pixelPath.append(pix)

                    if len(Algorytms.ucsListOfVisited) > 0:
                        gv.pixelPath = []
                        for i in Algorytms.ucsListOfVisited:
                            pix = gv.ShipCreator.Pixel(int(i[0] * 50), int(i[1] * 50))
                            gv.pixelPath.append(pix)


                        # if len(Algorytms) > 0:
                        #     for i in Algorytms.pixelPath:
                        #         gv.pixelPath.remove(i)




        for enemy in gv.ENEMIES[:]:
            enemy.move(gv.ENEMY_VEL)
            enemy.move_lasers(gv.LASER_VEL, gv.GOOD_SHIP)

            if gv.RANDOM_LIB.randrange(0, 20) == 1:   # рандомізація пострілу ворога
                enemy.shoot()

            if gv.LaserCreator.collide(enemy, gv.GOOD_SHIP):  # дотик до ворога
                gv.GOOD_SHIP.health -= 10
                gv.ENEMIES.remove(enemy)
                gv.SCORE -= 20

            if enemy.y + gv.BAD_SHIP_SIZEY + 10 > gv.HEIGHT:  # проходження ворогу до низу екрану
                gv.LIVES -= 1
                gv.ENEMIES.remove(enemy)
                gv.SCORE -= 100

        for asteroid in gv.ASTEROIDS[:]:
            asteroid.move(0.8 * gv.ENEMY_VEL)

            if gv.LaserCreator.collide(asteroid, gv.GOOD_SHIP):  # дотик до ворога
                gv.GOOD_SHIP.health -= 5
                gv.ASTEROIDS.remove(asteroid)


        gv.GOOD_SHIP.move_lasers(-gv.LASER_VEL, gv.ENEMIES)
        gv.GOOD_SHIP.move_lasers(-gv.LASER_VEL, gv.ASTEROIDS)

        gv.FrameCreator_LIB.updateFrame()


if __name__ == '__main__':
    title_font = gv.PG_LIB.font.SysFont("comicsans", 70)
    run = True
    main_menu = True
    while run:
        gv.WINDOW.blit(gv.BACKGROUND_PNG, (0, 0))   #створення графіки для гри
        title_label = title_font.render("Press any button to begin...", 1, (255, 255, 255))

        gv.WINDOW.blit(title_label, (gv.WIDTH / 2 - title_label.get_width() / 2,350))
        if main_menu:
            main_menu = False

        gv.PG_LIB.display.update()
        for event in gv.PG_LIB.event.get():
            if event.type == gv.PG_LIB.QUIT:
                run = False
            if event.type == gv.PG_LIB.KEYDOWN or event.type == gv.PG_LIB.MOUSEBUTTONDOWN:
                main()
    gv.PG_LIB.quit()
