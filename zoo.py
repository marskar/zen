class Snake:
    legs = 0

python = Snake

class Snake:
    def __init__(self, name):
        self.name = name

class Snake:
    def __init__(self, name):
        self.name = name
    def hiss(self):
        return f"Hisss! My name is {self.name}!"

class Snake:
    names = set()
    def __init__(self, name):
        self.name = name
        Snake.names.add(self.name)

class Snake:
    names = set()
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Snake.names.add(self.name)


class Snake:
    names = set()
    def __init__(self, name, species):
        self.name, self.species = name, species
        Snake.names.add(self.name)

class Snake:
    names = set()
    def __init__(self, name):
        self.name = name
        Snake.names.add(self.name)
    def remove(self):
        Snake.names.remove(self.name)
    def replace(self):
        Snake.names.add(self.name)
        
class Snake:
    inventory = {}
    def __init__(self, species, count = 1):
        self.species = species
        self.count = count
        Snake.inventory.update((self.species, self.count))

class Snake:
    inventory = {}
    def __init__(self, species):
        self.species = species
        if self.species in Snake.inventory.keys():
            Snake.inventory[self.species] += 1
        else:
            Snake.inventory.update({self.species: 1})


class Snake:
    names = set()
    inventory = {}
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Snake.names.add(self.name)
        if self.species in Snake.inventory.keys():
            Snake.inventory[self.species] += 1
        else:
            Snake.inventory.update({self.species: 1})

class Snake:
    def __init__(self, species, count = 1):
        self.species = species
        self.count = count

class Snake:
    inventory = {}
    def __init__(self, species, count = 1):
        self.species = species
        self.count = count
        Snake.inventory.update({self.species: self.count})
    def remove(self):
        Snake.inventory.pop(self.species)
    def add(self, delta = 1):
        self.count += delta
        Snake.inventory.update({self.species: self.count})

class Snake:
    inventory = {}
    def __init__(self, species, count = 1):
        self.species = species
        self.count = count
        Snake.inventory.update({self.species: self.count})
    def remove(self, delta = 1):
        if self.count >= delta:
            self.count -= delta
        else:
            return "Cannot have fewer than zero animals"
        if self.count == 0:
            Snake.inventory.pop(self.species)
        else:
            Snake.inventory.update({self.species: self.count})

            
