# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame, random, sys
from pygame.locals import*

pygame.init()

indexclicked=500
BOARDHEIGHT = 800
BOARDWIDTH = 1400
RIGHTBOARDERWIDTH = 500
LEFTBOARDERWIDTH = 20
SIDEBOARDERHEIGHT = 20
BOXSIZE = 30
placed=[]
rotated90=[]
rotated180=[]
rotated270=[]
version=0
DISPLAYSURF = pygame.display.set_mode((BOARDWIDTH,BOARDHEIGHT))
pygame.display.set_caption('Puzzle')
DISPLAYSURF.fill((247,143,167))
finished=[]
finishedindex=[]
lakecopy=pygame.image.load('lake - Copy.jpg')
treecopy=pygame.image.load('tree - Copy.jpg')
rivercopy=pygame.image.load('river - Copy.png')
river=pygame.image.load('river.png')
treecopy2=pygame.image.load('tree - Copy (2).jpg')
lakecopy2=pygame.image.load('lake - Copy (2).jpg')
rivercopy2=pygame.image.load('river - Copy (2).png')
tree=pygame.image.load('tree.jpg')
tree1=pygame.image.load('tree1.png')
tree2=pygame.image.load('tree2.png')
tree3=pygame.image.load('tree3.png')
tree4=pygame.image.load('tree4.png')
treepieces=[tree1, tree2, tree3, tree4]
lake=pygame.image.load('lake.jpg')
lake1=pygame.image.load('lake1.png')
lake2=pygame.image.load('lake2.png')
lake3=pygame.image.load('lake3.png')
lake4=pygame.image.load('lake4.png')
lake5=pygame.image.load('lake5.png')
lake6=pygame.image.load('lake6.png')
lake7=pygame.image.load('lake7.png')
lake8=pygame.image.load('lake8.png')
lake9=pygame.image.load('lake9.png')
lake10=pygame.image.load('lake10.png')
lake11=pygame.image.load('lake11.png')
lake12=pygame.image.load('lake12.png')
lake13=pygame.image.load('lake13.png')
lake14=pygame.image.load('lake14.png')
lake15=pygame.image.load('lake15.png')
lake16=pygame.image.load('lake16.png')
lakepieces=[lake1, lake2, lake3, lake4, lake5, lake6, lake7, lake8, lake9, lake10, lake11, lake12, lake13, lake14, lake15, lake16]
river1= pygame.image.load('river1.png')
river2= pygame.image.load('river2.png')
river3= pygame.image.load('river3.png')
river4= pygame.image.load('river4.png')
river5= pygame.image.load('river5.png')
river6= pygame.image.load('river6.png')
river7= pygame.image.load('river7.png')
river8= pygame.image.load('river8.png')
river9= pygame.image.load('river9.png')
river10= pygame.image.load('river10.png')
river11= pygame.image.load('river11.png')
river12= pygame.image.load('river12.png')
river13= pygame.image.load('river13.png')
river14= pygame.image.load('river14.png')
river15= pygame.image.load('river15.png')
river16= pygame.image.load('river16.png')
river17= pygame.image.load('river17.png')
river18= pygame.image.load('river18.png')
river19= pygame.image.load('river19.png')
river20= pygame.image.load('river20.png')
river21= pygame.image.load('river21.png')
river22= pygame.image.load('river22.png')
river23= pygame.image.load('river23.png')
river24= pygame.image.load('river24.png')
river25= pygame.image.load('river25.png')
river26= pygame.image.load('river26.png')
river27= pygame.image.load('river27.png')
river28= pygame.image.load('river28.png')
river29= pygame.image.load('river29.png')
river30= pygame.image.load('river30.png')
river31= pygame.image.load('river31.png')
river32= pygame.image.load('river32.png')
river33= pygame.image.load('river33.png')
river34= pygame.image.load('river34.png')
river35= pygame.image.load('river35.png')
river36= pygame.image.load('river36.png')
river37= pygame.image.load('river37.png')
river38= pygame.image.load('river38.png')
river39= pygame.image.load('river39.png')
river40= pygame.image.load('river40.png')
river41= pygame.image.load('river41.png')
river42= pygame.image.load('river42.png')
river43= pygame.image.load('river43.png')
river44= pygame.image.load('river44.png')
river45= pygame.image.load('river45.png')
river46= pygame.image.load('river46.png')
river47= pygame.image.load('river47.png')
river48= pygame.image.load('river48.png')
river49= pygame.image.load('river49.png')
river50= pygame.image.load('river50.png')
river51= pygame.image.load('river51.png')
river52= pygame.image.load('river52.png')
river53= pygame.image.load('river53.png')
river54= pygame.image.load('river54.png')
river55= pygame.image.load('river55.png')
river56= pygame.image.load('river56.png')
river57= pygame.image.load('river57.png')
river58= pygame.image.load('river58.png')
river59= pygame.image.load('river59.png')
river60= pygame.image.load('river60.png')
river61= pygame.image.load('river61.png')
river62= pygame.image.load('river62.png')
river63= pygame.image.load('river63.png')
river64= pygame.image.load('river64.png')
river65= pygame.image.load('river65.png')
river66= pygame.image.load('river66.png')
river67= pygame.image.load('river67.png')
river68= pygame.image.load('river68.png')
river69= pygame.image.load('river69.png')
river70= pygame.image.load('river70.png')
river71= pygame.image.load('river71.png')
river72= pygame.image.load('river72.png')
river73= pygame.image.load('river73.png')
river74= pygame.image.load('river74.png')
river75= pygame.image.load('river75.png')
river76= pygame.image.load('river76.png')
river77= pygame.image.load('river77.png')
river78= pygame.image.load('river78.png')
river79= pygame.image.load('river79.png')
river80= pygame.image.load('river80.png')
river81= pygame.image.load('river81.png')
river82= pygame.image.load('river82.png')
river83= pygame.image.load('river83.png')
river84= pygame.image.load('river84.png')
river85= pygame.image.load('river85.png')
river86= pygame.image.load('river86.png')
river87= pygame.image.load('river87.png')
river88= pygame.image.load('river88.png')
river89= pygame.image.load('river89.png')
river90= pygame.image.load('river90.png')
river91= pygame.image.load('river91.png')
river92= pygame.image.load('river92.png')
river93= pygame.image.load('river93.png')
river94= pygame.image.load('river94.png')
river95= pygame.image.load('river95.png')
river96= pygame.image.load('river96.png')
river97= pygame.image.load('river97.png')
river98= pygame.image.load('river98.png')
river99= pygame.image.load('river99.png')
river100= pygame.image.load('river100.png')
riverpieces=[river1, river2, river3, river4, river5, river6, river7, river8, river9, river10, river11, river12, river13, river14, river15, river16, river17, river18, river19, river20, river21, river22, river23, river24, river25, river26, river27, river28, river29, river30, river31, river32, river33, river34, river35, river36, river37, river38, river39, river40, river41, river42, river43, river44, river45, river46, river47, river48, river49, river50, river51, river52, river53, river54, river55, river56, river57, river58, river59, river60, river61, river62, river63, river64, river65, river66, river67, river68, river69, river70, river71, river72, river73, river74, river75, river76, river77, river78, river79, river80, river81, river82, river83, river84, river85, river86, river87, river88, river89, river90, river91, river92, river93, river94, river95, river96, river97, river98, river99, river100]
def shoinfo():
    DISPLAYSURF = pygame.display.set_mode((600, 300))
    DISPLAYSURF.fill((247, 143, 167))
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (12.5, 45), 5)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('Click and drag to move pieces to the correct position', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 40))
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (12.5, 90), 5)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('Hover your mouse over a piece and press SPACE to rotate', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 80))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('it', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 100))
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (12.5, 145), 5)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('Click the image to enlarge it. Press the + or - to zoom in', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 140))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render( 'and out. Use the arrow keys to move the image',  True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 160))
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj = fontObj.render('BACK', True, (255, 255, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (22, 10)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (12.5, 207), 5)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('If you get stuck, hover over an empty area of your puzzle ', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 200))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('and press H for a hint. Be careful; you have a limited ', True,(255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 220))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('number of hints', True,(255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 240))
    pygame.display.update()
