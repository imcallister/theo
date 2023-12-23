import turtle


def draw_flower_head(bob, line_color, fill_color, start_x, start_y):

    bob.pendown()

    bob.pencolor(line_color)
    bob.fillcolor(fill_color)

    bob.goto(start_x, start_y)


    bob.begin_fill()

    for i in range (8):
        bob.forward(200)
        bob.left(135)

    bob.penup()

    bob.end_fill()

    return

line_color = input("what color do you want the outline to be?")

fill_color = input("what color do you want the inside to be?")

start_x = float(input("What do you want the x to be?"))

start_y = float(input("What do you want the y to be?"))

greg = turtle.Turtle()

greg.penup()
greg.speed("fastest")

greg.goto(200,200)
draw_flower_head(greg, line_color, fill_color, start_x, start_y)

greg.goto(-200,200)
draw_flower_head(greg, line_color, fill_color, start_x, start_y)

greg.goto(-200,-200)
draw_flower_head(greg, line_color, fill_color, start_x, start_y)

greg.goto(200,-200)
draw_flower_head(greg, line_color, fill_color, start_x, start_y)

input("Press enter to exit")