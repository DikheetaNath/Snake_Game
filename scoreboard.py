from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 278)

    def update_score(self, new_score):
        self.clear()
        self.pencolor("white")
        self.write(arg=f'Score: {new_score}', align='center', font=("Ariel", 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.pencolor('red')
        self.write("GAME OVER!!!!", align='center', font=("Calibri", 30, 'normal'))
