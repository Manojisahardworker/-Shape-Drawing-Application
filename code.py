from graphics import *

def main():
    win = GraphWin("Drawing a shape of user choice", 1000, 800)

    # Prompt user for shape
    option = Text(Point(200, 50), "Enter the shape to draw (circle, rectangle, square, triangle):")
    option.draw(win)
    entry = Entry(Point(400, 100), 15)
    entry.draw(win)

    cont = Text(Point(200, 150), "After typing, click anywhere to continue")
    cont.draw(win)
    win.getMouse()

    choice = entry.getText().lower()

    if choice == "circle":
        instruction = Text(Point(300, 200), "Click center and edge of the circle")
        instruction.draw(win)
        center = win.getMouse()
        edge = win.getMouse()
        radius = ((center.getX() - edge.getX()) ** 2 + (center.getY() - edge.getY()) ** 2) ** 0.5
        circle = Circle(center, radius)
        circle.setOutline("blue")
        circle.draw(win)
        info = Text(Point(400, 500), f"Circle center: ({center.getX():.1f}, {center.getY():.1f}), Radius: {radius:.1f}")
        info.draw(win)

    elif choice == "rectangle":
        instruction = Text(Point(200, 200), "Click two opposite corners of the rectangle")
        instruction.draw(win)
        p1 = win.getMouse()
        p2 = win.getMouse()
        rect = Rectangle(p1, p2)
        rect.setOutline("green")
        rect.draw(win)
        width = abs(p1.getX() - p2.getX())
        height = abs(p1.getY() - p2.getY())
        info = Text(Point(400, 500), f"Rectangle width: {width:.1f}, height: {height:.1f}")
        info.draw(win)

    elif choice == "square":
        instruction = Text(Point(200, 200), "Click top-left point, then bottom-right point")
        instruction.draw(win)
        p1 = win.getMouse()
        p2 = win.getMouse()
        side = min(abs(p1.getX() - p2.getX()), abs(p1.getY() - p2.getY()))
        p2_fixed = Point(p1.getX() + side, p1.getY() + side)
        square = Rectangle(p1, p2_fixed)
        square.setOutline("red")
        square.draw(win)
        info = Text(Point(400, 500), f"Square side length: {side:.1f}")
        info.draw(win)

    elif choice == "triangle":
        instruction = Text(Point(200, 200), "Click three vertices of the triangle")
        instruction.draw(win)
        p1 = win.getMouse()
        p2 = win.getMouse()
        p3 = win.getMouse()
        triangle = Polygon(p1, p2, p3)
        triangle.setOutline("purple")
        triangle.draw(win)
        info = Text(Point(400, 500),
                    f"Triangle vertices: ({p1.getX():.1f},{p1.getY():.1f}), "
                    f"({p2.getX():.1f},{p2.getY():.1f}), "
                    f"({p3.getX():.1f},{p3.getY():.1f})")
        info.draw(win)

    else:
        error = Text(Point(200, 300), "Invalid shape entered!")
        error.setFill("red")
        error.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
