import core
import time
from pygame.math import Vector2

def projectiles():

    p = Vector2(core.memory("pos"))
    v = Vector2(core.memory("Direction"))
    v.scale_to_length(core.memory("vitesse").length()+8)
    r = 5
    c = (255,255,255)
    st = time.time()

    dp = {"position": p, "vitesse": v, "rayon": r, "couleur": c, "startTime": st}
    core.memory("projectiles").append(dp)

def CadenceTir():

    if core.getKeyPressList("SPACE"):

        if len(core.memory("projectiles"))>0:
            if time.time()-core.memory("projectiles")[-1]["startTime"] > 1:
                projectiles()
        else:
            projectiles()

def DrawProj():

    for proj in core.memory("projectiles"):
        core.Draw.circle(proj["couleur"],proj["position"],proj["rayon"])

    for proj in core.memory("projectiles"):
        proj["position"]=proj["position"]+proj["vitesse"]

def SupprProj():

    for proj in core.memory("projectiles"):
        if time.time() - proj["startTime"] > 10:
            core.memory("projectiles").remove(proj)

def BordEcranProj():
    for proj in core.memory("projectiles"):
        if proj["position"].y < 0:
            proj["position"].y = core.WINDOW_SIZE[1]

        if proj["position"].x < 0:
            core.memory("projectiles")["position"].x = core.WINDOW_SIZE[1]

        if proj["position"].y > core.WINDOW_SIZE[1]:
            proj["position"].y = 0

        if proj["position"].x > core.WINDOW_SIZE[1]:
            proj["position"].x = 0