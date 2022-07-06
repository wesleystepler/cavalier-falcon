from graphics import *

def main():
    win = GraphWin("My Circle", 1000, 1000)
    c = Circle(Point(450,300), 250)
    diameter = Line(Point(200,300), Point(700,300))
    c.draw(win)
    c.setWidth(2)
    win.getMouse() # pause for click in window
    win.close()
 

main()