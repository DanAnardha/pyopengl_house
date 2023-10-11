import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption("DrawHouse Danuar | 2113020083") 
        pg.display.set_mode((1024, 720), pg.OPENGL | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.2, 0.2, 1)
        self.initGL()
        self.mainLoop()

    def initGL(self):
        # Set perspective mode to projection
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-400, 400, -300, 300, 0.1, 50)

        # Configure modelview to default
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Drag camera to behind so object can visible
        glTranslatef(0, 0, -5)

    def mainLoop(self):
        running = True
        while (running):
            for event in pg.event.get():
                if(event.type == pg.quit):
                    running = False
            glClear(GL_COLOR_BUFFER_BIT)
            self.drawHouse()
            pg.display.flip()
            self.clock.tick(60)
        self.quit()
    
    def quit(self):
        pg.quit()

    # Function to draw hollow rectangle
    def drawRectangle(self, x1, y1, x2, y2, x3, y3, x4, y4):
        glBegin(GL_LINE_LOOP)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glVertex2f(x3, y3)
        glVertex2f(x4, y4)
        glEnd()

    # Function to draw lines
    def drawLine(self, x1, y1, x2, y2):
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

    # Function to draw house
    def drawHouse(self):
        glColor3f(1.0 ,1.0 ,1.0)
        self.drawRectangle(-30, 230, 178, 95, 178, 35, -30, 125)
        self.drawRectangle(-19, 208, 166, 92, 166, 49, -19, 133)
        self.drawRectangle(-170, 114, -30, 230, -30, 125, -170, 48)
        self.drawRectangle(-30, 125, 42, 94, 42, 5, -30, 20)
        self.drawRectangle(-132, 69, -30, 125, -30, 20, -132, -10)
        self.drawRectangle(42, 33, 105, 50, 105, 20, 42, 5)
        self.drawRectangle(105, 50, 208, 12, 208, -11, 105, 20)
        self.drawRectangle(-30, 20, 321, -56, 321, -86, -30, -86)
        self.drawLine(151, -19, 208, -11)
        self.drawLine(147, 47, 147, 35)
        self.drawRectangle(-200, -30, -30, 20, -30, -86, -200, -86)
        self.drawLine(-170, 48, -132, 39)
        self.drawRectangle(-199, 31, -132, 17, -132, -10, -199, 1)
        self.drawRectangle(-276, -10, -199, 31, -199, 1, -276, -31)
        self.drawLine(-276, -31, -224, -36)
        self.drawLine(-224, -36, -200, -30)
        self.drawLine(-200, -86, -318, -86)
        self.drawRectangle(-318, -86, -269, -86, -269, -184, -318, -154)
        self.drawLine(-269, -184, -223, -177)
        self.drawLine(-223, -177, -223, -120)
        self.drawLine(-223, -120, -185, -116)
        self.drawLine(-185, -116, -185, -173)
        self.drawLine(-185, -173, -223, -161)
        self.drawLine(-186, -173, -140, -168)
        self.drawLine(-140, -168, -140, -86)
        self.drawLine(-140, -168, -30, -200)
        self.drawLine(-30, -200, -30, -86)
        self.drawLine(-30, -200, 8, -192)
        self.drawLine(8, -192, 8, -109)
        self.drawLine(8, -109, 45, -109)
        self.drawLine(45, -109, 45, -181)
        self.drawLine(45, -181, 219, -143)
        self.drawLine(45, -181, 8, -172)
        self.drawLine(219, -143, 219, -98)
        self.drawLine(219, -98, 250, -98)
        self.drawLine(250, -98, 250, -135)
        self.drawLine(250, -135, 299, -124)
        self.drawLine(250, -135, 219, -131)
        self.drawLine(299, -124, 299, -86)

        # Windows
        self.drawRectangle(-15, 1, 29, -8, 29, -79, -15, -79)
        self.drawLine(29, -8, -15, -16)
        self.drawRectangle(42, -10, 86, -17, 86, -79, 42, -79)
        self.drawLine(86, -17, 42, -26)
        self.drawRectangle(98, -21, 143, -30, 143, -79, 98, -79)
        self.drawLine(143, -30, 98, -35)
        self.drawRectangle(155, -32, 200, -40, 200, -79, 155, -79)
        self.drawLine(200, -40, 155, -44)
        self.drawRectangle(212, -43, 257, -51, 257, -79, 212, -79)
        self.drawLine(257, -51, 212, -54)
        self.drawRectangle(269, -54, 313, -63, 313, -79, 269, -79)
        self.drawLine(313, -63, 269, -64)
    
if __name__ == "__main__":
    myApp = App()