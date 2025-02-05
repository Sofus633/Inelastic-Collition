import pygame
import json
SCREEN_SIZE = [800, 600]
FPS = 60
screen = pygame.display.set_mode(SCREEN_SIZE)


def open_log():
    with open("simlog.json", "r") as openfile:
        jsons = json.load(openfile)
    return jsons

def getid():
    return len(open_log())

def get_log(id):
    return open_log()[id]


def setjsonvalue(id, values):
    print("adding " + str(id))
    jsons = open_log()
    if not id in jsons:
        jsons[id] = {}
    if id in jsons:
        jsons[id][len(jsons[id])] = values
    print(jsons)
    with open("simlog.json", "w") as file:
        json.dump(jsons, file, indent=4)