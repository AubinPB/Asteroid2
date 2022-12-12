import time

import core
from Asteroid.Difficulté import difficulte
from Asteroid.Target import DrawTarget, collisionproj, CreationTarget, BordEcranTarget
from Asteroid.player import Deplacement, Controle, DrawPlayer, BordEcranPlayer
from Asteroid.projectile import CadenceTir, DrawProj, SupprProj, BordEcranProj


def Jeu():
    # if core.memory("etat",1):

    #Affichage

    # core.memory("timer", time.time()-core.memory("startTime"))
    # core.Draw.text((255, 255, 255), "Score : ", str(core.memory("point")),(100,100))
    # core.Draw.text((255, 255, 255), "Temps : ", str(core.memory("timer")),(100,200))
    # core.Draw.text((255, 255, 255), "Nombre de vies : ", str(core.memory("Vie")), (100, 300))


    # Joueur

    Deplacement()
    Controle()
    DrawPlayer()
    BordEcranPlayer()

    # Projectiles

    CadenceTir()
    DrawProj()
    SupprProj()
    BordEcranProj()

    # Boost()


    # Target

    DrawTarget()
    CreationTarget()
    collisionproj()
    BordEcranTarget()


    #Difficulté

    difficulte()



