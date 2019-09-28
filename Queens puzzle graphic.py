def InitialiseBorad(size):
    '''
    initialise the borad with 0s\n
    borad is a dictionary with coordinates as keys\n
    coordinates starts with 0
    '''
    Borad = {}
    for x in range(size[0]):
        for y in range(size[1]):
            Borad[(x,y)] = 0
    return Borad
def DisplyBorad(Borad):
    '''
    Display the borad\n
    Borad: a dictionary with coordinates as keys\n
    0 for empty, 1 for red, 2 for blue\n
    '''
    global screen
    color = (238,221,130)
    size,pos = (SIZE[0]*50+50, SIZE[1]*50+50),(0,100)
    pygame.draw.rect(screen, color, Rect(pos, size))
    for i in range(1,SIZE[0]+1):
        pygame.draw.rect(screen, (0,0,0), Rect((i*50-1,150), (2,SIZE[1]*50-50)))

    for i in range(1,SIZE[1]+1):
        pygame.draw.rect(screen, (0,0,0), Rect((50,i*50-1+100), (SIZE[1]*50-50,2)))
    for point in Borad:
        p = ((point[0]+1)*50,(point[1]+1)*50+100)
        if Borad[point]==0:
            continue
            #c = (0,0,0)
            #pygame.draw.circle(screen, c, p, 4)
        else:
            if Borad[point]==1:
                c = (255,255,224)
            elif Borad[point]==2:
                c = (0,0,0)
            elif Borad[point]==-1:
                c = (255,255,224)
            elif Borad[point]==-2:
                c = (0,0,0)
            pygame.draw.circle(screen, c, p, 20)
    return screen
def Init():
    '''
    Initialize the borad, the screen and some values
    '''
    global player,Anime,Borad,screen,Borad,loc,SIZE,n,Ssize,OnR
    OnR = False
    n = 8
    loc = []
    Borad = InitialiseBorad(SIZE)
    screen = pygame.display.set_mode((SIZE[0]*50+50, SIZE[1]*50+150), 0, 32)
    screen.fill((0,0,0))
    player = 0
    Anime = 0
    Ssize = (0,0)
def ShoeIndex():
    '''
    Show the Index
    '''
    global screen,index,Ssize
    font = pygame.font.SysFont('impact',50)
    k = font.render(f'{index+1}',True,(255,165,0))
    pygame.draw.rect(screen, (0,0,0), Rect((SIZE[0]*15,30), Ssize))
    Ssize = k.get_width(),k.get_height()
    pygame.draw.rect(screen, (0,0,0), Rect((SIZE[0]*15,30), Ssize))
    screen.blit(k,(SIZE[0]*15,30))
import random,math,copy
n,WinList,trys = int(input('n:')),[],0
QueenList = list(range(n))
while trys<=math.factorial(n)*2 :
    random.shuffle(QueenList)
    trys+=1
    Goo = True
    for i,v in enumerate(QueenList):
        for k,l in enumerate(QueenList):
            if i!=k and abs((v-l)/(k-i)) == 1:
                Goo = False
    if Goo:
        if not QueenList in WinList:
            WinList.append(copy.deepcopy(QueenList))
            print(f'Found {QueenList} in {trys} trys(NO.{len(WinList)})')
            trys = 0
print(f'There are {len(WinList)} solutions')
import pygame
from pygame.locals import *
from sys import exit
import time
SIZE = n,n
pygame.init()
pygame.display.set_caption('Queens')
Init()
index = 0
Down = False
tempT = time.time()
key = 0
while True:
#游戏主循环
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
        if event.type == KEYDOWN and event.key == K_DOWN:
            key = 1
            Down = True
        if event.type == KEYDOWN and event.key == K_UP:
            key = -1
            Down = True
        if event.type == KEYUP:
            Down = False
    if Down and time.time()-tempT>0.15:
        if index<len(WinList)-1 and key == 1:
            index+=key
            tempT = time.time()
        if index>0 and key == -1:
            index+=key
            tempT = time.time()
    Borad = InitialiseBorad((n,n))
    for x,y in enumerate(WinList[index]):
        Borad[(x,y)] = 1
    ShoeIndex()
    DisplyBorad(Borad)
    pygame.display.update()
    #刷新一下画面