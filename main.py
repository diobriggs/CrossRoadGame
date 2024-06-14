import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    if player.ycor() > 290:
        player.reset()
        car.next_level()
        scoreboard.update_score()

    for cars in car.all_cars:
        if player.distance(cars) < 30:
            player.reset()
            scoreboard.game_over()
            game_is_on = False










screen.exitonclick()