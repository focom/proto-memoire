# Prototype pour le memoire de Pierre Valentin

## Importer le code sur votre machine

```
git clone https://github.com/focom/proto-memoire.git
cd proto-memoire
```

Si votre machine possede pipenv:
```
pipenv install
```

Sinon avec pip faites:
```
pip install -r requirements.txt
```
### Installer tkinter (librarie pour le gui) sur votre machine 
#### Sur Window
Tkinter est deja installer avec votre version de python sinon, installer la derniere version de python en cochant l'option tkinter
#### Sur Ubuntu/Debian :
```
sudo apt install python3-tk
```
#### Sur CentOS/Fedora : 
```
sudo dnf install python3-tkinter 
```

## Launch the neo4j server 
```
docker run -d --publish=7474:7474 --publish=7687:7687 --volume=neo4j:/data --name neo4j --env NEO4J_AUTH=neo4j/root neo4j
```

Une fois les dependances installees, executer le code avec 

```
python3 src/main.py
```