# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula14_json_dump_load.json'
CAMINHO_ABSOLUTO = os.path.abspath(  # redundante, nao e necessario
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)
print(__file__)
print('-' * 40)

print(CAMINHO_ABSOLUTO)
print('-' * 40)

dict_movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO, 'w', encoding='utf-8') as archive:
    json.dump(dict_movie, archive, ensure_ascii=False, indent=2)
# print(dict_movie)

with open(CAMINHO_ABSOLUTO, 'r', encoding='utf-8') as archive:
    filme_do_json = json.load(archive)
    print(filme_do_json)
