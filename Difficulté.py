import time

import core

def difficulte():
    if time.time()-core.memory("temps")==30:
        core.memory("temps",time.time())
        core.memory("difficulte",core.memory("difficulte")+1)

