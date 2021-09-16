import numpy as np
from gekko import GEKKO

def objective(x):
    print("Called")
    return ((x-3.1)**2) + 5

m = GEKKO()

m.options.SOLVER = 1

x1 = m.Var(value=0, integer=True)

m.Obj(objective(x1))

m.solve(disp=False)

print(x1.value)