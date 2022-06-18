from cmath import sqrt
import os
import subprocess
import pandas as pd
import numpy as np
import math




def avl():
    subprocess.call("avl.exe < command_file.in", shell=True)
avl()

def aerodynamic():

    #taper ratio
    lamda = (c_tip/c_root)
    
    #aspect ratio
    AR = (pow(b,2))/S

    
    #p.62 RAYMER
    S = w/ ( w / S)
    b = sqrt(AR * S)
    c_root = 2 * ( S / ( b * (1 + lambda)))
    c_tip = lamba * c_root

    #mean chordwise
    c_med = (2/3)*c_root*((1+ lambda + pow(lambda,2))/(1 + lambda))
    
    #distance in the y axie 
    Y_med = (b/6)*((1 + 2 * lambda)*(1 + lambda))

    #aerodynamic center
    c_a = 0.25 * c_med

    