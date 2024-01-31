#Strings
#Dada a frase Python é muito legal., use fatiamento para dar nome às variáveis contendo cada palavra. O resultado final deve ser:

#frase = "Python é muito legal."
## resolução do problema aqui
#palavra1
#"Python"
#palavra2
#"é"
#palavra3
#"muito"
#palavra4
#"legal"
#Qual o tamanho dessa frase? E qual o tamanho de cada palavra?

#Agora que conhecemos atribuição múltipla e o método str.split() refaça os dois exercícios anteriores usando essas técnicas.

#Use slicing (mais especificamente o passo do fatiamento) para inverter a string «Python».

phrase = 'Python é muito legal.'

word1 = phrase[0:6]
print(word1)
word2 = phrase[7:8]
print(word2)
word3 = phrase[9:14]
print(word3)
word4 = phrase[15:]
print(word4)

print(f'A frase tem {len(phrase)} letras')

print(f'A palavra {word1} tem {len(word1)} letras')

print(f'A palavra {word2} tem {len(word2)} letra')

print(f'A palavra {word3} tem {len(word3)} letras')
word4 = word4.replace('.', '')
print(f'A palavra {word4} tem {len(word4)} letras')

print('-' * 50)

phrase_split = phrase.split(' ')

print(phrase_split)

word1 = phrase_split[0]
print(word1)
word2 = phrase_split[1]
print(word2)
word3 = phrase_split[2]
print(word3)
word4 = phrase_split[3]
print(word4)

print(word1[::-1])