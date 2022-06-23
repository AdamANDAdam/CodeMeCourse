txt = 'abrakabar'

print(txt)

class Dogs:

    def __init__(self, name, colour, breed):#pierwsza podstawowa instancja
        self.name = name
        self.colour = colour
        self.breed = breed
    def bark(self):
        return (f'{self.name} bark!')
    def wag(self):
        return (f'{self.name}wag your tail!')

def main():

    Max = Dogs('Max', 'brown', 'German Shepherd')
    Boris = Dogs('Boris', 'Black', 'Puddle')

main()
