# lib_ucef08.py
import subprocess
import os
import pandas as pd
import requests
from io import StringIO

def Google_Drive_csv(lien):
    url = lien
    r = requests.get(url)
    data = r.content
    return (pd.read_csv(StringIO(data.decode('utf-8'))))


def maj(commentaire):
    os.chdir('/')  # équivalent de "cd /"
    os.chdir(os.getcwd())  # équivalent de "cd <répertoire courant>"
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commentaire])
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])


