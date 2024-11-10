from random import randint
from datetime import time
def horaRandom(min, max):
    hora = randint(min, max)
    mins = randint(0,59)
    seg = randint(0,59)
    
    return str(time(hora, mins, seg))