import numpy as np
import pandas as pd
import itertools
from astropy.stats import sigma_clip

def adc(signal, gain, offset):
    signal = signal.astype(np.float64)

    signal /= gain
    signal += offset

    return signal

def calibration(signal, dead, dark, dt, line_corr, flat):

    '''
    Calibrating the input signal data imagery using the calibration databases to remove noise \n

    Parameters: \n
    signal : input signal imagery \n
    dead : dead pixel map \n
    dark : dark pixel map \n
    dt : Time integration \n
    lin_corr : Linear correction \n
    flat : Flat field map \n

    Returns -> Calibrated Signal imagery
    
    '''

    # masking dead and dark pixels from the signals

    hot = sigma_clip(
        sigma= 5, maxiters= 5, data= dark
    )

    hot = np.tile(hot, (signal.shape[0], 1, 1))
    dead = np.tile(dead, (signal.shape[0], 1, 1))

    signal = np.ma.masked_where(dead, signal)
    signal = np.ma.masked_where(hot, signal)


    # dark current subtraction

    dark = np.ma.masked_where(dead, dark)

    dark = np.tile(dark, (signal.shape[0], 1,1))

    signal -= dark * dt[:, np.newaxis, np.newaxis]

    # linearity correction

    line_corr = np.flip(line_corr, axis = 0)

    for x,y, in itertools.product(
        range(signal.shape[1]), range(signal.shape[2])

    ): 
        poli = np.poly1d(line_corr[:, x,y])
        signal[:, x,y] = poli(signal[:, x,y])


    # flat field correction

    flat = flat.transpose(1,0)
    dead = dead.transpose(1,0)

    flat = np.ma.masked_where(dead, flat)
    flat = np.tile(flat, (signal.shape[0], 1,1))

    signal = signal / flat 

    return signal


