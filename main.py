import GlobalVariables as gv
import Algorytms
import time


def main():
    gv.CAN_EDIT = True
    gv.PG_LIB.display.set_caption("Space Invaders")  # Назва застосунку

    run = True
    clock = gv.PG_LIB.time.Clock()
    while run:
        clock.tick(gv.FPS)  # Виставлено кількість оновлень у секунду

        gv.FrameCreator_LIB.updateFrame()
        if gv.LIVES <= 0 or gv.GOOD_SHIP.health <= 0:  # умови програшу
            gv.LOST = True
            gv.LOST_COUNT += 1

        if gv.LOST:  # час показання екрану програшу
            if gv.LOST_COUNT > gv.FPS * 3:
                run = False
                with open('somefile.txt', 'a') as the_file:
                    the_file.write(
                        f'level: {gv.LEVEL - 1} lost, time: {time.time() - gv.time} seconds, score: {gv.SCORE} \n')
            else:
                continue
        if len(gv.ENEMIES) == 0:  # збільшення рівня складності
            if gv.LEVEL != 1:
                with open('somefile.txt', 'a') as the_file:
                    the_file.write(
                        f'level: {gv.LEVEL - 1} passed, time: {time.time() - gv.time} seconds, score: {gv.SCORE} \n')
            gv.LEVEL += 1
            gv.WAVE_LENGTH += 5
            for i in range(gv.WAVE_LENGTH):  # створення масиву з ворогів
                enemy = gv.ShipCreator.Enemy(gv.RANDOM_LIB.randrange(1, 12) * 50,
                                             gv.RANDOM_LIB.randrange(-1500, -100),
                                             gv.RANDOM_LIB.choice(
                                                 ["red", "blue", "purple"]))  # створення місця та колір ворога
                gv.ENEMIES.append(enemy)
            gv.time = time.time()

        for event in gv.PG_LIB.event.get():
            if event.type == gv.PG_LIB.QUIT:
                run = False

        keys = gv.PG_LIB.key.get_pressed()  # рух корабля по натиску на клавішу та стрільба
        if keys[gv.PG_LIB.K_a] and gv.GOOD_SHIP.x - gv.PLAYER_VEL > 0:  # left
            gv.GOOD_SHIP.x -= gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_d] and gv.GOOD_SHIP.x + gv.PLAYER_VEL + gv.GOOD_SHIP_SIZEX < gv.WIDTH:  # right
            gv.GOOD_SHIP.x += gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_w] and gv.GOOD_SHIP.y - gv.PLAYER_VEL > 0:  # up
            gv.GOOD_SHIP.y -= gv.PLAYER_VEL
        if keys[gv.PG_LIB.K_s] and gv.GOOD_SHIP.y + gv.PLAYER_VEL + gv.GOOD_SHIP_SIZEY < gv.HEIGHT:  # down
            gv.GOOD_SHIP.y += gv.PLAYER_VEL

        gv.GOOD_SHIP.shoot()

        # if len(Algorytms) > 0:
        #     for i in Algorytms.pixelPath:
        #         gv.pixelPath.remove(i)

        for enemy in gv.ENEMIES[:]:
            enemy.move(gv.ENEMY_VEL)
            enemy.move_lasers(gv.LASER_VEL, gv.GOOD_SHIP)

            if gv.RANDOM_LIB.randrange(0, 20) == 1:  # рандомізація пострілу ворога
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
        gv.WINDOW.blit(gv.BACKGROUND_PNG, (0, 0))  # створення графіки для гри
        title_label = title_font.render("Press any button to begin...", 1, (255, 255, 255))

        gv.WINDOW.blit(title_label, (gv.WIDTH / 2 - title_label.get_width() / 2, 350))
        if main_menu:
            main_menu = False
            Algorytms.startGame = True
        gv.PG_LIB.display.update()
        for event in gv.PG_LIB.event.get():
            if event.type == gv.PG_LIB.QUIT:
                run = False
            if event.type == gv.PG_LIB.KEYDOWN or event.type == gv.PG_LIB.MOUSEBUTTONDOWN:
                main()
    gv.PG_LIB.quit()
