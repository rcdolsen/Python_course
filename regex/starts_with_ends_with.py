# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação


import re

nif = '147.852.963-12'
nif_start = 'ajhwdfg 147.852.963-12'
nif_end = '147.852.963-12 iyteafd'
nif2 = 'jyafegd 147.852.963-12 aghsjfd'
nif_messed = '1ret47.85gfsd2.9nucedh63-1sdgs2'

print('*' * 20, ' ^ ', '*' * 20)

print("right", re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', nif))
print("wrong start", re.findall(
    r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', nif_start))
print("wrong end", re.findall(
    r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', nif_end))
print("wrong start end", re.findall(
    r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', nif2))

print('*' * 20, ' $ ', '*' * 20)

print("right", re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', nif))
print("wrong start", re.findall(
    r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', nif_start))
print("wrong end", re.findall(
    r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', nif_end))
print("wrong start end", re.findall(
    r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', nif2))

print('*' * 20, ' ^ and $ ', '*' * 20)

print("right", re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', nif))
print("wrong start", re.findall(
    r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', nif_start))
print("wrong end", re.findall(
    r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', nif_end))
print("wrong start end", re.findall(
    r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', nif2))

print('*' * 20, ' [] ', '*' * 20)

print("right", *re.findall(r'[^a-z]', nif_messed))
print("right", *re.findall(r'[^a-z]+', nif_messed))


print("right", re.findall(r'[^0-9 a-z]+', nif_messed))
