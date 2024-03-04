#Exercise 1 - Write a Python class for an Animal that has a name and energy attributes. 
#The animal class should also have methods for eat, sleep, and play that will take 
#in an integer and increase/decrease the energy of the animal with a formatted print statement

# Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) -> "Buddy is sleeping for 10 minutes. His energy is now 15"

class Animal:
    """A class tbat represents an animal"""

    def __init__(self, name, energy=100):
        self.name = name
        self.energy = energy

    def eat(self, num):
        self.energy +=  num
        print(f"{num} food has given {self.name} {num} energy!")
        print(f"energy = {self.energy}")

    def play(self, num):
        self.energy -= num
        print(f"{num} play has taken {num} energy from {self.name}!")
        print(f"energy = {self.energy}")

def sleep(animal_instance, num):
    animal_instance.energy += num
    print(f"{num} hours of sleep has given {animal_instance.name} {num} energy!")
    print(f"energy = {animal_instance.energy}")

giraffe = Animal('giraffe')
print(f"The giraffe has {giraffe.energy} energy.")
giraffe.play(50)
giraffe.play(10)
giraffe.eat(10)
sleep(giraffe, 20)