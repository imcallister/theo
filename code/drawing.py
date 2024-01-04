import turtle

Flower_Colors = [
    {'pen_color': 'red', 'fill_color': 'blue', 'start_x': 250, 'start_y': 200},
    {'pen_color': 'pink', 'fill_color': 'green', 'start_x': -200, 'start_y': 200},
    {'pen_color': 'black', 'fill_color': 'pink', 'start_x': 200, 'start_y': -100},
    {'pen_color': 'black', 'fill_color': 'orange', 'start_x': -200, 'start_y': -200},
    {'pen_color': 'pink', 'fill_color': 'black', 'start_x': 100, 'start_y': -75},
    {'pen_color': 'yellow', 'fill_color': 'grey', 'start_x': -100, 'start_y': 100},
    {'pen_color': 'pink', 'fill_color': 'blue', 'start_x': -300, 'start_y': -75},
    {'pen_color': 'purple', 'fill_color': 'purple', 'start_x': 150, 'start_y': 100},
    {'pen_color': 'pink', 'fill_color': 'red', 'start_x': 500, 'start_y': -75},
    {'pen_color': 'purple', 'fill_color': 'yellow', 'start_x': -150, 'start_y': -200},
    {'pen_color': 'purple', 'fill_color': 'orange', 'start_x': -100, 'start_y': -150},
]

def draw_flower_head(bob, line_color, fill_color, start_x, start_y):

    bob.goto(start_x , start_y)
    bob.setheading(0)
    bob.pendown()

    bob.pencolor(line_color)
    bob.fillcolor(fill_color)

    bob.begin_fill()

    for i in range (8):
        bob.forward(200)
        bob.left(135)

    bob.penup()
    bob.setheading(0)
    bob.end_fill()

    return


greg = turtle.Turtle()

greg.penup()
greg.speed("fastest")

for flower_info in Flower_Colors:
    draw_flower_head(greg, flower_info['pen_color'], flower_info['fill_color'], flower_info['start_x'], flower_info['start_y'])

input("Press enter to exit")