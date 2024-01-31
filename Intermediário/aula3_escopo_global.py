"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 'x'
y = 'y'

def escopo():
    x = 'x do escopo'

    def outra_funcao():
        x = 'x da outra funcao'
        print(x, '---', y)

    outra_funcao()
    print(x)  

print(x)
escopo()
print(x)

print('---------------')

x = 'x'
y = 'y'

def escopo():
    global x # Ma pratica (deixa confuso)
    x = 'x do escopo'

    def outra_funcao():
        x = 'x da outra funcao'
        y = 'y da outra funcao'
        print(x,'---', y)

    outra_funcao()
    print(x)  

print(x)
escopo()
print(x)