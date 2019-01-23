# Prototype pour le memoire de Pierre Valentin


Pour installer les dependences, installer le packet manager pipenv puis:
```
pipenv install
```

Sinon avec pip faite:
```
pip install -r requirements.txt
```
## To install tkinter
on fedora : sudo dnf install python3-tkinter 


## Launch the neo4j server 
```
docker run -d --publish=7474:7474 --publish=7687:7687 --volume=neo4j:/data --env NEO4J_AUTH=neo4j/root neo4j
```