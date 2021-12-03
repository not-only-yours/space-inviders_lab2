import pygame
from numpy import random
from numpy.random import randint
from Game.data import *
from Game.functions import *

class Gameobject:
	def __init__(self,posx,posy,img):
		self.posx= posx
		self.posy = posy
		self.width,self.height = img.get_rect().size
		self.img = img
		self.left = False
		self.right = False
		self.velx = 200
		self.vely =200
		self.is_alive=True
		self.health = ENEMY_HEALTH	
		self.hit = 0
		self.hit_cond = False

	def __sub__(self, other):
		sign = np.sign(other.posx-self.posx)
		return sign*np.sqrt((other.posx-self.posx)**2+(other.posy - self.posy)**2)/WIN_HEIGHT



class player(Gameobject):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)


	def draw(self,win,player_shoots):
		for laser in player_shoots:
			if laser.posy > 0:
				laser.posy -= laser.vely*DT*2
			else:
				player_shoots.remove(laser)
			win.blit(laser.img,(laser.posx,laser.posy))	
		win.blit(self.img,(self.posx,self.posy))

	def collision(self,enemy_lasers):
		for laser in enemy_lasers:
			if touch(laser,self):
				enemy_lasers.remove(laser)
				self.hit +=1
				self.hit_cond=True
				if self.hit >= self.health:
					self.is_alive = False
					self.posx = 1000000
					self.posy = 1000000

	def closest_lasers(self,lasers_positions,treshold):
		if len(lasers_positions)>0:			
			result=sorted(lasers_positions, key=abs)[:treshold]

		else:
		   	result=[]
		return result



class enemy(Gameobject):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)


	def draw(self,win,lasers):
		for laser in lasers:
			if laser.posy < WIN_HEIGHT:
				laser.posy += laser.vely*DT/4
			else:
				lasers.remove(laser)
			win.blit(laser.img,(laser.posx,laser.posy))	
		win.blit(self.img,(self.posx,self.posy))

	def move(self):
		if self.posx >= WIN_WIDTH-enemy_width:
			self.posx = WIN_WIDTH-enemy_width
			self.velx *=-1
		if self.posx <= 0:
			self.posx = 0
			self.velx *=-1
		self.posx += self.velx*DT
		self.posy += self.vely*DT
		

	def collision(self,laser_list):
		for laser in laser_list:
			if touch(laser,self):

				laser_list.remove(laser)
				self.hit +=1
				self.hit_cond=True
				if self.hit >= self.health:
					self.is_alive = False

	def in_screen(self):
		return self.posy + 200< WIN_HEIGHT


def enemy_shoot(enemy,probability,lasers):
	if random.random() < probability:
		X = enemy.posx + (enemy.width-laser_width)/2
		Y = enemy.posy+enemy_height
		lasers.append(Gameobject(X,Y,laser_enemy_img))

	return lasers

def player_shoot(player,lasers):
	X = player.posx + (player.width-laser_width)/2
	Y = player.posy-laser_height
	lasers.append(Gameobject(X,Y,laser_player_img))

	return lasers


