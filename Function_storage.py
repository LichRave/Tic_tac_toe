game_field = [" "] * 9
player_icon = "o"

# Funkcja do rysowania


def draw_board(game_data: List[str]) -> None:
    print(f"|{game_data[6]}|{game_data[7]}|{game_data[8]}|")
    print("________")
    print(f"|{game_data[3]}|{game_data[4]}|{game_data[5]}|")
    print("________")
    print(f"|{game_data[0]}|{game_data[1]}|{game_field[2]}|")


def player_input(game_field: List[str]) -> int:
    player_position = input("Podaj numer pola[1-9]: ")
    while not player_position.isdigit() or not (0 < int(player_position) < 10):
        player_position = input("Podaj numer pola[1-9]: ")
    player_position = int(player_position) - 1

    while game_field[player_position] != " ":
        print(f"Pozycja {player_position + 1} jest już zajęta!")
        player_position = int(input("Podaj numer pola[1-9]: ")) - 1
    game_field[player_position] = player_icon
    return player_position


# game


def end_condition_check(game_field: [str]) -> bool:
    # poziomo
    if game_field[0] == game_field[1] == game_field[2] and game_field[0] != " ":
        print(f"Wygrał gracz {game_field[0]}")
        return True
    if game_field[3] == game_field[4] == game_field[5] and game_field[3] != " ":
        print(f"Wygrał gracz {game_field[3]}")
        return True
    if game_field[6] == game_field[7] == game_field[8] and game_field[6] != " ":
        print(f"Wygrał gracz {game_field[6]}")
        return True

    # Pion
    if game_field[0] == game_field[3] == game_field[6] and game_field[0] != " ":
        print(f"Wygrał gracz {game_field[0]}")
        return True
    if game_field[1] == game_field[4] == game_field[7] and game_field[1] != " ":
        print(f"Wygrał gracz {game_field[1]}")
        return True
    if game_field[2] == game_field[5] == game_field[8] and game_field[2] != " ":
        print(f"Wygrał gracz {game_field[2]}")
        return True
    # skosy
    if game_field[0] == game_field[4] == game_field[8] and game_field[0] != " ":
        print(f"Wygrał gracz {game_field[0]}")
        return True
    if game_field[2] == game_field[4] == game_field[6] and game_field[2] != " ":
        print(f"Wygrał gracz {game_field[2]}")
        return True

    if all([item != " " for item in game_field]):
        print("Remis!")
        return True

    return False