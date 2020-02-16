import pygame
import random
from math import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)


pygame.init()
screenwidth = 800
screenheight = 600

gameDisplay = pygame.display.set_mode((screenwidth,screenheight))

class vertices(pygame.sprite.Sprite):
	def __init__(self, x, y, num):
		self.x = x
		self.y = y
		self.size = 4
		self.color = (255,0,0)	
		self.thickness = 2
		self.num = num
	def display(self):
		screen = gameDisplay
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.thickness)
	def __str__(self):
		return "x:{} y:{}".format(self.x, self.y)


multBy = 2
dots = 100	


def mults(multBy, dots):
	a = 2*pi / dots
	r = 250
	verts = []
	connect = []
	graph = []

	for q in range(dots):
		x = int(r*sin(q*a) + 400)
		y = int(r*cos(q*a) + 300)
		connect = [*connect, [q, q*multBy]]
		graph.append([])
		verts = [*verts, vertices(x,y,q)]
		

	for c in connect:
		if c[1] >= dots:
			c[1] = c[1]%dots
		graph[c[0]].append(c[1])
		
	return [verts, connect, graph]
		

font_1 = pygame.font.SysFont('Courier New', 15)
                             #(font name,size)
	
all_verts = pygame.sprite.Group()
clock = pygame.time.Clock()
seb = 0
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop
			if event.key == K_SPACE:
				seb = 0
			if event.key == K_UP:
				seb += 0.01
			elif event.key == K_DOWN:
				seb -= 0.01
			elif event.key == K_LEFT:
				multBy += 1
			elif event.key == K_RIGHT:
				multBy -= 1
			elif event.key == K_ESCAPE:
				multBy = 0
			
	gameDisplay.fill((0,0,255))
	
	
	this_sentence=font_1.render("mult by: {}".format(multBy),True,(255,255,255))
	gameDisplay.blit(this_sentence,(10,10))
	this_sentence=font_1.render("dots: {}".format(dots),True,(255,255,255))
	gameDisplay.blit(this_sentence,(10,30))
	this_sentence=font_1.render("sebesseg: {}".format(seb),True,(255,255,255))
	gameDisplay.blit(this_sentence,(10,50))
	verts = mults(multBy, dots)[0]
	graph = mults(multBy, dots)[2]
	
	for v in verts:
		v.display()
		
	
	
	for e in range(len(verts)):
		e = int(round(e, 0))
		print(e)
		for u in graph[e]:
			u = int(round(u, 0))
			print(u)
			if u == dots:
				u = 0
			pygame.draw.line(gameDisplay, (255,0,0), [verts[e].x, verts[e].y], [verts[u].x, verts[u].y], 2)
			
	
	multBy += seb
	multBy = round(multBy, 2)
	
	pygame.time.wait(10)

	pygame.display.flip()
	clock = pygame.time.Clock()
	
	
	
	
	
	
	
