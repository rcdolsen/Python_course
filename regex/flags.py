# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall \n
import re

texto = '''
131.768.460-53 qdjhgv
055.123.060-50efas
955.123.060-90
'''

print(re.findall(r'\d{3}.\d{3}.\d{3}-\d{2}', texto))

print('')

print(re.findall(r'^\d{3}.\d{3}.\d{3}-\d{2}', texto))

print('')

print(re.findall(r'^\d{3}.\d{3}.\d{3}-\d{2}$', texto, re.M))

print('')

texto2 = '''O João gosta de folia E adora ser amado'''

texto3 = '''O João gosta de folia
E adora ser amado'''

print(re.findall(r'^o.*o$', texto2, flags=re.I))
print(re.findall(r'^o.*o$', texto3, flags=re.I))
print(re.findall(r'^o.*o$', texto3, flags=re.I | re.S))
