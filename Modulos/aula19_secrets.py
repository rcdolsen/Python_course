# secrets gera números aleatórios seguros

import secrets
import string as s
from secrets import SystemRandom as sr

print(''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))

print(secrets.randbelow(100))
print(secrets.choice([10, 11, 12]))
