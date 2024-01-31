# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma(a, b, /, x, y):
    print(a + b + x + y)
    print('*' * 50)

#soma(a=1, b=2, x=3, y=4) # Retorna erro em a e b pq deveriam ser exclusivamente posicionais e nao nomeados

soma(1, 2, 3, y=4) # x e y podem ser nomeados

def soma2(a, b, *args):
    print(args)
    print(a + b)
    print(args, b, a)
    print('*' * 50)
    
soma2(1, 2, 'Qualquer', 'coisa')

def soma3(a, b, *, c): # Tudo depois do * e' nomeado e antes pode ser nomeado ou posicional
    print(a + b + c)
    print('*' * 50)

#soma3(1, 2, 3) # retorna erro pq c nao e nomeado

soma3(1, b=2, c=3)

def soma4(a, b, /, *, c): # Tudo depois do * e' nomeado e antes da / deve ser posicional
    print(a + b + c)
    print('*' * 50)

#soma4(1, b=2, c=3)# retorna erro pq b e nomeado

soma4(1, 2, c=3)

def soma5(a, b, /, *, c, **kwargs): # Tudo depois do * e' nomeado e antes da / deve ser posicional
    print(a + b + c)
    print(kwargs)
    print('*' * 50)

#soma4(1, b=2, c=3)# retorna erro pq b e nomeado

soma5(1, 2, c=3, teste='TeStE')