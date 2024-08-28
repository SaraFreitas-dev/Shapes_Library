from turtle import Turtle, Screen
from random import randint

class ShapeDrawer:
    def __init__(self):
        self.screen = Screen()
        self.screen.colormode(255)
        self.turtle = Turtle()
        self.turtle.speed("fastest")
    
    def random_color(self):
        return randint(0, 255), randint(0, 255), randint(0, 255)
    
    def set_thickness(self, thickness):
        self.turtle.pensize(thickness)
    
    def reset_position(self):
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()

    def exit_on_click(self):
        self.screen.exitonclick()


class Spinograph(ShapeDrawer):
    def draw(self, size_of_gap, radius=150):
        for _ in range(int(360 / size_of_gap)):
            self.turtle.color(self.random_color())
            self.turtle.circle(radius)
            self.turtle.setheading(self.turtle.heading() + size_of_gap)


class SquarePattern(ShapeDrawer):
    def draw(self, side_length=100, number_of_squares=36):
        for _ in range(number_of_squares):
            self.turtle.color(self.random_color())
            for _ in range(4):
                self.turtle.forward(side_length)
                self.turtle.right(90)
            self.turtle.right(360 / number_of_squares)


class CirclePattern(ShapeDrawer):
    def draw(self, radius=100, number_of_circles=36):
        for _ in range(number_of_circles):
            self.turtle.color(self.random_color())
            self.turtle.circle(radius)
            self.turtle.right(360 / number_of_circles)


class HexagonPattern(ShapeDrawer):
    def draw(self, side_length=100, number_of_hexagons=36):
        for _ in range(number_of_hexagons):
            self.turtle.color(self.random_color())
            for _ in range(6):
                self.turtle.forward(side_length)
                self.turtle.right(60)
            self.turtle.right(360 / number_of_hexagons)


class StarPattern(ShapeDrawer):
    def draw(self, size=100, points=5):
        angle = 180 - 180/points  # Calculate angle for the star
        self.turtle.color(self.random_color())
        for _ in range(points):
            self.turtle.forward(size)
            self.turtle.right(angle)


class TrianglePattern(ShapeDrawer):
    def draw(self, side_length=100, number_of_triangles=36):
        for _ in range(number_of_triangles):
            self.turtle.color(self.random_color())
            for _ in range(3):
                self.turtle.forward(side_length)
                self.turtle.right(120)
            self.turtle.right(360 / number_of_triangles)


class PolygonPattern(ShapeDrawer):
    def draw(self, sides=6, side_length=100, number_of_polygons=36):
        angle = 360 / sides  # Calculate interior angle
        for _ in range(number_of_polygons):
            self.turtle.color(self.random_color())
            for _ in range(sides):
                self.turtle.forward(side_length)
                self.turtle.right(angle)
            self.turtle.right(360 / number_of_polygons)


class FlowerPattern(ShapeDrawer):
    def draw(self, radius=100, petals=12):
        for _ in range(petals):
            self.turtle.color(self.random_color())
            self.turtle.circle(radius, 60)
            self.turtle.left(120)
            self.turtle.circle(radius, 60)
            self.turtle.left(360 / petals)


class SunburstPattern(ShapeDrawer):
    def draw(self, line_length=150, number_of_lines=36):
        for _ in range(number_of_lines):
            self.turtle.color(self.random_color())
            self.turtle.forward(line_length)
            self.turtle.backward(line_length)
            self.turtle.right(360 / number_of_lines)


class ChangingRadiusSpirograph(ShapeDrawer):
    def draw(self, size_of_gap=5, start_radius=50, end_radius=150, step=2):
        radius = start_radius
        while radius <= end_radius:
            self.turtle.color(self.random_color())
            self.turtle.circle(radius)
            self.turtle.setheading(self.turtle.heading() + size_of_gap)
            radius += step


class RandomWalk(ShapeDrawer):
    def draw(self, steps=100, step_length=30):
        for _ in range(steps):
            self.turtle.color(self.random_color())
            self.turtle.setheading(randint(0, 3) * 90)  # Random direction
            self.turtle.forward(step_length)
            # Ensure the turtle stays within the screen boundaries
            if abs(self.turtle.xcor()) > 300 or abs(self.turtle.ycor()) > 300:
                self.turtle.penup()
                self.turtle.goto(0, 0)  # Reset to center
                self.turtle.pendown()


class ConcentricCircles(ShapeDrawer):
    def draw(self, start_radius=50, end_radius=200, step=10):
        for radius in range(start_radius, end_radius, step):
            self.turtle.color(self.random_color())
            self.turtle.circle(radius)
            self.turtle.penup()
            self.turtle.goto(0, -radius)
            self.turtle.pendown()

