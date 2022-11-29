import couchdb


# criando conexão
couch = couchdb.Server('http://admin:admin@localhost:5984')

couch.delete('test')

# criando uma database ()
db = couch.create('test')  # newly create

# assim apenas seleciona uma já criada
# db = couch['mydb']

# criando um doc que salvaremos no bd
doc = {'foo': 'bar'}

# salvado doc no bd e pegando o id
id = db.save(doc)

print(id)

# db.delete(doc)

for id in db:
    print(id)
