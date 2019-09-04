from graphics import *

win = GraphWin()
p = Point(134,89)
p.draw(win)
line1 = Line(Point(120,120),Point(120,65))
line1.draw(win)
circlecenter = Point(50,80)
circle = Circle(circlecenter,20)
label1 = Text(circlecenter,"Stop!")
circlecenter = Point(50,160)
circle = Circle(circlecenter,20)
label2 = Text(circlecenter,"Go!")

aRectangle = Rectangle(Point(23,60), Point(82,180))
aRectangle.draw(win)
circle1 = Circle(Point(50,80),20)
circle1.setFill('red')
circle1.draw(win)
label1.draw(win)

circle2 = Circle(Point(50,120),20)
circle2.setFill('yellow')
circle2.draw(win)

circle3 = Circle(Point(50,160),20)
circle3.setFill('green')
circle3.draw(win)
label2.draw(win)

while True:
    mouse = win.getMouse()
    if mouse.getX() in range (30,80) and mouse.getY() in range:
        print("Stop!")
    elif mouse.getY() in range (30,40):
        print("Go!")
    print(mouse.getX())
    print(mouse.getY())
input("Waiting")