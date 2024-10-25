import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.initialize_scoreboard()


screen.listen()
screen.onkey(player.go_up, "w")


game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over_sequence()

    if player.ycor() > 290:
        player.player_reset()
        scoreboard.increase_score()
        car_manager.increase_car_speed()


screen.exitonclick()


