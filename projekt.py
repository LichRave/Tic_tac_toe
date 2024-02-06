game_field = [" "] * 9
player_icon = "o"
print(f"|{game_field[6]}|{game_field[7]}|{game_field[8]}|")
print("________")
print(f"|{game_field[3]}|{game_field[4]}|{game_field[5]}|")
print("________")
print(f"|{game_field[0]}|{game_field[1]}|{game_field[2]}|")
while True:
    print(f"Ruch gracza {player_icon}")
    player_position = input("Podaj numer pola[1-9]: ")
    while not player_position.isdigit() or not (0 < int(player_position) < 10):
        player_position = input("Podaj numer pola[1-9]: ")
    player_position = int(player_position) - 1

    while game_field[player_position] != " ":
        print(f"Pozycja {player_position + 1} jest już zajęta!")
        player_position = int(input("Podaj numer pola[1-9]: ")) - 1
    game_field[player_position] = player_icon
    # if game_field[player_position] == " ":
    #     game_field[player_position] = player_icon
    # else:
    #     continue
    print(f"|{game_field[6]}|{game_field[7]}|{game_field[8]}|")
    print("________")
    print(f"|{game_field[3]}|{game_field[4]}|{game_field[5]}|")
    print("________")
    print(f"|{game_field[0]}|{game_field[1]}|{game_field[2]}|")

    print("Round ended.")
    # poziomo
    if game_field[0] == game_field[1] == game_field[2] and game_field[0] != " ":
        print(f"Wygrał gracz {game_field[0]}")
        break
    if game_field[3] == game_field[4] == game_field[5] and game_field[3] != " ":
        print(f"Wygrał gracz {game_field[3]}")
        break
    if game_field[6] == game_field[7] == game_field[8] and game_field[6] != " ":
        print(f"Wygrał gracz {game_field[6]}")
        break

    # Pion
    if game_field[0] == game_field[3] == game_field[6] and game_field[0] != " ":
        print(f"Wygrał gracz {game_field[0]}")
        break
    if game_field[1] == game_field[4] == game_field[7] and game_field[1] != " ":
        print(f"Wygrał gracz {game_field[1]}")
        break
    if game_field[2] == game_field[5] == game_field[8] and game_field[2] != " ":
        print(f"Wygrał gracz {game_field[2]}")
        break
    # skosy
    if game_field[0] == game_field[4] == game_field[8] and game_field[0] != " ":
        print(f"Wygrał gracz {game_field[0]}")
        break
    if game_field[2] == game_field[4] == game_field[6] and game_field[2] != " ":
        print(f"Wygrał gracz {game_field[2]}")
        break

    if all([item != " " for item in game_field]):
        print("Remis!")
        break
    player_icon = "x" if player_icon == "o" else "o"
