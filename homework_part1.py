import math
import matplotlib

def present_value_calculation(C, r, t):
    """
    present_value_calculation: explain
    C: explain
    r: explain
    t: explain
    PV: explain
    """
    PV = C/((1+r)**t)

    return PV

C_ten = 100
r_ten = 0.03
t_ten = 10  

PV_ten = present_value_calculation(C_ten, r_ten, t_ten)

print(PV_ten)

  





