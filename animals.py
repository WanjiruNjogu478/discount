


class Animal:
     pass

animal = Animal()
dog = Animal()
cow = Animal()

print(animal,dog,cow)


class Animal:
    def __init__(self):
        print("web development")

animal = Animal()
print(animal)
print("---------------------------------------------")
dog = Animal()
print(dog)

class Animal:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

        print(f"My name is {self.name} i am {self.age} years old and my owner is {self.owner}")

animal = Animal( "Bosco", 4, "Wanjiru")
print("---------------------------------------------")
dog = Animal( "Osama", 6, "Larry")



# components of OPP
# inheritance - we are able to inherit class and methods
# encapsulation -keeping something private
# polymorphism - using the same method to get dif behaviours of the object
# abstraction - for example using the laptop, you don't have to understand everything about it



class Animal:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def sound(self):
        print(f"I am {self.name} and i produce bark sound")


creature = Animal( "Bosco", 4, "Wamjiru")

# access variables of the object
print(animal.age)
print("---------------------------")
creature.sound()


class Animal:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def sound(self):
        return f"I am {self.name} and i produce bark sound"


animal = Animal( "Bosco", 4, "Wamjiru")

# access variables of the object
print(f"age: {animal.age}")
print(f"name: {animal.name}")
print("---------------------------")
print(creature.sound())

#INHERITANCE

class Animal:
    def __init__(self):
        self.name = input("what is your name?")
        self.age = input("how old are you?")
        self.sound = input("which sound do you produce?")
        self.move = input("how do you move?")

    def get_sound(self):
        return f"I am {self.name} and i produce {self.sound} sound"

    def get_move(self):
        return f"I {self.move} very fast"

class Dog(Animal):
    pass

animal = Animal()
print(animal.get_sound())
print(animal.get_move())

print("----------------------------------------")
dog = Dog()
print(dog.get_sound())
print(dog.get_move())



class Animal:
    def __init__(self, name, age, sound, move):
        self.name = name
        self.age = age
        self.sound = sound
        self.move = move

    def get_sound(self):
        return f"I am {self.name} and i produce {self.sound} sound"

    def get_move(self):
        return f"I {self.move} very fast"

class Dog(Animal):
    def get_sound(self):
        return "i produce bark sound"

class Cat(Animal):
    def get_sound(self):
        return "i produce meow sound"


animal = Animal("sarah", 12, "speak", "run")
print(animal.get_sound())
print(animal.get_move())

print("----------------------------------------")
dog = Dog( "king", 6, "bark", "walk")
print(dog.get_sound())
print(dog.get_move())

print("----------------------------------------")
cat = Cat( "May", 4, "meow", "run")
print(cat.get_sound())
print(cat.get_move())






