import random

# Andre McDonald
# 04/26/2025
# P5HW
# This program will be a simple character creation game. 

def create_character():
    # Create a character with default attributes and allow the player to choose a class
    preset_classes = {
        "Warrior": ("A strong and brave fighter skilled in melee combat.", "Strength"),
        "Mage": ("A master of magical arts with high intelligence.", "Intelligence"),
        "Rogue": ("A stealthy and agile character skilled in dexterity.", "Dexterity"),
        "Cleric": ("A healer and protector with strong charisma.", "Charisma"),
    }

    print("Choose your character's class:")
    for cls, (description, _) in preset_classes.items():
        print(f"{cls}: {description}")

    while True:
        chosen_class = input("Enter your character's class: ")
        if chosen_class in preset_classes:
            break
        else:
            print("Invalid class. Please choose from the available options.")

    character = {
        "name": input("Enter your character's name: "),
        "class": chosen_class,
        "Home region": input("Enter your character's home region: "),
        "level": 1,
    }

    # Apply a 10% stat boost to the attribute associated with the chosen class
    _, boosted_attribute = preset_classes[chosen_class]
    character["boosted_attribute"] = boosted_attribute  # Store the boosted attribute for later use

    return character

def set_attributes(character):  
    # Set attributes for the character with random values that add up to the total number of attributes * 10
    total_points = 40  # 4 attributes * 10
    attributes = ["Strength", "Dexterity", "Intelligence", "Charisma"]
    assigned_points = [1] * len(attributes)  # Start with 1 point in each attribute to ensure minimum value
    total_points -= len(attributes)  # Subtract the initial points

    for i in range(total_points):
        assigned_points[random.randint(0, len(attributes) - 1)] += 1

    random.shuffle(assigned_points)  # Shuffle to randomize the distribution
    character["attributes"] = dict(zip(attributes, assigned_points))
    return character
    def pick_up_item(character):
        # Allow the character to pick up an item that gives a temporary boost to an attribute
        items = {
            "Potion of Strength": ("Strength", 5),
            "Elixir of Dexterity": ("Dexterity", 5),
            "Scroll of Intelligence": ("Intelligence", 5),
            "Charm of Charisma": ("Charisma", 5),
        }
        item = random.choice(list(items.keys()))
        attribute, boost = items[item]

        print(f"\nYou found a {item}!")
        print(f"It temporarily boosts your {attribute} by {boost} points.")

        # Apply the temporary boost
        character["attributes"][attribute] += boost
        display_character(character)

        # Remove the boost after a short explanation
        input("\nPress Enter to continue (the boost will wear off)...")
        character["attributes"][attribute] -= boost
        print(f"The effect of the {item} has worn off.")
def display_character(character):
    # Display the character's attributes
    print("\nCharacter Summary:")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Home Region: {character['Home region']}")
    print(f"Level: {character['level']}")
    print("Attributes:")
    for attr, value in character["attributes"].items():
        print(f"{attr}: {value}")

def combat(character):
    # Allow the character to engage in combat with randomly generated enemies
    enemies = ["Rat", "Bat", "Snake"]
    enemy = random.choice(enemies)
    enemy_level = character["level"] * 1.015
    enemy_attributes = {
        "Strength": int(character["attributes"]["Strength"] * 1.015),
        "Dexterity": int(character["attributes"]["Dexterity"] * 1.015),
        "Intelligence": int(character["attributes"]["Intelligence"] * 1.015),
        "Charisma": int(character["attributes"]["Charisma"] * 1.015),
    }

    print(f"\nA wild {enemy} appears!")
    print(f"{enemy}'s Level: {enemy_level:.2f}")
    print("Enemy Attributes:")
    for attr, value in enemy_attributes.items():
        print(f"{attr}: {value}")

    player_health = 100
    enemy_health = 100

    while player_health > 0 and enemy_health > 0:
        # Player's turn
        print("\nYour turn!")
        print("Choose an action: (1: Fight, 2: Defend, 3: Run, 4: Item)")
        action = input("Enter your choice: ")

        if action == "1":  # Fight
            if random.random() < 0.2:  # 20% chance to miss
                print("You missed!")
            else:
                damage = character["attributes"]["Strength"]
                if random.random() < 0.2:  # 20% chance for a critical hit
                    damage *= 1.5
                    print("Critical hit!")
                enemy_health -= damage
                print(f"You dealt {damage:.2f} damage to the {enemy}. Enemy health: {max(enemy_health, 0):.2f}")

        elif action == "2":  # Defend
            print("You brace yourself to reduce incoming damage.")

        elif action == "3":  # Run
            if random.random() < 0.5:  # 50% chance to successfully run
                print("You successfully ran away!")
                return
            else:
                print("You failed to escape!")

        elif action == "4":  # Item
            print("You don't have any items to use right now!")  # Placeholder for item functionality

        else:
            print("Invalid choice. You lose your turn.")

        if enemy_health <= 0:
            print(f"\nYou defeated the {enemy}!")
            character["level"] += 1
            print(f"Your level has increased to {character['level']}!")
            break

        # Enemy's turn
        print("\nEnemy's turn!")
        if random.random() < 0.2:  # 20% chance for the enemy to miss
            print(f"The {enemy} missed!")
        else:
            damage = enemy_attributes["Strength"]
            if random.random() < 0.2:  # 20% chance for a critical hit
                damage *= 1.5
                print("Critical hit by the enemy!")
            if action == "2":  # If the player defended, reduce damage by 1/3
                damage *= 2 / 3
                print("Your defense reduced the damage!")
            player_health -= damage
            print(f"The {enemy} dealt {damage:.2f} damage to you. Your health: {max(player_health, 0):.2f}")

        if player_health <= 0:
            print(f"\nThe {enemy} defeated you. Better luck next time!")
            break

def main():
    # Main function to run the character creation process
    print("Welcome to the Character Creation Game!")
    character = create_character()
    character = set_attributes(character)
    display_character(character)

    while True:
        action = input("\nWhat would you like to do? (1: Engage in combat, 2: Display character, 3: Exit): ")
        if action == "1":
            combat(character)
        elif action == "2":
            display_character(character)
        elif action == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
