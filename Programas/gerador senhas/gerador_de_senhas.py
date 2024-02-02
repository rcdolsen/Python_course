import json
import string
from secrets import SystemRandom

FILE_PATH = 'Programas\gerador senhas\senhas_geradas.json'

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
