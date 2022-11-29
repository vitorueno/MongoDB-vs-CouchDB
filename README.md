
```sh
sudo apt install mongodb 
```


```sh
docker pull couchdb                                                                                        
docker run -d --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=admin -p 5984:5984 couchdb:latest
```