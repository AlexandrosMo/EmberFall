from classes import Character

name = input("Enter your character's name: ")

print(f"Welcome, {name}! Choose your class from the following options:")
for cls in Character.classes:
    print(cls)
class_type = input("Enter your class: ")
if class_type not in Character.classes:
    print("Invalid class selected. Please choose a valid class.")
else:
    print(f"You have chosen the {class_type} class. Good luck on your adventure, {name}!")
