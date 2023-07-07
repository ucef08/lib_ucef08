# lib_ucef08.py
import subprocess
import os

def fonction1():
    print("Ceci est la fonction 1 de ma bibliothèque.")


def maj(commentaire):
    os.chdir('/')  # équivalent de "cd /"
    os.chdir(os.getcwd())  # équivalent de "cd <répertoire courant>"
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commentaire])
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])


