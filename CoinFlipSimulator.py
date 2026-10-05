#program outputs PISMO/GLAVA, based on random number mod 2, after user klicks RUN

import random

if random.randint(1,10) % 2 == 0:
    print("PISMO")
else:
    print("GLAVA")     