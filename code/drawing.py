import turtle


def draw_flower_head(greg):

    greg.pendown()

    greg.pencolor("red")
    greg.fillcolor("yellow")

    greg.begin_fill()

    for i in range (8):
        greg.forward(200)
        greg.left(135)

    greg.penup()

    greg.end_fill()

    return

greg = turtle.Turtle()

greg.penup()
greg.speed("fastest")

greg.goto(200,200)
draw_flower_head(greg)

greg.goto(-200,200)
draw_flower_head(greg)

greg.goto(-200,-200)
draw_flower_head(greg)

greg.goto(200,-200)
draw_flower_head(greg)

input("Press enter to exit")