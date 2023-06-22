# Active (TinyScanner)

TinyScanner est un outil simple et efficace de balayage de ports, écrit en Python. Il prend en charge le balayage de ports TCP et UDP sur un hôte spécifié et peut balayer une plage de ports.

## Installation

Pour installer et utiliser TinyScanner, vous aurez besoin de Python 3.6 ou supérieur.

1. Clonez le dépôt dans votre espace de travail local :
```
git clone https://zone01normandie.org/git/max92/active.git
cd active
```

## Utilisation

Pour utiliser TinyScanner, exécutez le fichier `main.py` avec l'adresse de l'hôte que vous souhaitez scanner et les options de votre choix.

- Pour un balayage TCP :
```
python3 main.py -t <host> -p <port ou plage de ports>
```
- Pour un balayage UDP :
```
python3 main.py -u <host> -p <port ou plage de ports>
```

Par exemple, pour effectuer un balayage TCP sur les ports 80 à 90 de l'hôte 127.0.0.1, vous pouvez utiliser la commande suivante :
```
python3 main.py -t 127.0.0.1 -p 80-90
```


## Licence

Lemesle Maxence





