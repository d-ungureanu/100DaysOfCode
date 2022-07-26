from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("slowest")
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movement = 10
        self.y_movement = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce_y_axis(self):
        self.y_movement *= -1

    def bounce_x_axis(self):
        self.x_movement *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x_axis()
        self.move_speed = 0.1
