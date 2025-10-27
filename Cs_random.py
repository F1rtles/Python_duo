# <<<<<<<<<<<<<<<<<<<<<<<Version 1.0>>>>>>>>>>>>>>>>>>>>>>>#

import random

Dust_2 = ["A_site", "B_site", "Mid", "Long", "Short", "Under"]

Mirage = ["A_site", "B_site", "Mid", "Connector", "Palace", "Ramp"]

Inferno = ["A_site", "B_site", "Mid", "Banana", "Apartments"]

Nuke = ["A_site", "B_site", "Mid", "Ramp", "Silo", "Heaven"]

# current_map = []

map_result = None

while map_result != "exit":

    map_result = input("Enter the map: ")

    if map_result == "Dust_2":
        play_choice = random.choice(Dust_2)
    elif map_result == "Mirage":
        play_choice = random.choice(Mirage)
    elif map_result == "Inferno":
        play_choice = random.choice(Inferno)
    elif map_result == "Nuke":
        play_choice = random.choice(Nuke)
    # else:
    #     print("error")
    print(f"Random position: {play_choice}")
