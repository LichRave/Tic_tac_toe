game_field = [" "] * 9
player_icon = "o"
print(f"|{game_field[6]}|{game_field[7]}|{game_field[8]}|")
print("_________")
print(f"|{game_field[3]}|{game_field[4]}|{game_field[5]}|")
print("_________")
print(f"|{game_field[0]}|{game_field[1]}|{game_field[2]}|")
while True:
    player_position = int(input("Podaj numer pola[1-9]: ")) - 1
    game_field[player_position] = player_icon
    print(f"|{game_field[6]}|{game_field[7]}|{game_field[8]}|")
    print("_________")
    print(f"|{game_field[3]}|{game_field[4]}|{game_field[5]}|")
    print("_________")
    print(f"|{game_field[0]}|{game_field[1]}|{game_field[2]}|")
    break
