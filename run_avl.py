from cmath import sqrt
import os
import subprocess
import pandas as pd
import numpy as np
import math




def avl():
    subprocess.call("avl.exe < command_file.in", shell=True)

avl()

def teste():
    
    if os.path.exists("Aerodynamic_coefficients.txt") and os.path.exists("Aerodynamic_coefficients_5.txt"):

        read_file = pd.read_csv("Aerodynamic_coefficients.txt", skiprows=8, delim_whitespace=True)
        read_file.to_csv("Aerodynamic_coefficients.csv", index=None)

        df = pd.read_csv("Aerodynamic_coefficients.csv")

        CL_tot = float(df._get_value(9, 2, takeable = True))
        CD_tot = float(df._get_value(10,2, takeable= True))
        print('Coeficiente de sustentação: ', CL_tot)
        print('Coeficiente de arrasto: ', CD_tot)

teste()


'''
def aerodynamic():

    #taper ratio
    lamda = (c_tip/c_root)
    
    #aspect ratio
    AR = (pow(b,2))/S

    
    #p.62 RAYMER
    S = w / ( w / S)
    b = sqrt(AR * S)
    c_root = (2 * ( S / ( b * (1 + lambda))))
    c_tip = lamba * c_root

    #mean chordwise
    c_med = ((2/3)*c_root*((1+ lambda + pow(lambda,2))/(1 + lambda)))
    
    #distance in the y axie 
    Y_med = (b/6)*((1 + 2 * lambda)*(1 + lambda))

    #aerodynamic center
    c_a = 0.25 * c_med
'''
