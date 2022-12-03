import couchdb


# criando conexão
couch = couchdb.Server('http://admin:admin@localhost:5984')

# couch.delete('test')


def pessoa_helper(pessoa) -> dict:
    return {
        'id': str(pessoa['_id']),
        'nome': pessoa['nome'],
        'endereco': pessoa['endereco'],
        'email': pessoa['email'],
        'idade': pessoa['idade'],
    }


# assim apenas seleciona uma já criada
try:
    # assim apenas seleciona uma já criada
    db = couch['test']
    # print(db)

except couchdb.ResourceNotFound:
    # criando uma database ()
    db = couch.create('test')  # newly create


db = couch['test']

# criando um doc que salvaremos no bd
doc = {'nome': 'Vítor',
       'email': 'vitor@email.com',
       'endereco': 'rua bonita, 123 - Cidade, Estado, País',
       'idade': 20}

# salvado doc no bd e pegando o id
id1, bla1 = db.save(doc)


recuperado = db.get(id1)
doc_atualizado = {'nome': 'rodrigues',
                  'email': 'rodrigues@email.com',
                  'endereco': 'asdfasdfsadf',
                  'idade': 24}

if recuperado:
    recuperado['nome'] = doc_atualizado['nome']
    recuperado['email'] = doc_atualizado['email']
    recuperado['endereco'] = doc_atualizado['endereco']
    recuperado['idade'] = doc_atualizado['idade']
    db[id1] = recuperado

print(db.get(id1)['nome'])

# db.delete(doc)
# for id in db:
#     print(db[id]['nome'])

couch.delete('test')
