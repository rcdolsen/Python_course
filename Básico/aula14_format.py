a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

print(formato)

string = 'a={1} b={0} c={nome3:.2f} d={1}'
formato = string.format(a, b, nome3=c)
# a,b,c sao argumentos; nomex sao parametros
#tudo que vem depois de um parametro nomeado tambem precisa ser nomeado

print(formato)