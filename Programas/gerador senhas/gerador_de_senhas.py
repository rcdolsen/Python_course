import json
import string
from pathlib import Path
from secrets import SystemRandom

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR/'senhas_geradas.json'
print(BASE_DIR)

try:
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        passwords = json.load(file)
except FileNotFoundError:
    passwords = []

letters = string.ascii_letters
numbers = string.digits
special = string.punctuation

new_password = (''.join(SystemRandom().choices(
    letters + numbers + special, k=9)))

site = input('Digite o site para essa senha: ').upper()
passwords.append(f'{site}: {new_password}')
# passwords.append(site)

with open(FILE_PATH, 'w', encoding='utf8') as file:
    json.dump(passwords, file, ensure_ascii=False, indent=2)

print(passwords)
