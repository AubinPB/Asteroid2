import core
import random
from pygame import *
import time

def Target():

    x = random.randint(0, 750)
    y = random.randint(0, 750)
    l = 50
    h = 50
    st = time.time()
    c = (255, 0, 0)
    v = Vector2(random.uniform(-3,3), random.uniform(-3,3)) # attention vitesse doit etre différent de 0

    dt = {"position": Vector2(x, y), "dimension": Vector2(l,h), "startTime": st, "couleur": c, "vitesse": v}
    core.memory("target").append(dt)
    core.memory("targetRect", Rect(dt["position"], dt["dimension"]))

def CreationTarget():
    if len(core.memory("target")) > 0:
        if time.time() - core.memory("target")[-1]["startTime"] > 10/core.memory("difficulte"):
            Target()
    else:
        Target()
        Target()
        Target()
        Target()
        Target()



def DrawTarget():
    for t in core.memory("target"):
        core.Draw.rect(t["couleur"],(t["position"],t["dimension"]),0)

    for t in core.memory("target"):
        t["position"]=t["position"]+t["vitesse"]


def collisionproj():
    for t in core.memory("target"):
        core.memory("targetRect", Rect(t["position"], t["dimension"]))
        for proj in core.memory("projectiles"):
            if core.memory("targetRect").collidepoint(proj["position"].x, proj["position"].y):
                core.memory("point",core.memory("point")+1)
                core.memory("projectiles").remove(proj)
                core.memory("target").remove(t)

def collisionplayer():
    for t in core.memory("target"):
        core.memory("targetRect", Rect(t["position"], t["dimension"]))
        if core.memory("targetRect").collidepoint(core.memory("pos")):
            core.memory("point", core.memory("point") + 1)
            core.memory("Vie",core.memory("Vie")-1)
            core.memory("projectiles").remove(t)
            reset()

def reset():
    core.memory("pos", Vector2(400, 400))
    core.memory("vitesse", Vector2(1, 0))
    core.memory("Direction", Vector2(1, 0))

def BordEcranTarget():
    for t in core.memory("target"):
        if t["position"].y < 0:
            t["position"].y = core.WINDOW_SIZE[1]

        if t["position"].x < 0:
            t["position"].x = core.WINDOW_SIZE[1]

        if t["position"].y > core.WINDOW_SIZE[1]:
            t["position"].y = 0

        if t["position"].x > core.WINDOW_SIZE[1]:
            t["position"].x = 0
