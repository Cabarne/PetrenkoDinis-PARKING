parking_places = 7
free_place = 3

print("#"*parking_places*5)

for place_index in range(1, parking_places + 1):
    if place_index == free_place:
        print("|   |", end="")
    else:
        print("| x |", end="")

print("\n", "#"*parking_places*5, sep="")