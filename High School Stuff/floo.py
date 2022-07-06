from graphics import *

def main():
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

main()

