import random
import requests


def red(text):
    return "\033[31m{}\033[0m".format(text)


def brightred(text):
    return "\033[91m{}\033[0m".format(text)


def green(text):
    return "\033[32m{}\033[0m".format(text)


def yellow(text):
    return "\033[33m{}\033[0m".format(text)


def blue(text):
    return "\033[34m{}\033[0m".format(text)


def magenta(text):
    return "\033[35m{}\033[0m".format(text)


def cyan(text):
    return "\033[36m{}\033[0m".format(text)


characters = "https://hp-api.onrender.com/api/characters"
spells = "https://hp-api.onrender.com/api/spells"

response = requests.get(characters)
characters = response.json()

response = requests.get(spells)
spells = response.json()

# Filter so that only characters with a house and DoB show:
filtered_characters = [character for character in characters if
                       character.get('house') and character.get('dateOfBirth') and character.get('wand') and character[
                           'wand'].get('wood') and character['wand'].get('core') and character['wand'].get('length')]

# Define the mapping of wand woods to integer values
wand_wood_mapping = {
    "mahogany": 1,
    "willow": 2,
    "walnut": 3,
    "hornbeam": 4,
    "chestnut": 5,
    "cherry": 6,
    "birch": 7,
    "ash": 8,
    "vine": 9,
    "oak": 10,
    "holly": 11,
    "cedar": 12,
    "cypress": 13,
    "fir": 14,
    "hawthorn": 15,
    "larch": 16,
    "yew": 17,
}

# Define the mapping of wand cores to integer values
wand_core_mapping = {
    "phoenix feather": 1,
    "dragon heartstring": 2,
    "unicorn hair": 3,
    "unicorn tail-hair": 4,
}

# Define the mapping of spell names to integer values
spell_mapping = {
    "Aberto": 1,
    "Accio": 2,
    "Aguamenti": 3,
    "Alohomora": 4,
    "Anapneo": 5,
    "Aparecium": 6,
    "Apparate": 7,
    "Ascendio": 8,
    "Avada Kedavra": 9,
    "Avis": 10,
    "Bat": 11,
    "Bombardo": 12,
    "Brackium Emendo": 13,
    "Capacious Extremis": 14,
    "Confundo": 15,
    "Conjunctivitis Curse": 16,
    "Crinus Muto": 17,
    "Crucio": 18,
    "Diffindo": 19,
    "Disillusionment Charm": 20,
    "Disapparate": 21,
    "Engorgio": 22,
    "Episkey": 23,
    "Expecto patronum": 24,
    "Erecto": 25,
    "Evanesco": 26,
    "Expelliarmus": 27,
    "Ferula": 28,
    "Fidelius Charm": 29,
    "Fiendfyre Curse": 30,
    "Finite Incantatem": 31,
    "Furnunculus Curse": 32,
    "Geminio": 33,
    "Glisseo": 34,
    "Homenum Revelio": 35,
    "Homonculus Charm": 36,
    "Immobulus": 37,
    "Impedimenta": 38,
    "Incarcerous": 39,
    "Imperio": 40,
    "Impervius": 41,
    "Incendio": 42,
    "Langlock": 43,
    "Legilimens": 44,
    "Levicorpus": 45,
    "Locomotor Mortis": 46,
    "Lumos": 47,
    "Morsmordre": 48,
    "Mucus Ad Nauseam": 49,
    "Muffliato": 50,
    "Nox": 51,
    "Obliviate": 52,
    "Obscuro": 53,
    "Oculus Reparo": 54,
    "Oppugno": 55,
    "Petrificus Totalus": 56,
    "Periculum": 57,
    "Piertotum Locomotor": 58,
    "Protean Charm": 59,
    "Protego": 60,
    "Reducto": 61,
    "Reducio": 62,
    "Renneverate": 63,
    "Reparifors": 64,
    "Reparo": 65,
    "Rictusempra": 66,
    "Riddikulus": 67,
    "Scourgify": 68,
    "Sectumsempra": 69,
    "Serpensortia": 70,
    "Silencio": 71,
    "Sonorus": 72,
    "Spongify": 73,
    "Stupefy": 74,
    "Tarantallegra": 75,
    "Unbreakable Vow": 76,
    "Wingardium Leviosa": 77,
}

# Initialize player and computer scores
player_score = 0
computer_score = 0

# Create a line break
line_break = "_______________________________________________________________________________________________________________________________________________\n"

