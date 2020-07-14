import pygame
import random
import time
from Classes import *

screensize = (1080,720)

pygame.init()
screen = pygame.display.set_mode(screensize)


def generateTerrain(seed):
    screen.fill((0,200,255))
    weights = [335,335,335]
    points = []
    stonelayer = []
    x = 0
    stonelevel = 0
    mountainreq = 400
    snowreq = 500
    sandreq = 350
    steepness = 2
    distances = 10
    weightchange = 1
    random.seed(seed)
    ypos = random.randint(screensize[1] / 2 - 100,screensize[1] / 2 + 100)
    
    while x < screensize[0]:
        colour = (0,200,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        w = random.randint(0,1000)
        if w <= weights[0]:
            rand = random.randint(1,steepness)
            weights[2] += weightchange
            weights[1] += weightchange
            weights[0] -= weightchange * 2
        elif w > weights[0] and w <= weights[0] + weights[1]:
            rand = random.randint(-steepness,-1)
            weights[2] += weightchange
            weights[1] -= weightchange * 2
            weights[0] += weightchange
        else:
            rand = 0
            weights[2] -= weightchange * 2
            weights[1] += weightchange
            weights[0] += weightchange
        for iiii in range(1,distances):
            if ypos <= screensize[1] - mountainreq:
                colour = (125,125,125)
            if ypos <= screensize[1] - snowreq:
                colour = (255,255,255)
            if ypos >= screensize[1] - sandreq:
                colour = (255,255,100)
                
            if rand > 0:
                for i in range(0,rand):
                    points.append(point(colour,(x,ypos)))
                    ypos += 1
            elif rand < 0:
                for i in range(rand,0):
                    points.append(point(colour,(x,ypos)))
                    ypos -= 1
            else:
                points.append(point(colour,(x,ypos)))
            x += 1
            
        if ypos < 0:
            ypos = 0
        elif ypos > screensize[1]:
            ypos = screensize[1]


    stoneY = stonelevel
    pygame.draw.rect(screen,(0,100,255),[0,screensize[1]-sandreq + 2,screensize[0],screensize[1]-sandreq - 2])
    for p in points:
        stoneRan = steepness
        stoneY += random.randint(-stoneRan,stoneRan)
        if stoneY - p.position[1] < 100:
            stoneY = p.position[1] + 100
        if stoneY < p.position[1]:
            stoneY = p.position[1]
        stonelayer.append(point((125,125,125),(int(p.position[0]),int(stoneY))))
            

    for i in range(0,len(points)):
        p = points[i]
        y = p.position[1]
        while y < screensize[1]:
            c = (200,200,0)
            if (p.colour == (125,125,125) or p.colour == (255,255,255)) and y < screensize[1] - mountainreq:
                c =(125,125,125)
            
            if y >= stonelayer[i].position[1]:
                c = (125,125,125)
                pass
                
            pygame.draw.circle(screen,c,(int(p.position[0]),int(y)),1)
            y += 1
            
    for i in range(0,len(points)):
        p = points[i]      
            
        pygame.draw.circle(screen,p.colour,(int(p.position[0]),int(p.position[1])),3)
    pygame.display.update()

x = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    generateTerrain(x)
    x = time.time()
    t = time.time()
    while (time.time()- t) < 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pass
