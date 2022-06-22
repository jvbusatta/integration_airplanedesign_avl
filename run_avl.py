from cmath import sqrt
import os
import subprocess
import pandas as pd
import numpy as np
import math

def avl():
    subprocess.call("avl.exe < arq_comandos.in", shell=True)

avl()

def teste():
    
    if os.path.exists("coef_aerodynamic.txt") and os.path.exists("coef_aerodynamic_2.txt"):

        read_file = pd.read_csv("coef_aerodynamic.txt", skiprows = [0,1,2,3,4,5,6,7], delim_whitespace = True)
        read_file.to_csv("coef_aerodynamic.csv", index = None)

        df = pd.read_csv("coef_aerodynamic.csv")

        AoA = float(df._get_value(3, 2, takeable = True))
        CL_tot = float(df._get_value(9, 2, takeable = True))
        CD_tot = float(df._get_value(10, 2, takeable = True))

        print(df)
        print('------------------------------------------------')
        print('Ângulo de ataque avaliado (AoA): ', AoA)
        print('Coeficiente de sustentação (CL): ', CL_tot)
        print('Coeficiente de arrasto (CD): ', CD_tot)

teste()

print('------------------------------------------------------------')

def stability():

    df = pd.read_csv("coef_aerodynamic.csv")
    
    
    CL_tot_1 = float(df._get_value(9, 2, takeable = True))
    CM_tot_1 = float(df._get_value(7, 5, takeable = True))
    n_lines =  len(df)
    print(df)

    print('Coeficiente de momento: ',CM_tot_1)
    print('Coeficiente de sustentação : ',CL_tot_1)
    print('Número de linhas do arquivo de texto: ', n_lines)    

stability()
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
    
    #distance y  
    Y_med = (b/6)*((1 + 2 * lambda)*(1 + lambda))

    #aerodynamic center
    c_a = 0.25 * c_med
'''
