for i in range(10): # o 10 nao e incluido
        if i == 2:
            print('i e 2, pulando...')
            continue

        if i == 8:
            print('i e 8, seu else nao sera executado')
            break

        for j in range(1, 3): # O 3 nao e  incluido
            print(i, j)

else:
    print('For completo com sucesso')