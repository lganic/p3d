def cos(val):
    import math
    return math.cos(math.radians(val))

def sin(val):
    import math
    return math.sin(math.radians(val))

def arccos(val):
    import math
    return math.degrees(math.acos(val))

def arctan(val):
    import math
    return math.degrees(math.atan(val))

class engine:
    def __init__(self,width,height):
        self.cameraX=0
        self.cameraY=0
        self.cameraZ=0
        self.cameraFov=45
        self.cameraRotUp=0
        self.cameraRotLR=0
        self.width=width
        self.height=height
        global pygame,screen
        import pygame
        pygame.init()
        screen=pygame.display.set_mode((width,height))
    def update(self):
        pygame.display.flip()
        pygame.event.get()
    def fill(self,color):
        screen.fill(color)
    def putVoxel(self,x,y,z,color=(255,255,255)):
        try:
            d=((self.cameraX-x)**2+(self.cameraY-y)**2)**.5
            px=d*cos(self.cameraRotLR)
            py=d*sin(self.cameraRotLR)
            h=((px-x)**2+(py-y)**2)**.5
            xrot=arccos(1-((h*h)/(2*d*d)))#-self.cameraRotLR
            if y>self.cameraY:
                xrot=-xrot
                if y>py:
                    xrot+=self.cameraRotLR
                else:
                    xrot=self.cameraRotLR-xrot
            else:
                if y<py:
                    xrot+=self.cameraRotLR
                else:
                    xrot=self.cameraRotLR-xrot
            o=z-self.cameraZ
            yrot=arctan(o/d)+self.cameraRotUp
            xpos=int(((xrot/self.cameraFov)+.5)*self.width)
            ypos=int(((yrot/self.cameraFov)+.5)*self.height)
            if xpos>0 and xpos<self.width and ypos>0 and ypos<self.height:
                screen.set_at((xpos,ypos),color)
            return (xpos,ypos)
        except:
            return (int(self.width/2),int(self.height/2))
    def line(self,cord1,cord2,color=(255,255,255)):
        px1=self.putVoxel(cord1[0],cord1[1],cord1[2])
        px2=self.putVoxel(cord2[0],cord2[1],cord2[2])
        pygame.draw.line(screen,color,px1,px2)#wow
    def translate(self,x,y,z):
        self.cameraX+=x
        self.cameraY+=y
        self.cameraZ+=z
    def panUp(self,amount):
        self.cameraRotUp+=amount
    def panLR(self,amount):
        self.cameraRotLR+=amount
    def checkKey(self,key):
        return pygame.key.get_pressed()[key]==1
