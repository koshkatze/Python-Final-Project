import random
import requests
from pprint import pprint

url = 'https://hp-api.onrender.com/api/characters'

response = requests.get(url)

characters = response.json()

# Filter so that only characters with a house and DoB show:
filtered_characters = [character for character in characters if character.get('house') and character.get('dateOfBirth')]

# Generate the random character
character = random.choice(filtered_characters)

print(f"You have received the following card: ")
print(f"Name: {character['name']}")
print(f"Gender: {character['gender']}")
print(f"House: {character['house']}")
print(f"Date of Birth: {character['dateOfBirth']}")
print(f"Ancestry: {character['ancestry']}")