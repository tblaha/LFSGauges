# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket
import struct
import pygame, sys
from math import *
from pygame.locals import *

# Create UDP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print "connecting"
# Bind to LFS.
sock.connect(('192.168.1.105', 30000))
#sock.bind(('127.0.0.1', 30000))

print "connected"

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400, 300))
screenrect = screen.get_rect()
pygame.display.set_caption('Hello World!')

radius = 100
rpmmax = (9000,-pi/6)
rpmmin = (0,7*pi/6)
ranget = 8*pi/6
start = (200,250)

print "hello"

#
#while True: # main game loop
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.exit()
#            sys.exit()
#            pygame.display.update()

while True:
    # Receive data.

    data = sock.recv(256)
    print "Daten erhalten"
    if not data:
        break # Lost connection
  
    # Unpack the data.
    outgauge_pack = struct.unpack('I3sxH2B7f2I3f15sx15sx', data)
    time = outgauge_pack[0]
    car = outgauge_pack[1]
    flags = outgauge_pack[2]
    gear = outgauge_pack[3]
    speed = outgauge_pack[5]
    rpm = outgauge_pack[6]
    turbo = outgauge_pack[7]
    engtemp = outgauge_pack[8]
    fuel = outgauge_pack[9]
    oilpressure = outgauge_pack[10]
    oiltemp = outgauge_pack[11]
    dashlights = outgauge_pack[12]
    showlights = outgauge_pack[13]
    throttle = outgauge_pack[14]
    brake = outgauge_pack[15]
    clutch = outgauge_pack[16]
    display1 = outgauge_pack[17]
    display2 = outgauge_pack[18]


    pygame.draw.rect(screen,(0,0,0),screenrect)
    myfont = pygame.font.SysFont("monospace", 15)

    # render text
    label = myfont.render(str(rpm), 1, (255,255,0))
    screen.blit(label, (100, 100))
    
    end   = (start[0]+radius*cos(rpmmin[1]-ranget*rpm/rpmmax[0]),
             start[1]-radius*sin(rpmmin[1]-ranget*rpm/rpmmax[0]))
    
    pygame.draw.line(screen, (255,255,255), start, end, 1)
    
    
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


pygame.quit()
# Release the socket.
sock.close()
