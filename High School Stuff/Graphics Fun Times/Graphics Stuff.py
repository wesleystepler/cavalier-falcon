from graphics import *

def circle():
    win = GraphWin("My Circle", 1000, 1000)
    c = Circle(Point(500,300), 250)
    c.setWidth(50)
    c.setFill("silver")
    c.draw(win)

    x = Line(Point(100,100), Point(1000,1000))
    win.plot(35, 128, "blue")
    win.setBackground("purple")
    win.getMouse() #Pause for click in window
    win.close()

circle()

def rectangle():
    win = GraphWin("An Rectangle", 1000, 1000)
    r = Rectangle(Point(50,50), Point(200,200))
    r.setWidth(5)
    r.draw(win)
    c.setFill("black")

    win.setBackground("white")
    win.getMouse()
    win.close()

#rectangle()

