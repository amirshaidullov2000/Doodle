import pygame
import time
###1.11.19

def getXY(object):
    return object.getY
class Gm:
    def __init__(self, x, y, width, height, speed, image, exist, direction):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._speed = speed
        self._image = image
        self._exist = exist
        self._time0 = time.time()
        self._jumpCount = 28
        self._direction = direction
        #self._time = time.time() - self._time0
        self._isFalling = True
        self._v0 = 15 #####################################

    def new(self):
        self._y += 1
        if self._y > 17:
            self._exist = False

    def setTileY(self, y):
        self._tileY = y

    def setTileX(self, x):
        self._tileX = x

    def dY(self):
        return self._tileY - self._y
    def getDirection(self):
        return self._direction
    def setDirection(self, direction):
        self._direction = direction
    def setPicture(self, image):
        self._image = image

    def GetExist(self):
            return self._exist

    def getFalling(self):
        return self._isFalling

    def setFalling(self, temp):
        self._isFalling = temp

    def notExist(self):
        self._exist = False

    def turnLeft(self):
        self._x -= self._speed
        if self._x < -30:
            self._x = 480

    def turnRight(self):
        self._x += self._speed
        if self._x > 460:
            self._x = -25

    def getX(self):
        return self._x

    def getY(self):
        return self._y
    def setJumpCount(self, jumpCount):
        self._jumpCount = jumpCount


    def motion(self):

        if self._jumpCount > -81:
            if self._jumpCount < 0:
                #(self._tileY - self._y < 69)
                if (self._tileY - 70 < self._y) and (self._y < self._tileY - 61)and\
                        (self._tileX - self._width + 12 <  self._x) and\
                        (self._x < self._tileX + 66):
                    self._y = 288 # исправить потом taleY + self._height
                    self._jumpCount = 28
                    pygame.display.update()

                    #self._y -= 1
                    return 0
                self._y += (self._jumpCount ** 2) / 40
            else:
                self._y -= (self._jumpCount ** 2) / 40
            self._jumpCount -= 1
        else:
            #self._isFalling = False
            #self._jumpCount = 20
            font = pygame.font.Font(None, 50)
            text = font.render("Game over", True, (255, 0, 0))
            win.blit(text, [170, 150])
            pygame.display.update()
            time.sleep(1)
            pygame.quit()




class Tile:
    def __init__(self, x, y, image):
        self._x = x
        self._y = y
        self._image = image
        #self._width = 0 !!!!!!!!!!!!!!!!!
        #self._height = 0 !!!!!!!!!!!!!!!!

    def getX(self):
        return self._x

    def getY(self):
        return self._y


pygame.init()
win = pygame.display.set_mode((503, 505)) #((624, 800))
pygame.display.set_caption("D00dle")
bg = pygame.image.load('sheet.jpg')
clock = pygame.time.Clock()

ob1 = Gm(250, 300, 75, 69, 8, pygame.image.load('doodle-r.png'), True, True) #
tale1 = Tile(250, 350, pygame.image.load('green_tale1.png'))

def drawWindow():
    win.blit(bg, (0, 0))
    win.blit(tale1._image, (tale1.getX(), tale1.getY()) )
    win.blit(ob1._image, (ob1.getX(), ob1.getY()))

    pygame.display.update()

   # XY = getXY(tale1)

while ob1.GetExist():

    clock.tick(500)

    pygame.time.delay(14)  #приостановить на N секунд

    Y = tale1.getY()
    X = tale1.getX()
    ob1.setTileY(Y)
    ob1.setTileX(X)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ob1.notExist()

    keys = pygame.key.get_pressed()
    if ob1.getFalling():
        ob1.motion()
    if keys[pygame.K_LEFT] :

        if ob1.getDirection():
            ob1.setPicture(pygame.image.load('doodle2.png'))
            ob1.setDirection(False)
        ob1.turnLeft()
    if keys[pygame.K_RIGHT]:
        if not ob1.getDirection():
            ob1.setPicture(pygame.image.load('doodle-r.png'))
            ob1.setDirection(True)
        ob1.turnRight()
    if keys[pygame.K_SPACE]:
       ob1.setFalling(True)

    drawWindow()

pygame.quit()


