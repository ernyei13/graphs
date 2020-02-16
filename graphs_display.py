import pygame
import random
from math import *

pygame.init()

red = (255,0,0)	
idk = (255,255,0)	
font_1 = pygame.font.SysFont('Courier New', 15)

def findPathSimple(s, b, graph):
    visited = {s}
    stack= [s]
    path = []  
	
    while stack != []:
        top = stack[-1]
        path = [*path, top]
        neighboursOfTop  =  graph[top]
        if b in  neighboursOfTop:
            return path + [b]
        neighboursToCheck = [x for x in neighboursOfTop if x not in visited]
		
        if neighboursToCheck != []:
            nextTop = neighboursToCheck[-1]
            stack = [*stack, nextTop]
            visited = {*visited, nextTop}
        else:
            stack = stack[:-1]
            
            path = path[:-2]     
    return  None
	

def createGraph(p):
	connected = []
	x = random.randint(5, p)
	for r in range(x):
		connected.append([])
	for c in range(len(connected)):
		for r in range(random.randint(0, 4)):
			a = random.randint(0, x-1)
			if a not in connected[c]:
				connected[c].append(a)
	return connected







	

screenwidth = 800
screenheight = 600

gameDisplay = pygame.display.set_mode((screenwidth,screenheight))

class vertices(pygame.sprite.Sprite):
	def __init__(self, x, y, num):
		self.x = x
		self.y = y
		self.size = 10
		
		self.thickness = 2
		self.num = num
	def display(self, color):
		screen = gameDisplay
		pygame.draw.circle(screen, color, (self.x, self.y), self.size, self.thickness)
		this_sentence=font_1.render((str(self.num)),True,(255,255,255))
		screen.blit(this_sentence, (self.x,self.y -30))
	def __str__(self):
		return "x:{} y:{}".format(self.x, self.y)

graph = createGraph(15)

a = 2*pi / len(graph)
r = 150
verts = []


for q in range(len(graph)):
	x = int(r*sin(q*a) + 400)
	y = int(r*cos(q*a) + 300)

	verts = [*verts, vertices(x,y,q)]

	
	

	
all_verts = pygame.sprite.Group()
clock = pygame.time.Clock()
run = True
cnt = 0
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	gameDisplay.fill((0,0,255))
	
	for v in verts:
		v.display(red)
	for e in range(len(verts)):
		for u in graph[e]:
			pygame.draw.line(gameDisplay, (255,0,0), [verts[e].x, verts[e].y], [verts[u].x, verts[u].y], 2)
	

	o = findPathSimple(1, 3, graph) 
	print(o)
	try:
		if o != None:
			verts[o[0]].display((0,255,0))
			verts[o[-1]].display((0,255,0))
			pygame.draw.line(gameDisplay, (0,255,0), [verts[o[cnt]].x, verts[o[cnt]].y], [verts[o[cnt+1]].x, verts[o[cnt+1]].y], 2)
			verts[o[cnt]].display((0,255,0))
			
		else:
			this_sentence=font_1.render(("nincs lehetoseg"),True,(255,255,255))
			gameDisplay.blit(this_sentence,(10,10))
	
		cnt += 1
	except IndexError:
		cnt = 0
	
	pygame.time.wait(500)
	pygame.display.flip()
	clock = pygame.time.Clock()