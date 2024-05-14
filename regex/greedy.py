# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
'''

# Greedy, returns until the last check
print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))

# non greeedy (lazy), returns until the first check
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))
