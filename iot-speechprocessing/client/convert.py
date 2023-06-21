# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:24:41 2020

@author: Samira Breitling
"""

from scipy.io.wavfile import read
import numpy as np


def convert(wave_datei):
    try:
        a = read(wave_datei)
        a = np.array(a[1])

        print(a)

        return a

    except UnboundLocalError:
        print("No valid data could be found!")