# Create the welcome message
welcome_message = f"________________________________________________ {yellow('Welcome to the Harry Potter Top Trumps game!')} _________________________________________________\n\n"
welcome_message += "__________________________ In this game, you will be facing off against the computer in a battle of wits and magic. ___________________________\n"
welcome_message += "_____________ You will each take turns selecting a character from the Harry Potter universe and compare their magical abilities. ______________\n\n"
welcome_message += f"______________________________________ The player with the most {magenta('power')} for each category wins the round. _______________________________________\n\n"
welcome_message += "_________ The game continues until all categories have been compared, and the player with the most rounds won is the ultimate winner! _________\n"
welcome_message += "_______________________ Get ready to delve into the magical world of Harry Potter and may the best witch or wizard win! _______________________\n"

# Print the line break
print(line_break)

# Print the welcome message
print(welcome_message)

# Print the line break
print(line_break)

# Prompt the user to press any key to begin
input(f"Press {cyan('any key')} to begin: ")


def print_category_message():
    print(f"\n{red('Invalid choice. Please choose a valid category')} "
          f"{yellow('1')}/"
          f"{green('2')}/"
          f"{cyan('3')}/"
          f"{brightred('4')}. \n")


# Create a loop for 5 rounds
for round_num in range(1, 6):

    # Generate the random character and spell for the player
    player_character = random.choice(filtered_characters)
    player_spell = random.choice(spells)

    # Generate a different random character and spell for the computer
    filtered_characters.remove(player_character)  # Remove the player's character from the list
    computer_character = random.choice(filtered_characters)
    computer_spell = random.choice(spells)

    # Convert wand wood strings to their corresponding integer values using the mapping dictionary
    player_wand_wood = player_character['wand']['wood']
    player_wand_wood_value = wand_wood_mapping.get(player_wand_wood.lower(),
                                                   0)  # Default value of 0 if not found in the mapping
    computer_wand_wood = computer_character['wand']['wood']
    computer_wand_wood_value = wand_wood_mapping.get(computer_wand_wood.lower(),
                                                     0)  # Default value of 0 if not found in the mapping

    # Convert wand core strings to their corresponding integer values using the mapping dictionary
    player_wand_core = player_character['wand']['core']
    player_wand_core_value = wand_core_mapping.get(player_wand_core.lower(),
                                                   0)  # Default value of 0 if not found in the mapping
    computer_wand_core = computer_character['wand']['core']
    computer_wand_core_value = wand_core_mapping.get(computer_wand_core.lower(),
                                                     0)  # Default value of 0 if not found in the mapping

    # Convert spell names to their corresponding integer values using the mapping dictionary
    player_spell_name = player_spell['name']
    player_spell_value = spell_mapping.get(player_spell_name, 0)  # Default value of 0 if not found in the mapping
    computer_spell_name = computer_spell['name']
    computer_spell_value = spell_mapping.get(computer_spell_name, 0)  # Default value of 0 if not found in the mapping

    # Create the player character selection message
    player_card = f"{green('You have received the following card:')}\n"
    player_card += f"Name: {player_character['name']}\n"
    player_card += f"House: {player_character['house']}\n"
    player_card += f"Date of Birth: {player_character['dateOfBirth']}\n"
    player_card += f"Ancestry: {player_character['ancestry']}\n"
    player_card += f"Wand wood: {player_character['wand']['wood']}\n"
    player_card += f"Wand core: {player_character['wand']['core']}\n"
    player_card += f"Wand length: {player_character['wand']['length']}\n"
    player_card += f"Spell: {player_spell['name']} | Action: {player_spell['description']}\n"

    # Create the computer character selection message
    computer_card = "Your opponent has received the following card: \n"
    computer_card += f"Name: {computer_character['name']}\n"
    computer_card += f"House: {computer_character['house']}\n"
    computer_card += f"Date of Birth: {computer_character['dateOfBirth']}\n"
    computer_card += f"Ancestry: {computer_character['ancestry']}\n"
    computer_card += f"Wand wood: {computer_character['wand']['wood']}\n"
    computer_card += f"Wand core: {computer_character['wand']['core']}\n"
    computer_card += f"Wand length: {computer_character['wand']['length']}\n"
    computer_card += f"Spell: {computer_spell['name']} | Action: {computer_spell['description']}\n"

    # Print the line break
    print(line_break)

    # Print the round number before starting each round
    print(f"{yellow('Round number:')} {round_num}\n")

    # Print the line break
    print(line_break)

    # Print the player card
    print(player_card)

    # Print the computer card
    # print(computer_card)

    # Print the line break       # f"{red('TEXT')}
    print(line_break)

    print(f"Your opponent has the {blue(computer_character['name'])} card\n")
    print("\n".join([
        "Choose a category to compare:",
        f"{yellow('1. Wand Wood')}",
        f"{green('2. Wand core')}",
        f"{cyan('3. Spell name')}",
        f"{brightred('4. Wand length')}"
    ]))

    while True:
        try:
            choice = int(input("\nEnter the number of your choice "
                               f"{yellow('1')}/"
                               f"{green('2')}/"
                               f"{cyan('3')}/"
                               f"{brightred('4')}: \n"))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print(red("\nInvalid choice"))
                continue
        except ValueError:
            print(red('\nInvalid choice'))
            continue

    # Determine the player's chosen category and get the corresponding value
    chosen_category = None
    player_chosen_value = None
    player_chosen_category_str = None

    if choice == 1:
        chosen_category = "wand wood"
        player_chosen_value = player_wand_wood_value
        player_chosen_category_str = player_wand_wood
    elif choice == 2:
        chosen_category = "wand core"
        player_chosen_value = player_wand_core_value
        player_chosen_category_str = player_wand_core
    elif choice == 3:
        chosen_category = "spell name"
        player_chosen_value = player_spell_value
        player_chosen_category_str = player_spell_name
    elif choice == 4:
        chosen_category = "wand length"
        player_wand_length = player_character['wand']['length']
        if isinstance(player_wand_length, (int, float)):  # Check for both integer and float types
            player_chosen_value = player_wand_length
            player_chosen_category_str = str(player_wand_length)  # Convert integer to string for consistent printing
        else:
            player_chosen_value = 0  # Default value of 0 if the wand length is not an integer
            player_chosen_category_str = "N/A"
    else:
        print_category_message()
        exit()

    # Get the computer's chosen value for the same category
    computer_chosen_value = None

    if chosen_category == "wand wood":
        computer_chosen_value = computer_wand_wood_value
        computer_chosen_category_str = computer_wand_wood
    elif chosen_category == "wand core":
        computer_chosen_value = computer_wand_core_value
        computer_chosen_category_str = computer_wand_core
    elif chosen_category == "spell name":
        computer_chosen_value = computer_spell_value
        computer_chosen_category_str = computer_spell_name
    elif chosen_category == "wand length":
        computer_wand_length = computer_character['wand']['length']
        if isinstance(computer_wand_length, (int, float)):  # Check for both integer and float types
            computer_chosen_value = computer_wand_length
            computer_chosen_category_str = str(
                computer_wand_length)  # Convert integer to string for consistent printing
        else:
            computer_chosen_category_str = "N/A"
            computer_chosen_value = 0  # Assign a default value for comparison

    # Determine the winner of the round
    if player_chosen_value > computer_chosen_value:
        winner = "You have won this round!"
        player_score += 1
    elif player_chosen_value < computer_chosen_value:
        winner = "The computer wins this round"
        computer_score += 1
    else:
        winner = "You have tied this round"

    # Print the line break
    print(line_break)

    # Print the result of the round
    print(
        f"{magenta('Player')} {chosen_category}: {player_chosen_category_str.capitalize()} (Power: {player_chosen_value})")
    print(
        f"{blue('Computer')} {chosen_category}: {computer_chosen_category_str.capitalize()} (Power: {computer_chosen_value})")
    print(f"{yellow('Result:')} {winner}\n")
    print(f"{yellow('Current scores:')}")
    print(f"{magenta('Player:')} {player_score} | {blue('Computer:')} {computer_score}\n")

    # Print the line break
    print(line_break)

    # Ask the user to continue or terminate
    while True:
        try:
            choice = int(input(f"Enter {cyan('1')} to continue or {red('2')} to rage quit: \n"))
            if choice == 1:
                break
            elif choice == 2:
                print(f"You have chosen to {red('terminate')} the game. Goodbye!")
                exit()
            else:
                print(red("\nInvalid choice"))
                continue
        except ValueError:
            print(red("\nInvalid choice"))
            continue

# Print the line break
print(line_break)

# Determine the overall winner     # f"{red('TEXT')}
if player_score > computer_score:
    overall_winner = f"{yellow('Congratulations! You are the overall winner!')}"
elif player_score < computer_score:
    overall_winner = f"{red('The computer is the overall winner. Better luck next time!')}"
else:
    overall_winner = f"{green('It is a tie! There is no overall winner.')}"

# Print the overall winner
print(f"{yellow('Finishing scores:')}")
print(f"{magenta('Player:')} {player_score} | {blue('Computer:')} {computer_score}\n")
print(overall_winner)
