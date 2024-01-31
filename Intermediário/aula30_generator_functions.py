#generator = (n for n  in range(1000000))

#def generator(n=0):
#    yield 1 # pausar
#    print('continuando...')
#    yield 2
#    print('acabooooooouuuuu, acabooooouuuu')
#    return "E tetraaaaa"

#gen = generator(n=0)
#print(next(gen))
#print(next(gen))
#print(next(gen))

def generator2(n=0, max=10):
    while True:
        yield n
        n += 1

        if n >= max:
            return
        
gen = generator2()
for n in gen:
    print(n)

gen = generator2(max=1000)
for n in gen:
    print(n)

gen = generator2(n=3, max=10)
for n in gen:
    print(n)