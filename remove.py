#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:21:10 2019
@author: jlee
"""

import numpy as np
import glob, os


# ----- Need to be manually revised! ----- #
dir_rerun = '/data/jlee/HSC_virgo/MACSJ0916-JFG1/Red/rerun/'
make_fringe = True    # y-band (NB0921, NB0926, and NB0973 are not available yet.) (default: False)
# ---------------------------------------- #


# --------------------------------------------- #
# ----- Directories (rerun : calibration) ----- #
# --------------------------------------------- #
direc = [dir_rerun+'calib_bias/',
         dir_rerun+'calib_dark/',
         dir_rerun+'calib_flat/',
         dir_rerun+'calib_sky/']
if make_fringe:
    direc.append(dir_rerun+'calib_fringe')

# ----- Removing & writing removing log files ----- #
current_dir = os.getcwd()
for k in np.arange(len(direc)):
    print('# ----- Working on '+direc[k]+' ----- #'+'\n')
    os.chdir(direc[k])
    os.system('rm -rfv * > rmlog.txt')
os.chdir(current_dir)


# ---------------------------------------- #
# ----- Directories (rerun : object) ----- #
# ---------------------------------------- #
dir_obj = dir_rerun+'object/'
os.chdir(dir_obj)
sub_dir = sorted(glob.glob('*'))
direc = []
for k in sub_dir:
    try:
        test_integer = int(k)
        direc.append(dir_obj+k+'/')
    except ValueError:
        if (k == 'deepCoadd'):
            direc.append(dir_obj+k+'/')
        else:
            continue

# ----- Removing & writing removing log files ----- #
current_dir = os.getcwd()
for k in np.arange(len(direc)):
    print('# ----- Working on '+direc[k]+' ----- #'+'\n')
    os.chdir(direc[k])
    os.system('rm -rfv * > rmlog.txt')
os.chdir(current_dir)
