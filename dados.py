import random

def tirada_dados():
    tirada1 = random.randint(1, 6)
    tirada2 = random.randint(1, 6)
    return tirada1, tirada2

tirada1, tirada2 = tirada_dados()
print(f"tu lanzamiento uno fue {tirada1} y el dos fue {tirada2}")
