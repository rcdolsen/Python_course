#Crie uma lista com o nome das 3 pessoas mais próximas.

people = ['Mozuda', 'Marrom', 'Theo']
#Crie três listas, uma lista de cada coisa a seguir:

#frutas

fruit = ['apple', 'banana', 'blueberry']

#docinhos de festa (não se esqueça de brigadeiros!!)

sweet = ['brigadeiro', 'quindim']
#ingredientes de feijoada

feijoada = ['feijao', 'couve', 'orange']
#Lembre-se de salvá-las em alguma variável!

#Agora crie uma lista que contém essas três listas.

big_list = people + fruit + sweet + feijoada

big_dict = {
    'people': people,
    'fruit': fruit,
    'sweet': sweet,
    'feijoada': feijoada,
}

print(big_list)
print('-' * 50)
print(big_dict)
print('-' * 50)

#Nessa lista de listas (vou chamar de listona):

#você consegue acessar o elemento brigadeiro?

print(big_list[6])
print('-' * 50)

#Adicione mais brigadeiros à segunda lista de listona. O que aconteceu com a lista de docinhos de festa?
big_list.insert(6, 'mais brigadeiro')
print(big_list)
print('-' * 50)

#Adicione bebidas ao final da listona, mas sem criar uma lista!

#Utilizando o del, remova todos os elementos da lista criada anteriormente até a lista ficar vazia.
del big_list[:]
print(big_list)
print('-' * 50)
#Faça uma lista de compras do mês, não se esqueça de comprar produtos de limpeza e sorvete!
cleaning = ['soup', 'detergent', 'alcohol']
ice_cream = ['ice cream']

shopping_list = cleaning + ice_cream
print(shopping_list)
print('-' * 50)

#Agora «vá ao mercado» e delete apenas os produtos de limpeza da lista.

del shopping_list[0:3]
print(shopping_list)
print('-' * 50)

#Agora «vá à sorveteria» e se empanturre de sorvete e tire o sorvete da lista.

#Dado uma lista de números, faça com que os números sejam ordenados e, em seguida, inverta a ordem da lista usando slicing.\

numbers = [1, 564, 234, 43, 2, 5643]
numbers.sort()
print(numbers)
print('-' * 50)
print(numbers[::-1])