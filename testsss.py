from BotExtensions import *
import os

_dir = os.listdir("./BotExtensions")

def load_ext():
    for i in _dir:
        print(f"Loading {i}")
        i.hithere()


load_ext()
