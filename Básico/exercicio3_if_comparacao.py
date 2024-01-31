prim_valor = input('Digite um valor: ')
seg_valor = input('Digite outro valor: ')

if prim_valor > seg_valor:
    print(
        f'{prim_valor = } e maior que '
        f'{seg_valor = }')
elif seg_valor > prim_valor:
    print(
        f'{seg_valor = } e maior que '
        f'{prim_valor = }')
else:
    print('Os valores sao iguais')