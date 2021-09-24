import numpy
import pygame
import os
import time
import random
import FrameCreator
import ShipCreator as sc
import LaserCreator


# created global variables of libraries
OS_LIB = os
PG_LIB = pygame
TIME_LIB = time
RANDOM_LIB = random
FrameCreator_LIB = FrameCreator
ShipCreator = sc
LaserCreator = LaserCreator

# Created global variables of Integer values
LOST = False
FPS = 25
LEVEL = 1
LIVES = 5
SCORE = 0
WIDTH, HEIGHT = 750, 750
PLAYER_VEL = 5
LASER_VEL = 4
ENEMIES = []
ASTEROIDS = []
WAVE_LENGTH = 5
ENEMY_VEL = 1
LOST_COUNT = 0
GOOD_SHIP_SIZEX, GOOD_SHIP_SIZEY = 50, 50
BAD_SHIP_SIZEX, BAD_SHIP_SIZEY = 50, 50
LASER_SIZEX = 10
LASER_SIZEY = 20
LINE = []
# Created global variables of Font
PG_LIB.font.init()
MAIN_FONT = PG_LIB.font.SysFont("comicsans", 50)
LOST_FONT = PG_LIB.font.SysFont("comicsans", 60)

WINDOW = PG_LIB.display.set_mode((WIDTH, HEIGHT))

# Created global variables of boats images
GOOD_SHIP_PNG = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "good_ship.png")),
                                       (GOOD_SHIP_SIZEX, GOOD_SHIP_SIZEY))

BAD_SHIP_RED_PNG = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "bad_ship_red.png")),
                                          (BAD_SHIP_SIZEX, BAD_SHIP_SIZEX))
BAD_SHIP_BLUE_PNG = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "bad_ship_blue.png")),
                                           (BAD_SHIP_SIZEX, BAD_SHIP_SIZEX))
BAD_SHIP_PURPLE_PNG = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "bad_ship_purple.png")),
                                             (BAD_SHIP_SIZEX, BAD_SHIP_SIZEX))

BAD_BULLET_PNG = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "bad_bullet.png")),
                                        (LASER_SIZEX, LASER_SIZEY))
GOOD_BULLET_PNG = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "good_bullet.png")),
                                         (LASER_SIZEX, LASER_SIZEY))

# Created global variables of background images
BACKGROUND_PNG = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))
PIXELPOINT = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "1x1.png")), (10, 10))
WAY = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "unknown.png")), (15, 15))
ASTEROID = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets",
                                                                 "66-667836_meteor-clipart-pixel-art-asteroid-png.jpg")),
                                  (BAD_SHIP_SIZEX, BAD_SHIP_SIZEX))
# Created ships
GOOD_SHIP = sc.Player(350, 600)

COLOR_MAP = {
    "red": BAD_SHIP_RED_PNG,
    "blue": BAD_SHIP_BLUE_PNG,
    "purple": BAD_SHIP_PURPLE_PNG
}


currPoint = [GOOD_SHIP.x/150, GOOD_SHIP.y/150]
dfsArrayOfPath = []
bfsArrayOfPath = []
End = False
path = []
VisitMatrix = numpy.full((int(WIDTH / 50), int(HEIGHT / 50)), 0)
findedPoints = []
enemyCount = 0
currAlg = "ucs"
pixelPath = []
work = True