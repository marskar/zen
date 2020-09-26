import this
with open('zen.txt', 'w') as f:
    f.write("".join([this.d.get(c, c) for c in this.s]))

with open('zen.txt', 'r') as f:
    my_list = [line for line in f]

with open('zen.txt') as f:
    text = f.read()

def read(file):
    with open(file) as f:
        return f.read()



class TextFile:
    def read(file):
        with open(file) as f:
            return f.read()

MyClass.file2list('zen.txt')

text = read('zen.txt')

text.splitlines()[0]

from this import s
from codecs import decode
with open('zen.txt', 'w') as f:
    f.write(decode(s, 'rot-13'))

class SimplestPossibleClass:
    pass

SimplestPossibleClass.class_attribute = 'stores data'


class MyClass:
    class_attribute = 'stores data'

# Lists

list(1, 2, 3)

['a', 'b', 'c']

# Tuples

tuple(1, 2, 3)

'a', 'b', 'c'

('a', 'b', 'c')


# Sets

set(1, 2, 3)

{'a', 'b', 'c'}

# Dictionary

{'a': 1, 'b': 2, 'c': 3}

letters = 'a', 'b', 'c'
numbers = 1, 2, 3
dict(zip(letters, numbers))

dict([['a',1], ['b',2], ['c',3]]) # list of lists

dict((['a',1], ['b',2], ['c',3])) # list of tuples

dict([{'a',1}, {'b',2}, {'c',3}]) # list of sets

dict((('a',1), ('b',2), ('c',3))) # tuple of tuples

dict((['a',1], ['b',2], ['c',3])) # tuple of lists

dict(({'a',1}, {'b',2}, {'c',3})) # tuple of sets

from dataclasses import dataclass
@dataclass
class Snake:
    species: str

royal_python = Snake(species = "Python regius")

@dataclass
class TextFile:
    text: list    

# Instantiation
from dataclasses import dataclass

@dataclass
class TextFile:
    filename: str

    def read(self):
    with open(self.file) as f:
        self.lines = f.read()

zen = TextFile('zen.txt')
zen.read()

# Or
zen = TextFile(file='zen.txt')

def read(self):
    with open(self.file) as f:
        self.lines = [line for line in f]

TextFile.read = read
zen.read()
zen.lines

TextFile.read('zen.txt')



@dataclass
class TextFile:
    filename: str

    def read(self):
        with open(self.file) as f:
            self.text = f.read()


zen = TextFile('zen.txt', [])

zen.lines
zen = TextFile(file = 'zen.txt')
zen.file

def read(self):
    with open(self.file) as f:
        self.text = f.read()

TextFile.read = read


zen.read()

zen.lines = []
zen.read()
zen.lines[0]
def reset(self):
    del self.lines


@dataclass
class TextFile:
    count = 0
    file: str
    
    def read(self):
        with open(self.file) as f:
            self.lines = f.read()
        TextFile.count += 1

    def reset(self):
        del self.lines
        TextFile.count -= 1

@dataclass
class TextFile:
    """Informative docstring"""
    count = 0
    file: str

    def read(self) -> list:
        with open(self.file) as f:
            self.lines = f.read()
        TextFile.count += 1

    def reset(self) -> None:
        del self.lines
        TextFile.count -= 1

