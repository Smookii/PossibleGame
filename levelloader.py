import json
from os import path
class LevelLoader():
    @staticmethod 
    def loadLevel(filename):   
        with open(path.join(path.dirname(path.abspath(__file__)),filename)) as f:
            return json.load(f)