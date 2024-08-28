"""
Turtle Shapes Library
=========================

Welcome to the Shape Library! This Python package allows you to create a variety of artistic patterns using the Turtle graphics module. Whether you're interested in spirographs, polygons, or random walk patterns, this library has something for you. Feel free to test it out !

Installation
-------------
To use this library, you need to have Python and the `turtle` module installed. The `turtle` module is included with the standard Python library, so no additional installation is required.

1. **Install Python:** Ensure you have Python installed. You can download it from https://www.python.org/downloads/.
2. **Download the Shape Library:** Save the code provided in a file named `shape_library.py`.

How to Use
-----------
1. **Import the Library:**

   ```python
   from shape_library import *

Notes
-----------
Each class inherits from ShapeDrawer, which provides methods for setting the pen size, resetting the turtle's position, and closing the drawing window on click.
The random_color method provides a random color for each line or shape, adding variability to your patterns.
Feel free to experiment with different parameters to create unique and beautiful patterns!

Create and Draw Patterns:
-----------
2. **Spirograph:**
spiro = Spinograph()
spiro.draw(size_of_gap=5)
spiro.exit_on_click()  # Close the window on click

3. **SquarePattern:**
square = SquarePattern()
square.draw(side_length=200, number_of_squares=36)
square.exit_on_click()
Circle Pattern:

4. **CirclePattern:**
circle = CirclePattern()
circle.draw(radius=100, number_of_circles=10)
circle.exit_on_click()

5. **HexagonPattern:**
hexagon = HexagonPattern()
hexagon.draw(side_length=100, number_of_hexagons=30)
hexagon.exit_on_click()


6. **StarPattern:**
star = StarPattern()
star.draw(size=250, points=7)  # Size and points of each star
star.exit_on_click()

7. **TrianglePattern:**
triangle = TrianglePattern()
triangle.draw(side_length=150, number_of_triangles=36)
triangle.exit_on_click()

8. **PolygonPattern:**
polygon = PolygonPattern()
polygon.draw(sides=8, side_length=100, number_of_polygons=24)
polygon.exit_on_click()
Flower Pattern:

8. **FlowerPattern:**
flower = FlowerPattern()
flower.draw(radius=100, petals=24)  # Radius and number of petals
flower.exit_on_click()

9. **SunburstPattern:**
sunburst = SunburstPattern()
sunburst.draw(line_length=150, number_of_lines=36)
sunburst.exit_on_click()
Spirograph with Changing Radius:

10. **ChangingRadiusSpirograph:**
changing_radius_spiro = ChangingRadiusSpirograph()
changing_radius_spiro.draw(size_of_gap=5, start_radius=50, end_radius=180, step=5)
changing_radius_spiro.exit_on_click()

11. **RandomWalk:**
random_walk = RandomWalk()
random_walk.draw(steps=100, step_length=30)
random_walk.exit_on_click()

12. **ConcentricCircles:**
concentric_circles = ConcentricCircles()
concentric_circles.draw(start_radius=10, end_radius=200, step=10)
concentric_circles.exit_on_click()
Notes
Inheritance: Each shape class inherits from ShapeDrawer, which provides methods for setting the pen size, resetting the turtle’s position, and closing the drawing window on click.
Random Colors: The random_color method generates a random color for each line or shape, adding variability to your patterns.
Experiment: Feel free to experiment with different parameters to create unique and beautiful patterns!