def hintriver(mousex, mousey):
    i=0
    a=0
    while i<600:
        j=0
        while j<600:
            if i<=mousey<i+60 and j<=mousex<j+60:
                finalindex=a
            j+=60
            a+=1
        i+=60
    temp=placed.index(finalindex+1)
    finished.append(finalindex)
    finishedindex.append(temp)
    makeboardriver(500)
def blitrotatedriver(index, angle, x, y):
    if angle==270:
        rotated_piece = pygame.transform.rotate(riverpieces[index-1], 270)
        DISPLAYSURF.blit(rotated_piece, (x-519, y))
    elif angle==180:
        rotated_piece = pygame.transform.rotate(riverpieces[index - 1], 180)
        DISPLAYSURF.blit(rotated_piece, (x-519, y-519))
    elif angle==90:
        rotated_piece = pygame.transform.rotate(riverpieces[index - 1], 90)
        DISPLAYSURF.blit(rotated_piece, (x, y-519))
def scatterriver():
    finished.clear()
    placed.clear()
    finishedindex.clear()
    rotated90.clear()
    rotated180.clear()
    rotated270.clear()
    int=0
    i=BOARDHEIGHT-80
    while i>=0:
        j=BOARDWIDTH-80
        while j>=0:
            if (i >= 600 or j >= 600) and j>200 and len(placed)<100:
                while (int in placed or int==0) and len(placed)<100 :
                    int=random.randint(1,100)
                temp=random.randint(1,4)
                if temp==2:
                    rotated90.append(int)
                    blitrotatedriver(int, 90, j, i)
                elif temp==3:
                    rotated180.append(int)
                    blitrotatedriver(int, 180, j, i)
                elif temp==4:
                    rotated270.append(int)
                    blitrotatedriver(int, 270, j, i)
                elif temp==1:
                    DISPLAYSURF.blit(riverpieces[int - 1], (j, i))
                placed.append(int)
            j-=80
        i-=80

    pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
    rivercopy = pygame.image.load('river - Copy.png')
    DISPLAYSURF.blit(rivercopy, (75,625))
def makeriverpuzzle():
    pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
    a = 0
    i = 0
    while i < 600:
        j = 0
        while j < 600:
            if a in finished:
                DISPLAYSURF.blit(riverpieces[a], (j - 11, i - 11))
            j += 60
            a += 1
        i += 60
def makeboardriver(index):

    DISPLAYSURF.fill((247, 143, 167))
    a=0
    i=BOARDHEIGHT-80
    while i>=0:
        j=BOARDWIDTH-80
        while j>=0:
            if (i >= 600 or j >= 600) and j>120 and a<100:
                if placed[a] in rotated270:
                    blitrotatedriver(placed[a], 270, j, i)
                elif placed[a] in rotated180:
                    blitrotatedriver(placed[a], 180, j, i)
                elif placed[a] in rotated90:
                    blitrotatedriver(placed[a], 90, j, i)
                else:
                    DISPLAYSURF.blit(riverpieces[placed[a]-1], (j,i))

                if (a==index and index!=500) or a in finishedindex:
                    pygame.draw.rect(DISPLAYSURF, (247,143,167), (j , i , 81, 81))
                a+=1
            j-=80
        i-=80

    pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
    rivercopy = pygame.image.load('river - Copy.png')
    DISPLAYSURF.blit(rivercopy, (75,625))
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (75, 735, 100, 50), 1)
    fontObj = pygame.font.Font('freesansbold.ttf', 30)
    textSurfaceObj = fontObj.render('Menu', True, (255, 255, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (125, 760)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (32, 760), 20, 1)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('?', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 750))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('Hints:', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (10, 603))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(hint), True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (72, 603))
    makeriverpuzzle()
def hintlake(mousex, mousey):
    i=0
    a=0
    while i<600:
        j=0
        while j<600:
            if i<=mousey<i+150 and j<=mousex<j+150:
                finalindex=a
            j+=150
            a+=1
        i+=150
    temp=placed.index(finalindex+1)
    finished.append(finalindex)
    finishedindex.append(temp)
    makeboardlake(500)
