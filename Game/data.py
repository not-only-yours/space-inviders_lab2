import pygame
import csv
import numpy as np

# Initializations -----------------------
# DIMENSIONS
WIN_WIDTH, WIN_HEIGHT = 750,750
MENU_WIDTH = 150 

# COLORS
WHITE = (255,255,255)
GREEN = (154, 186, 182)
YELLOW = (255, 250, 149)

# PLAYERS
NB_ENEMIES= 7
ENEMY_HEALTH = 3
PLAYER_HEALTH = 7
PROBABILITY_SHOOTING = 1/150
NB_LASERS_TRACKED = 3

# DISPLAY
FRAME_RATE= 10
DT = 1/FRAME_RATE

# STATS
HIGHEST_SCORE = 0
EPISODE = 1

# Environment
NB_MINIMUM_CLOSEST_LASERS = 6

# ACTIONS
ACTIONS = [0,1,2,3]

with open('Game/SCORE.txt','r') as file:
	 reader = list(csv.reader(file))
	 if len(reader) >=2:
	 	ind = np.arange(1,len(reader),step=2)
	 	EPISODE = int(reader[-2][0][-1])+1	 	
	 	scores = [int(reader[i][0]) for i in ind]
	 	HIGHEST_SCORE = max(scores)

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH+MENU_WIDTH,WIN_HEIGHT))
pygame.display.set_caption('Spaceship Invaders')
font = pygame.font.SysFont('Times New Roman', 25)
font2 = pygame.font.SysFont('Times New Roman', 25)
font3 = pygame.font.SysFont('Times New Roman', 50)
font4 = pygame.font.SysFont('Times New Roman', 10)

# imgs
player_img = pygame.image.load('Game/Imgs/spaceship.png')
player_img = pygame.transform.scale(player_img, (75,75))
laser_player_img = pygame.image.load('Game/Imgs/laser_player.png')
enemy_img = pygame.image.load('Game/Imgs/enemy.png')
laser_enemy_img = pygame.image.load('Game/Imgs/laser_enemy.png')

# sizes
player_width,player_height = player_img.get_rect().size
enemy_width,enemy_height = enemy_img.get_rect().size
laser_width,laser_height = laser_player_img.get_rect().size

#  Background
BG = pygame.image.load('Game/Imgs/space.png')
BG = pygame.transform.scale(BG, (WIN_WIDTH + 200, WIN_HEIGHT))
