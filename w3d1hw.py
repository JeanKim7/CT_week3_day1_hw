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



#====================================================================
# Exercise 2 - Turn the shopping cart program into an object-oriented program
# Create a class called cart that retains items and has methods to add, remove, and show



class ShoppingCart:
    """class that represents an online shopping cart"""

    def __init__(self, items = []):
        self.items=items

    def add(self, added_item):
        self.items.append(added_item)
        print(f"{added_item.title()} has been added to your shopping cart!")

    def remove(self, removed_item):
        self.items.remove(removed_item)
        print(f"{removed_item.title()} has been removed from your shopping cart!")

    def show(self):
        print(self.items)

    def clear(self):
        self.items.clear()


user_input=""
while user_input != "quit":
    user_input = input("Enter an option below to use your shopping cart!\n"
                       "Enter one of the following options (Add/Remove/Show/Clear/Quit): ").lower()
    
    shopping_cart1 = ShoppingCart()

    if user_input == "add":
        add_input = input("What item would you like to add to your shopping cart? ")
        shopping_cart1.add(add_input)
    
    elif user_input == "remove":
        remove_input = input("What item would you like to remove from your shopping cart? ")
        if remove_input in shopping_cart1.items:
            shopping_cart1.remove(remove_input)
        else:
            print(f"{remove_input} is not in your shoping cart!")
            continue

    elif user_input == "show":
        if shopping_cart1.items:
            print(shopping_cart1.items)
        else: 
            print("Your shopping cart is empty!")
            continue

    elif user_input == "clear":
        shopping_cart1.clear()
        print("Your shopping cart has been cleared!")
        continue

    elif user_input == "quit":
        continue
    
    else:
        print("Please choose one of the correct inputs!")
        continue