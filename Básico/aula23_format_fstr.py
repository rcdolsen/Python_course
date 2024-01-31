"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:_^10}')
print(f'{variavel:.<10}')
print(f'{variavel:a>10}')
print(f'{1000.2356784213:.1f}')
print(f'{1000.2356784213:,.1f}')
print(f'{1000.2356784213:+,.1f}')
print(f'{1000.2356784213:0=+10,.1f}')
hexa = input('Digite um numero para saber o hexadecimal')
hexa_int = int(hexa)
print(f'O hexadecimal de {hexa_int} e {hexa_int:08X}')
print(f'{variavel!r}')