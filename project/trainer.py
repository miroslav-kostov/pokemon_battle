from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, pokemon=[]):
        self.name = name
        self.pokemon = pokemon

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        else:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        current_pokemon = []
        for poke in self.pokemon:
            if poke.name == pokemon_name:
                current_pokemon.append(poke)
        if len(current_pokemon) > 0:
            self.pokemon.remove(current_pokemon[0])
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        res = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for poke in self.pokemon:
            res += f"- {poke.pokemon_details()}"
        return res

#trainer = Trainer("Stamat")
#pokemon = Pokemon("Pesho", 90)
#print(trainer.add_pokemon(pokemon))
#print(trainer.add_pokemon(pokemon))
#print(trainer.release_pokemon("Pesho"))
#print(trainer.release_pokemon("Pesho"))