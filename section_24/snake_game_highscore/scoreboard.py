from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as high_score_file:
            self.high_score = int(high_score_file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-20, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ", align="center", font=("Arial", 14, "bold"))

    def gain_a_point(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as hs_file:
                hs_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

