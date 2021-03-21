# Compile Python latest version

## Compiler la derniere version de Python
```shell
sudo apt-get update
sudo apt-get upgrade
wget https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz
tar -zxvf Python-3.9.2.tgz 
cd Python-3.9.2
sudo apt-get -y install build-essential  # install gcc et ses outils
sudo apt-get -y install libreadline-dev  # permet le rappel des commandes
sudo apt-get -y install libsqlite3-dev   # sqlite
sudo apt-get -y install libssl-dev libffi-dev libgdm-dev # libraries systeme
sudo apt-get -y install zlib1g-dev  lzma-dev libbz2-dev  # libraries de compression
sudo apt-get -y install uuid-dev  # creer des uuid
gcc --version  # should be 9.3.0
./configure --enable-optimizations --enable-shared
# Profile guided optimization (PGO) et Link Time Optimization (LTO).
# significant speed boost 10%-20%. 
# Creation d'une shared library pour l'ajouter ensuite dans postgresql
make -j`nproc`  # compile le code en parallele sur les cores
sudo make install # install dans la directory /usr/local/bin
```

## Mise a jour de l'environnement de votre user 
```shell
vi ~/.profile
# ajouter dans votre ~/.bashrc
export PATH=$PATH:/usr/local/bin
export LD_LIBRARY_PATH=/usr/local/bin:$LD_LIBRARY_PATH
source ~/.bashrc
python3 
et tapez Ctrl-d pour sortir du prompt
```

## Verifier les parametres techniques de la version compilee
```
python3 -c "import sysconfig;print('{}'.format('\n'.join(['{} = {}'.format(v, sysconfig.get_config_var(v)) for v in sorted(sysconfig.get_config_vars(), key=lambda s: s.lower())])))" > /tmp/python3.conf
```
Editez le fichier /tmp/python3.conf 
Voir dans le fichier la ligne 29 , pour verifier l'application des optimisations du compilateur

## Mise en place du virtualenv sous Ubuntu
```shell
cd tp-bac-4
python3 -m venv venv
source venv/bin/activate
```
## Installation des packages de test et de verification de code
```shell
pip3 install pytest flake8 pylint
```

## Ecriture d'un premier programme de type hello-world
```python
#!/usr/bin/env python3
# Purpose: Say hello
print('Hello, World')
```
Verification des LF et CRLF encodings types et presentation du shebang , et du File PATH  

## Premiers tests
```shell
pip3 install pytest
pytest -v hello.py
```

## Mettre le fichier executable 
```shell
chmod +x hello.py
```

## Prise en compte des arguments
```python
#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')
```
Verification 
```shell
./hello-argparse.py
./hello-argparse.py  Test
```
Continuer l'etude avec les codes source suivants: 
```shell
hello-optional-arg.py
hello-main.py
hello-get-args.py
hello-docstring.py
```

## Checking style et errors
```shell
pip3 install flake8 pylint black ipython mypy yapf
```
Pour garder la liste des packages python installes 
```shell
pip3 freeze > requirement.txt
```
Cette commande formate le code 
```shell
  yapf -i hello.py
```






