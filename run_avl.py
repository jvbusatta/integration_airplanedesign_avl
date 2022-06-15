import os
import subprocess
import pandas as pd
import numpy as np

def open_avl():
    subprocess.call("D:\TCC\integration_airplanedesign_avl\avl.exe < D:\TCC\integration_airplanedesign_avl\command_file.in", shell=True)

open_avl()