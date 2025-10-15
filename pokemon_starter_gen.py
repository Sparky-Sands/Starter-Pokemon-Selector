import random
x = "A wild pokemon has entered the scene!"
y = "The pokemon fled!"
z = "You caught the pokemon!"
pokemon_list = ["Bulbasaur", "Charmander", "Squirtle", "Chikorita" "Cyndaquil", "Totodile", "Treecko", "Torchic", "Mudkip", "Turtwig", "Chimchar", "Piplup", "Snivy", "Tepig", "Oshawott", "Chespin", "Fennekin", "Froakie", "Rowlet", "Litten", "Popplio", "Grookey", "Scorbunny", "Sobble", "Sprigatito", "Fuecoco", "Quaxly"]

while True:
    input("Press Enter to choose a random starter...")
    selected_item = random.choice(pokemon_list)
    print(f"Your starter is..... {selected_item}!")
