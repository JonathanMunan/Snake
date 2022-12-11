from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=250)
        self.color("white")
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()