def blitrotatedlake(index, angle, x, y):
    if angle==270:
        rotated_piece = pygame.transform.rotate(lakepieces[index-1], 270)
        DISPLAYSURF.blit(rotated_piece, (x-401, y))
    elif angle==180:
        rotated_piece = pygame.transform.rotate(lakepieces[index - 1], 180)
        DISPLAYSURF.blit(rotated_piece, (x-401, y-401))
    elif angle==90:
        rotated_piece = pygame.transform.rotate(lakepieces[index - 1], 90)
        DISPLAYSURF.blit(rotated_piece, (x, y-401))
def scatterlake():
    placed.clear()
    finished.clear()
    finishedindex.clear()
    rotated90.clear()
    rotated180.clear()
    rotated270.clear()
    int=0
    i=BOARDHEIGHT-200
    while i>=0:
        j=BOARDWIDTH-200
        while j>=0:
            if (i >= 600 or j >= 600) and j>200 and len(placed)<16:
                while (int in placed or int==0) and len(placed)<16 :
                    int=random.randint(1,16)
                temp = random.randint(1, 4)
                if temp == 2:
                    rotated90.append(int)
                    blitrotatedlake(int, 90, j, i)
                elif temp == 3:
                    rotated180.append(int)
                    blitrotatedlake(int, 180, j, i)
                elif temp == 4:
                    rotated270.append(int)
                    blitrotatedlake(int, 270, j, i)
                elif temp == 1:
                    DISPLAYSURF.blit(lakepieces[int - 1], (j, i))
                placed.append(int)
            j-=200
        i-=200
    pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
    lakecopy = pygame.image.load('lake - Copy.jpg')
    DISPLAYSURF.blit(lakecopy, (75,625))
def makelakepuzzle():
    pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
    a = 0
    i = 0
    while i < 600:
        j = 0
        while j < 600:
            if a in finished:
                DISPLAYSURF.blit(lakepieces[a], (j - 25, i - 25))
            j += 150
            a += 1
        i += 150
def makeboardlake(index):
    DISPLAYSURF.fill((247, 143, 167))
    a=0
    i=BOARDHEIGHT-200
    while i>=0:
        j=BOARDWIDTH-200
        while j>=0:
            if (i >= 600 or j >= 600) and j>200 and a<16:
                if placed[a] in rotated270:
                    blitrotatedlake(placed[a], 270, j, i)
                elif placed[a] in rotated180:
                    blitrotatedlake(placed[a], 180, j, i)
                elif placed[a] in rotated90:
                    blitrotatedlake(placed[a], 90, j, i)
                else:
                    DISPLAYSURF.blit(lakepieces[placed[a]-1], (j,i))
                if (a==index and index!=500) or a in finishedindex:
                    pygame.draw.rect(DISPLAYSURF, (247,143,167), (j , i , 201, 201))
                a+=1
            j-=200
        i-=200

    pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
    lake = pygame.image.load('lake - Copy.jpg')
    DISPLAYSURF.blit(lake, (75,625))
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (75, 735, 100, 50), 1)
    fontObj = pygame.font.Font('freesansbold.ttf', 30)
    textSurfaceObj = fontObj.render('Menu', True, (255, 255, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (125, 760)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (32, 760), 20, 1)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('?', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 750))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('Hints:', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (10, 603))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(hint), True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (72, 603))
    makelakepuzzle()
def hinttree(mousex, mousey):
    i=0
    a=0
    while i<600:
        j=0
        while j<600:
            if i<=mousey<i+300 and j<=mousex<j+300:
                finalindex=a
            j+=300
            a+=1
        i+=300
    temp=placed.index(finalindex+1)
    finished.append(finalindex)
    finishedindex.append(temp)
    makeboardtree(500)
def blitrotatedtree(index, angle, x, y):
    if angle==270:
        rotated_piece = pygame.transform.rotate(treepieces[index-1], 270)
        DISPLAYSURF.blit(rotated_piece, (x-199, y))
    elif angle==180:
        rotated_piece = pygame.transform.rotate(treepieces[index - 1], 180)
        DISPLAYSURF.blit(rotated_piece, (x-199, y-199))
    elif angle==90:
        rotated_piece = pygame.transform.rotate(treepieces[index - 1], 90)
        DISPLAYSURF.blit(rotated_piece, (x, y-199))
def scattertree():
    placed.clear()
    finished.clear()
    rotated90.clear()
    rotated180.clear()
    rotated270.clear()
    finishedindex.clear()
    int=0
    i=BOARDHEIGHT-400
    while i>=0:
        j=BOARDWIDTH-400
        while j>=0:
            if (i >= 600 or j >= 600) and j>200 and len(placed)<4:
                while (int in placed or int==0) and len(placed)<4 :
                    int=random.randint(1,4)
                temp = random.randint(1, 4)
                if temp == 2:
                    rotated90.append(int)
                    blitrotatedtree(int, 90, j, i)
                elif temp == 3:
                    rotated180.append(int)
                    blitrotatedtree(int, 180, j, i)
                elif temp == 4:
                    rotated270.append(int)
                    blitrotatedtree(int, 270, j, i)
                elif temp == 1:
                    DISPLAYSURF.blit(treepieces[int - 1], (j, i))
                placed.append(int)

                
            j-=400
        i-=400

    pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
    treecopy = pygame.image.load('tree - Copy.jpg')
    DISPLAYSURF.blit(treecopy, (75,625))
def maketreepuzzle():
    pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
    a = 0
    i = 0
    while i < 600:
        j = 0
        while j < 600:
            if a in finished:
                DISPLAYSURF.blit(treepieces[a], (j - 51, i - 51))
            j += 300
            a += 1
        i += 300
