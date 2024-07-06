import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Racing Game")
screen.setup(width=600, height=600)

screen.tracer(0)
player = Player()
car = CarManager()


screen.listen()
screen.onkeypress(fun=player.forward_move, key="Up")
screen.onkeypress(fun=player.right_move, key="Right")
screen.onkeypress(fun=player.left_move, key="Left")
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()
    for new_car in car.cars:
        if new_car.distance(player) < 25:
            game_is_on = False
            player.game_over()

    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.increase_level()
        car.speed_increase()


screen.exitonclick()
