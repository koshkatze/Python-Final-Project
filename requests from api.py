import requests

def get_wand_wood_values():
    url = "https://hp-api.onrender.com/api/characters"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the response
        data = response.json()

        wand_wood_values = set()  # Using a set to avoid duplicate entries

        for character in data:
            wand_wood = character["wand"]["wood"]
            if wand_wood:
                wand_wood_values.add(wand_wood)

        return list(wand_wood_values)

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

if __name__ == "__main__":
    wand_wood_values = get_wand_wood_values()
    print("Available wand wood values:")
    print(wand_wood_values)


import requests

def get_wand_core_values():
    url = "https://hp-api.onrender.com/api/characters"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the response
        data = response.json()

        wand_core_values = set()  # Using a set to avoid duplicate entries

        for character in data:
            wand_core = character["wand"]["core"]
            if wand_core:
                wand_core_values.add(wand_core)

        return list(wand_core_values)

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

if __name__ == "__main__":
    wand_core_values = get_wand_core_values()
    print("Available wand core values:")
    print(wand_core_values)


def get_spell_names():
    url = "https://hp-api.onrender.com/api/spells"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the response
        data = response.json()

        spell_names = []

        for spell in data:
            # The API structure might have changed, so we need to check if "name" key exists
            if "name" in spell:
                spell_name = spell["name"]
                spell_names.append(spell_name)

        return spell_names

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

if __name__ == "__main__":
    spell_names = get_spell_names()
    if spell_names:
        print("Available spell names:")
        for spell in spell_names:
            print(spell)
    else:
        print("No spell names found.")