def makeboardtree(index):
    DISPLAYSURF.fill((247, 143, 167))
    a=0
    i=BOARDHEIGHT-400
    while i>=0:
        j=BOARDWIDTH-400
        while j>=0:
            if (i >= 600 or j >= 600) and j>200 and a<4:
                if placed[a] in rotated270:
                    blitrotatedtree(placed[a], 270, j, i)
                elif placed[a] in rotated180:
                    blitrotatedtree(placed[a], 180, j, i)
                elif placed[a] in rotated90:
                    blitrotatedtree(placed[a], 90, j, i)
                else:
                    DISPLAYSURF.blit(treepieces[placed[a] - 1], (j, i))
                if (a==index and index!=500) or a in finishedindex:
                    pygame.draw.rect(DISPLAYSURF, (247,143,167), (j , i , 401, 401))
                a+=1
            j-=400
        i-=400

    pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
    tree = pygame.image.load('tree - Copy.jpg')
    DISPLAYSURF.blit(tree, (75,625))
    pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (75, 735, 100, 50), 1)
    fontObj = pygame.font.Font('freesansbold.ttf', 30)
    textSurfaceObj = fontObj.render('Menu', True, (255, 255, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (125, 760)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (32, 760), 20, 1)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('?', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (25, 750))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render('Hints:', True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (10, 603))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(str(hint), True, (255, 255, 255))
    DISPLAYSURF.blit(textSurfaceObj, (72, 603))
    maketreepuzzle()
while True:
    if version==0:
        DISPLAYSURF.fill((247, 143, 167))
        fontObj = pygame.font.Font('freesansbold.ttf', 50)
        textSurfaceObj = fontObj.render('Choose a puzzle', True, (255, 255, 255))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (700, 100)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        DISPLAYSURF.blit(treecopy2, (50, 300))
        DISPLAYSURF.blit(lakecopy2, (500, 300))
        DISPLAYSURF.blit(rivercopy2, (950, 300))
        fontObj = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceObj = fontObj.render('Easy - 4 pieces', True, (255, 255, 255))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 275)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        fontObj = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceObj = fontObj.render('Medium - 16 pieces', True, (255, 255, 255))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (700, 275)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        fontObj = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceObj = fontObj.render('Hard - 100 pieces', True, (255, 255, 255))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (1150, 275)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type==MOUSEBUTTONDOWN:
                if 50<mousex<450 and 300<mousey<700:
                    version=1
                    scattertree()
                    hint=1
                elif 500<mousex<900 and 300<mousey<700:
                    version=2
                    scatterlake()
                    hint=2
                elif 950<mousex<1350 and 300<mousey<700:
                    version=3
                    hint=5
                    scatterriver()
    if version==1:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                if indexclicked!=500:
                    makeboardtree(indexclicked)
                    if placed[indexclicked] in rotated270:
                        blitrotatedtree(placed[indexclicked], 270, mousex - 200, mousey - 200)
                    elif placed[indexclicked] in rotated180:
                        blitrotatedtree(placed[indexclicked], 180, mousex - 200, mousey - 200)
                    elif placed[indexclicked] in rotated90:
                        blitrotatedtree(placed[indexclicked], 90, mousex - 200, mousey - 200)
                    else:
                        DISPLAYSURF.blit(treepieces[placed[indexclicked] - 1], (mousex - 200, mousey - 200))

                    if mousex<400 and mousey<400:
                        maketreepuzzle()
                        if placed[indexclicked] in rotated270:
                            blitrotatedtree(placed[indexclicked], 270, mousex-200, mousey-200)
                        elif placed[indexclicked] in rotated180:
                            blitrotatedtree(placed[indexclicked], 180, mousex-200, mousey-200)
                        elif placed[indexclicked] in rotated90:
                            blitrotatedtree(placed[indexclicked], 90, mousex-200, mousey-200)
                        else:
                            DISPLAYSURF.blit(treepieces[placed[indexclicked] - 1], (mousex - 200, mousey - 200))
            elif event.type==MOUSEBUTTONDOWN:
                if (mousex<600 and mousey<600) or mousex<600:
                    indexclicked=500
                    if 75<mousex<175 and 735<mousey<785:
                        version=0
                    elif 12 < mousex < 52 and 740 < mousey < 780:
                        showinfo = True
                        shoinfo()
                        pygame.display.update()
                        while showinfo:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == MOUSEMOTION:
                                    mousex, mousey=event.pos
                                elif event.type==MOUSEBUTTONDOWN and mousey<20 and mousex<40:
                                    showinfo=False
                                    DISPLAYSURF = pygame.display.set_mode((1400, 800))
                    elif 75 < mousex < 175 and 625 < mousey < 725:
                        gopicture = True
                        zoom = 0
                        DISPLAYSURF = pygame.display.set_mode((600, 600))
                        DISPLAYSURF.blit(tree, (0, 0))
                        blitx = 0
                        blity = 0
                        picture = tree
                        squaresize=0
                        squarex=0
                        squarey=500
                        while gopicture:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == MOUSEMOTION:
                                    mousex, mousey = event.pos

                                elif event.type == MOUSEBUTTONDOWN:
                                    if 580 < mousex and 580 < mousey:
                                        blity = 0
                                        blitx = 0
                                        squarex = 0
                                        squarey = 500
                                        if zoom == 0:
                                            zoom += 1
                                            squaresize=75
                                            picture = pygame.transform.scale(tree, (800, 800))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                        elif zoom == 1:
                                            zoom += 1
                                            squaresize=60
                                            picture = pygame.transform.scale(tree, (1000, 1000))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                        elif zoom == 2:
                                            zoom += 1
                                            squaresize=50
                                            picture = pygame.transform.scale(tree, (1200, 1200))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                    elif 580 < mousex and 550 < mousey < 580:
                                        blity = 0
                                        blitx = 0
                                        squarex = 0
                                        squarey = 500
                                        if zoom == 1:
                                            zoom -= 1
                                            squaresize=0
                                            picture = pygame.transform.scale(tree, (600, 600))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                        elif zoom == 2:
                                            zoom -= 1
                                            squaresize=75
                                            picture = pygame.transform.scale(tree, (800, 800))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                        elif zoom == 3:
                                            zoom -= 1
                                            squaresize=60
                                            picture = pygame.transform.scale(tree, (1000, 1000))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                    elif mousex < 40 and mousey < 20:
                                        gopicture = False
                                        DISPLAYSURF = pygame.display.set_mode((1400, 800))
                                elif event.type == KEYDOWN and event.key == K_RIGHT:
                                    if zoom == 3:
                                        if blitx > -590:
                                            blitx -= 10
                                            squarex+=.833
                                    elif zoom == 2:
                                        if blitx > -390:
                                            blitx -= 10
                                            squarex+=1
                                    elif zoom == 1:
                                        if blitx > -190:
                                            blitx -= 10
                                            squarex+=1.25
                                    DISPLAYSURF.blit(picture, (blitx, blity))
                                elif event.type == KEYDOWN and event.key == K_LEFT:
                                    if blitx < 0:
                                        blitx += 10

                                        if zoom == 3:

                                            squarex -= .833
                                        elif zoom == 2:

                                            squarex -= 1
                                        elif zoom == 1:
                                            squarex -= 1.25
                                    DISPLAYSURF.blit(picture, (blitx, blity))
                                elif event.type == KEYDOWN and event.key == K_DOWN:
                                    if zoom == 3:
                                        if blity > -590:
                                            blity -= 10
                                            squarey+=.8333
                                    elif zoom == 2:
                                        if blity > -390:
                                            blity -= 10
                                            squarey+=1
                                    elif zoom == 1:
                                        if blity > -190:
                                            blity -= 10
                                            squarey+=1.25

                                    DISPLAYSURF.blit(picture, (blitx, blity))
                                elif event.type == KEYDOWN and event.key == K_UP:
                                    if blity < 0:
                                        blity += 10
                                        if zoom == 3:

                                            squarey -= .833
                                        elif zoom == 2:

                                            squarey -= 1
                                        elif zoom == 1:
                                            squarey -= 1.25
                                    DISPLAYSURF.blit(picture, (blitx, blity))
                            fontObj = pygame.font.Font('freesansbold.ttf', 40)
                            textSurfaceObj = fontObj.render('+', True, (255, 255, 255))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (590, 590)
                            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                            fontObj = pygame.font.Font('freesansbold.ttf', 40)
                            textSurfaceObj = fontObj.render('-', True, (255, 255, 255))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (590, 560)
                            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                            fontObj = pygame.font.Font('freesansbold.ttf', 15)
                            textSurfaceObj = fontObj.render('BACK', True, (255, 255, 255))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (22, 10)
                            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                            DISPLAYSURF.blit(treecopy, (0,500))
                            pygame.draw.rect(DISPLAYSURF, (255,255,255), (squarex, squarey, squaresize, squaresize),1)
                            pygame.display.update()
                elif len(finished)!=4:
                    indexclicked = 0
                    a = 0
                    i = BOARDHEIGHT
                    while i >= 0:
                        j = BOARDWIDTH
                        while j >= 0:
                            if i - 400 < mousey < i and j - 400 < mousex < j:
                                indexclicked = a
                                if placed[indexclicked]-1 in finished:
                                    indexclicked=500
                            j -= 400
                            if (i >= 900 or j >= 600) and j > 200:
                                a += 1
                        i -= 400
                makeboardtree(indexclicked)
            elif event.type==KEYDOWN and event.key==K_h:
                if hint>0 and mousex<600 and mousey<600:
                    hint -= 1
                    hinttree(mousex, mousey)
            elif event.type==KEYDOWN and event.key==K_SPACE:
                if (mousex>600 or mousey>600) and mousex>120:
                    if len(finished) != 4:
                        tempindex = 0
                        a = 0
                        i = BOARDHEIGHT
                        while i >= 0:
                            j = BOARDWIDTH
                            while j >= 0:
                                if i - 400 < mousey < i and j - 400 < mousex < j:
                                    tempindex = a
                                    if placed[tempindex] - 1 in finished:
                                        tempindex = 500
                                j -= 400
                                if (i >= 90 or j >= 600) and j > 200:
                                    a += 1
                            i -= 400
                    a = 0
                    i = BOARDHEIGHT - 400
                    while i >= 0:
                        j = BOARDWIDTH - 400
                        while j >= 0:
                            if (i >= 600 or j >= 600) and j > 120 and a < 4:
                                if (a == tempindex and tempindex != 500):
                                    pygame.draw.rect(DISPLAYSURF, (247, 143, 167), (j, i, 81, 81))
                                    if placed[tempindex] in rotated270:
                                        rotated270.remove(placed[tempindex])
                                    elif placed[tempindex] in rotated180:
                                        rotated180.remove(placed[tempindex])
                                        rotated270.append(placed[tempindex])
                                    elif placed[tempindex] in rotated90:
                                        rotated90.remove(placed[tempindex])
                                        rotated180.append(placed[tempindex])
                                    else:
                                        rotated90.append(placed[tempindex])
                                a += 1
                            j -= 400
                        i -= 400
                    makeboardtree(500)
            elif event.type==MOUSEBUTTONUP:
                if indexclicked!=500:
                    tempindex=placed[indexclicked]-1

                    i=0
                    a=0
                    while i<600:
                        j=0
                        while j<600:

                            if tempindex==a and j<mousex<j+300 and i<mousey<i+300 and tempindex+1 not in rotated90 and tempindex+1 not in rotated180 and tempindex+1 not in rotated270:
                                pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
                                DISPLAYSURF.blit(treepieces[placed[indexclicked]-1], (j-51,i-51))
                                finished.append(tempindex)
                                finishedindex.append(indexclicked)
                            j+=300
                            a+=1
                        i+=300

                indexclicked=500
                makeboardtree(indexclicked)
                if len(finished)==4:
                    fontObj = pygame.font.Font('freesansbold.ttf', 50)
                    textSurfaceObj = fontObj.render('You Win', True, (255,255,255))
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (1000,400)
                    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                    tree=pygame.image.load('tree.jpg')
                    DISPLAYSURF.blit(tree, (0,0))
    if version==2:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                if indexclicked!=500:
                    makeboardlake(indexclicked)
                    if placed[indexclicked] in rotated270:
                        blitrotatedlake(placed[indexclicked], 270, mousex - 100, mousey - 100)
                    elif placed[indexclicked] in rotated180:
                        blitrotatedlake(placed[indexclicked], 180, mousex - 100, mousey - 100)
                    elif placed[indexclicked] in rotated90:
                        blitrotatedlake(placed[indexclicked], 90, mousex - 100, mousey - 100)
                    else:
                        DISPLAYSURF.blit(lakepieces[placed[indexclicked] - 1], (mousex - 100, mousey - 100))

                    if mousex<500 and mousey<500:
                        makelakepuzzle()
                        if placed[indexclicked] in rotated270:
                            blitrotatedlake(placed[indexclicked], 270, mousex-100, mousey-100)
                        elif placed[indexclicked] in rotated180:
                            blitrotatedlake(placed[indexclicked], 180, mousex-100, mousey-100)
                        elif placed[indexclicked] in rotated90:
                            blitrotatedlake(placed[indexclicked], 90, mousex-100, mousey-100)
                        else:
                            DISPLAYSURF.blit(lakepieces[placed[indexclicked] - 1], (mousex - 100, mousey - 100))

            elif event.type==MOUSEBUTTONDOWN:
                if (mousex<600 and mousey<600) or mousex<400:
                    indexclicked=500
                    if 75<mousex<175 and 735<mousey<785:
                        version=0
                    elif 12 < mousex < 52 and 740 < mousey < 780:
                        showinfo = True
                        shoinfo()
                        pygame.display.update()
                        while showinfo:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == MOUSEMOTION:
                                    mousex, mousey=event.pos
                                elif event.type==MOUSEBUTTONDOWN and mousey<20 and mousex<40:
                                    showinfo=False
                                    DISPLAYSURF = pygame.display.set_mode((1400, 800))
                    elif 75<mousex<175 and 625<mousey<725:
                        gopicture=True
                        zoom=0
                        DISPLAYSURF = pygame.display.set_mode((600,600))
                        DISPLAYSURF.blit(lake, (0, 0))
                        blitx=0
                        blity=0
                        picture=lake
                        squarex=0
                        squarey=500
                        squaresize=0
                        while gopicture:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == MOUSEMOTION:
                                    mousex, mousey = event.pos

                                elif event.type == MOUSEBUTTONDOWN:
                                    if 580<mousex and 580<mousey:
                                        squarex=0
                                        squarey=500
                                        blity=0
                                        blitx=0
                                        if zoom==0:
                                            zoom+=1
                                            squaresize=75
                                            picture=pygame.transform.scale(lake, (800,800))
                                            DISPLAYSURF.blit(picture, (blitx,blity))
                                        elif zoom==1:
                                            zoom+=1
                                            squaresize=60
                                            picture = pygame.transform.scale(lake, (1000, 1000))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                        elif zoom==2:
                                            zoom+=1
                                            squaresize=50
                                            picture = pygame.transform.scale(lake, (1200, 1200))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                    elif 580<mousex and 550<mousey<580:
                                        squarex=0
                                        squarey=500
                                        blity=0
                                        blitx=0
                                        if zoom==1:
                                            zoom-=1
                                            squaresize=0
                                            picture=pygame.transform.scale(lake, (600,600))
                                            DISPLAYSURF.blit(picture, (blitx,blity))
                                        elif zoom==2:
                                            zoom-=1
                                            squaresize=75
                                            picture = pygame.transform.scale(lake, (800, 800))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                        elif zoom==3:
                                            zoom-=1
                                            squaresize=60
                                            picture = pygame.transform.scale(lake, (1000, 1000))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                    elif mousex<40 and mousey<20:
                                        gopicture=False
                                        DISPLAYSURF = pygame.display.set_mode((1400, 800))
                                elif event.type==KEYDOWN and event.key==K_RIGHT:
                                    if zoom==3:
                                        if blitx>-590:
                                            blitx-=10
                                            squarex+=.833333
                                    elif zoom==2:
                                        if blitx>-390:
                                            blitx-=10
                                            squarex+=1
                                    elif zoom==1:
                                        if blitx>-190:
                                            blitx-=10
                                            squarex+=1.25
                                    DISPLAYSURF.blit(picture, (blitx, blity))
                                elif event.type==KEYDOWN and event.key==K_LEFT:
                                    if blitx<0:
                                        blitx+=10
                                        if zoom==3:
                                            squarex-=.83333333
                                        elif zoom==2:
                                            squarex-=1
                                        elif zoom==1:
                                            squarex-=1.25
                                    DISPLAYSURF.blit(picture, (blitx, blity))
                                elif event.type==KEYDOWN and event.key==K_DOWN:
                                    if zoom == 3:
                                        if blity > -590:
                                            blity -= 10
                                            squarey+=.8333333
                                    elif zoom == 2:
                                        if blity > -390:
                                            blity -= 10
                                            squarey+=1
                                    elif zoom == 1:
                                        if blity > -190:
                                            blity -= 10
                                            squarey+=1.25

                                    DISPLAYSURF.blit(picture, (blitx, blity))
                                elif event.type==KEYDOWN and event.key==K_UP:
                                    if blity<0:
                                        blity+=10
                                        if zoom==3:
                                            squarey-=.8333333
                                        elif zoom==2:
                                            squarey-=1
                                        elif zoom==1:
                                            squarey-=1.25
                                    DISPLAYSURF.blit(picture, (blitx, blity))
                            fontObj = pygame.font.Font('freesansbold.ttf', 40)
                            textSurfaceObj = fontObj.render('+', True, (255, 255, 255))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (590, 590)
                            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                            fontObj = pygame.font.Font('freesansbold.ttf', 40)
                            textSurfaceObj = fontObj.render('-', True, (255, 255, 255))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (590, 560)
                            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                            fontObj = pygame.font.Font('freesansbold.ttf', 15)
                            textSurfaceObj = fontObj.render('BACK', True, (255, 255, 255))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (22, 10)
                            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                            DISPLAYSURF.blit(lakecopy, (0,500))
                            pygame.draw.rect(DISPLAYSURF, (255,255,255),(squarex, squarey, squaresize, squaresize),1)
                            pygame.display.update()
                elif len(finished)!=16:
                    indexclicked = 0
                    a = 0
                    i = BOARDHEIGHT
                    while i >= 0:
                        j = BOARDWIDTH
                        while j >= 0:
                            if i - 200 < mousey < i and j - 200 < mousex < j:
                                indexclicked = a
                                if placed[indexclicked]-1 in finished:
                                    indexclicked=500
                            j -= 200
                            if (i >= 750 or j >= 600) and j > 200:
                                a += 1
                        i -= 200
                makeboardlake(indexclicked)
            elif event.type==KEYDOWN and event.key==K_h:
                if hint>0 and mousex<600 and mousey<600:
                    hint -= 1
                    hintlake(mousex, mousey)
            elif event.type==KEYDOWN and event.key==K_SPACE:
                if (mousex>600 or mousey>600) and mousex>120:
                    if len(finished) != 16:
                        tempindex = 0
                        a = 0
                        i = BOARDHEIGHT
                        while i >= 0:
                            j = BOARDWIDTH
                            while j >= 0:
                                if i - 200 < mousey < i and j - 200 < mousex < j:
                                    tempindex = a
                                    if placed[tempindex] - 1 in finished:
                                        tempindex = 500
                                j -= 200
                                if (i >= 750 or j >= 600) and j > 200:
                                    a += 1
                            i -= 200
                    a = 0
                    i = BOARDHEIGHT - 200
                    while i >= 0:
                        j = BOARDWIDTH - 200
                        while j >= 0:
                            if (i >= 600 or j >= 600) and j > 120 and a < 16:
                                if (a == tempindex and tempindex != 500):
                                    pygame.draw.rect(DISPLAYSURF, (247, 143, 167), (j, i, 81, 81))
                                    if placed[tempindex] in rotated270:
                                        rotated270.remove(placed[tempindex])
                                    elif placed[tempindex] in rotated180:
                                        rotated180.remove(placed[tempindex])
                                        rotated270.append(placed[tempindex])
                                    elif placed[tempindex] in rotated90:
                                        rotated90.remove(placed[tempindex])
                                        rotated180.append(placed[tempindex])
                                    else:
                                        rotated90.append(placed[tempindex])
                                a += 1
                            j -= 200
                        i -= 200
                    makeboardlake(500)
            elif event.type==MOUSEBUTTONUP:
                if indexclicked!=500:
                    tempindex=placed[indexclicked]-1

                    i=0
                    a=0
                    while i<600:
                        j=0
                        while j<600:

                            if tempindex==a and j<mousex<j+150 and i<mousey<i+150 and tempindex+1 not in rotated90 and tempindex+1 not in rotated180 and tempindex+1 not in rotated270:
                                pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
                                DISPLAYSURF.blit(lakepieces[placed[indexclicked]-1], (j-25,i-25))
                                finished.append(tempindex)
                                finishedindex.append(indexclicked)
                            j+=150
                            a+=1
                        i+=150

                indexclicked=500
                makeboardlake(indexclicked)
                if len(finished)==16:
                    fontObj = pygame.font.Font('freesansbold.ttf', 50)
                    textSurfaceObj = fontObj.render('You Win', True, (255,255,255))
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (1000,400)
                    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                    lake=pygame.image.load('lake.jpg')
                    DISPLAYSURF.blit(lake, (0,0))

    if version==3:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                if indexclicked!=500:
                    if mousex<560 and mousey<560:
                        makeriverpuzzle()
                        if placed[indexclicked] in rotated270:
                            blitrotatedriver(placed[indexclicked], 270, mousex-40, mousey-40)
                        elif placed[indexclicked] in rotated180:
                            blitrotatedriver(placed[indexclicked], 180, mousex-40, mousey-40)
                        elif placed[indexclicked] in rotated90:
                            blitrotatedriver(placed[indexclicked], 90, mousex-40, mousey-40)
                        else:
                            DISPLAYSURF.blit(riverpieces[placed[indexclicked] - 1], (mousex - 40, mousey - 40))
            elif event.type==KEYDOWN and event.key==K_h:
                if hint>0 and mousex<600 and mousey<600:
                    hint -= 1
                    hintriver(mousex, mousey)
            elif event.type==KEYDOWN and event.key==K_SPACE:
                if (mousex>600 or mousey>600) and mousex>120:
                    if len(finished) != 100:
                        tempindex = 0
                        a = 0
                        i = BOARDHEIGHT
                        while i >= 0:
                            j = BOARDWIDTH
                            while j >= 0:
                                if i - 80 < mousey < i and j - 80 < mousex < j:
                                    tempindex = a
                                    if placed[tempindex] - 1 in finished:
                                        tempindex = 500
                                j -= 80
                                if (i >= 680 or j >= 600) and j > 120:
                                    a += 1
                            i -= 80
                    a = 0
                    i = BOARDHEIGHT - 80
                    while i >= 0:
                        j = BOARDWIDTH - 80
                        while j >= 0:
                            if (i >= 600 or j >= 600) and j > 120 and a < 100:
                                if (a == tempindex and tempindex != 500):
                                    pygame.draw.rect(DISPLAYSURF, (247, 143, 167), (j, i, 81, 81))
                                    if placed[tempindex] in rotated270:
                                        rotated270.remove(placed[tempindex])
                                    elif placed[tempindex] in rotated180:
                                        rotated180.remove(placed[tempindex])
                                        rotated270.append(placed[tempindex])
                                    elif placed[tempindex] in rotated90:
                                        rotated90.remove(placed[tempindex])
                                        rotated180.append(placed[tempindex])
                                    else:
                                        rotated90.append(placed[tempindex])
                                a += 1
                            j -= 80
                        i -= 80
                    makeboardriver(500)
            elif event.type==MOUSEBUTTONDOWN:
                if (mousex<600 and mousey<600) or mousex<200:
                    indexclicked=500
                    if 75<mousex<175 and 735<mousey<785:
                        version=0
                    elif 12 < mousex < 52 and 740 < mousey < 780:
                        showinfo = True
                        shoinfo()
                        pygame.display.update()
                        while showinfo:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == MOUSEMOTION:
                                    mousex, mousey=event.pos
                                elif event.type==MOUSEBUTTONDOWN and mousey<20 and mousex<40:
                                    showinfo=False
                                    DISPLAYSURF = pygame.display.set_mode((1400, 800))
                    elif 75<mousex<175 and 625<mousey<725:
                        gopicture=True
                        zoom=0
                        DISPLAYSURF = pygame.display.set_mode((600,600))
                        DISPLAYSURF.blit(river, (0, 0))
                        blitx=0
                        blity=0
                        squarey=500
                        squarex=0
                        squaresize=0
                        picture=river
                        while gopicture:
                            for event in pygame.event.get():
                                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == MOUSEMOTION:
                                    mousex, mousey = event.pos

                                elif event.type == MOUSEBUTTONDOWN:
                                    if 580<mousex and 580<mousey:
                                        squarex=0
                                        squarey=500
                                        blity=0
                                        blitx=0
                                        if zoom==0:
                                            zoom+=1
                                            squaresize=75
                                            picture=pygame.transform.scale(river, (800,800))
                                            DISPLAYSURF.blit(picture, (blitx,blity))
                                        elif zoom==1:
                                            zoom+=1
                                            squaresize=60
                                            picture = pygame.transform.scale(river, (1000, 1000))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                        elif zoom==2:
                                            zoom+=1
                                            squaresize=50
                                            picture = pygame.transform.scale(river, (1200, 1200))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                    elif 580<mousex and 550<mousey<580:
                                        blity=0
                                        blitx=0
                                        squarey=500
                                        squarex=0
                                        if zoom==1:
                                            zoom-=1
                                            squaresize=0
                                            picture=pygame.transform.scale(river, (600,600))
                                            DISPLAYSURF.blit(picture, (blitx,blity))
                                        elif zoom==2:
                                            zoom-=1
                                            squaresize=75
                                            picture = pygame.transform.scale(river, (800, 800))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                        elif zoom==3:
                                            zoom-=1
                                            squaresize=60
                                            picture = pygame.transform.scale(river, (1000, 1000))
                                            DISPLAYSURF.blit(picture, (blitx, blity))
                                    elif mousex<40 and mousey<20:
                                        gopicture=False
                                        DISPLAYSURF = pygame.display.set_mode((1400, 800))

                                elif event.type==KEYDOWN and event.key==K_RIGHT:
                                    if zoom==3:
                                        if blitx>-590:
                                            blitx-=10
                                            squarex+=.833333
                                    elif zoom==2:
                                        if blitx>-390:
                                            blitx-=10
                                            squarex+=1
                                    elif zoom==1:
                                        if blitx>-190:
                                            blitx-=10
                                            squarex+=1.25
                                    DISPLAYSURF.blit(picture, (blitx, blity))
                                elif event.type==KEYDOWN and event.key==K_LEFT:
                                    if blitx<0:
                                        blitx+=10
                                        if zoom==3:
                                            squarex-=.833333
                                        elif zoom==2:
                                            squarex-=1
                                        elif zoom==1:
                                            squarex-=1.25
                                    DISPLAYSURF.blit(picture, (blitx, blity))
                                elif event.type==KEYDOWN and event.key==K_DOWN:
                                    if zoom == 3:
                                        if blity > -590:
                                            blity -= 10
                                            squarey+=.833333
                                    elif zoom == 2:
                                        if blity > -390:
                                            blity -= 10
                                            squarey+=1
                                    elif zoom == 1:
                                        if blity > -190:
                                            blity -= 10
                                            squarey+=1.25

                                    DISPLAYSURF.blit(picture, (blitx, blity))
                                elif event.type==KEYDOWN and event.key==K_UP:
                                    if blity<0:
                                        blity+=10
                                        if zoom==3:
                                            squarey-=.833333
                                        elif zoom==2:
                                            squarey-=1
                                        elif zoom==3:
                                            squarey-=1.25
                                    DISPLAYSURF.blit(picture, (blitx, blity))
                            fontObj = pygame.font.Font('freesansbold.ttf', 40)
                            textSurfaceObj = fontObj.render('+', True, (255, 255, 255))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (590, 590)
                            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                            fontObj = pygame.font.Font('freesansbold.ttf', 40)
                            textSurfaceObj = fontObj.render('-', True, (255, 255, 255))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (590, 560)
                            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                            fontObj = pygame.font.Font('freesansbold.ttf', 15)
                            textSurfaceObj = fontObj.render('BACK', True, (255, 255, 255))
                            textRectObj = textSurfaceObj.get_rect()
                            textRectObj.center = (22, 10)
                            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                            DISPLAYSURF.blit(rivercopy, (0,500))
                            pygame.draw.rect(DISPLAYSURF, (255,255,255), (squarex, squarey, squaresize, squaresize), 1)
                            pygame.display.update()

                elif len(finished)!=100:
                    indexclicked = 0
                    a = 0
                    i = BOARDHEIGHT
                    while i >= 0:
                        j = BOARDWIDTH
                        while j >= 0:
                            if i - 80 < mousey < i and j - 80 < mousex < j:
                                indexclicked = a
                                if placed[indexclicked]-1 in finished:
                                    indexclicked=500
                            j -= 80
                            if (i >= 680 or j >= 600) and j > 120:
                                a += 1
                        i -= 80
                makeboardriver(indexclicked)
            elif event.type==MOUSEBUTTONUP:
                if indexclicked!=500:
                    tempindex=placed[indexclicked]-1

                    i=0
                    a=0
                    while i<600:
                        j=0
                        while j<600:

                            if tempindex==a and j<mousex<j+60 and i<mousey<i+60 and tempindex+1 not in rotated270 and tempindex+1 not in rotated90 and tempindex+1 not in rotated180:
                                pygame.draw.rect(DISPLAYSURF, (200,200,200), (0,0,600,600))
                                DISPLAYSURF.blit(riverpieces[placed[indexclicked]-1], (j-11,i-11))
                                finished.append(tempindex)
                                finishedindex.append(indexclicked)
                            j+=60
                            a+=1
                        i+=60

                indexclicked=500
                makeboardriver(indexclicked)
                if len(finished)==100:
                    fontObj = pygame.font.Font('freesansbold.ttf', 50)
                    textSurfaceObj = fontObj.render('You Win', True, (255,255,255))
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (1000,400)
                    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                    DISPLAYSURF.blit(river, (0,0))
                pygame.display.update()
    pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
