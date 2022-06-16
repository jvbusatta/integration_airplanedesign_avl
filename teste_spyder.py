# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:42:29 2022

@author: User
"""

import os
import subprocess32
import pandas as pd
import numpy as np

def open_avl():
    subprocess32.call("D:\TCC\integration_airplanedesign_avl\avl.exe < D:\TCC\integration_airplanedesign_avl\command_file.in", shell=True)

open_avl()
print(np.__path__)