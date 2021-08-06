class RangeExample:
    def range_method(self):
        for i in range(10):
            print("range_method", i)

    def range_start_stop(self):
        for i in range(2, 10):
            print("range_start_stop", i)

    def range_step(self):
        for i in range(0,10,2):
            print("range_step", i)

    def range_reverse(self):
        for i in range(10,0,-2):
            print("range_step", i)

    def reversed_range(self):
        for i in reversed(range(0,10,1)):
            print("range_step", i)


class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.');


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')


d = Dog()
print('')
bat = NonMarineMammal('Bat')


obj1 = RangeExample()
# obj1.range_method()
# obj1.range_start_stop()
# obj1.range_step()
obj1.reversed_range()

