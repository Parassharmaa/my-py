import turtle

def draw_spiral(radius):
    original_xcor = turtle.xcor()
    original_ycor = turtle.ycor()
    speed = 1
    while True:
        turtle.color("Green")
        turtle.forward(speed)
        turtle.color("red")
        turtle.left(20)
        turtle.width(speed)
        speed += 0.1
        if turtle.distance(original_xcor, original_ycor) > radius:
            break
