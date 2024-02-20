from Function_storage import *


def main():
    game_field = [" "] * 9
    player_icon = "o"
    draw_board(game_field)
    while not end_condition_check(game_field):
        print(f"Ruch gracza {player_icon}")
        player_position = player_input(game_field)
        game_field[player_position] = player_icon
        draw_board(game_field)
        print("Round ended")
        player_icon = "x" if player_icon == "o" else "o"


main()
