# -*- coding: utf-8 -*-
"""
Created on Thu May 18 20:49:34 2023

@author: mbelic
"""
import numpy as np
from scipy.stats import lognorm
from scipy.signal import resample


class SkinLightProperties:
    def __init__(self, num_cycles, cycle_duration, mean_energy, hit_probability):
        self.num_cycles = num_cycles
        self.cycle_duration = cycle_duration
        self.fs = 10
        self.hit_probability = hit_probability
        self.mean_energy = mean_energy
        self.num_photons = 1000
        self.photon_energy_stdev = 0.02
        
    def generate_photon_energy(self, mean_energy, std_dev):
        return np.random.normal(mean_energy, std_dev, self.num_photons)

    def generate_ppg_waveform(self):
        # Generate a single PPG pulse over a longer duration
        long_duration = 2.5  # duration of the long pulse in seconds
        time_long_pulse = np.linspace(0, long_duration, int(self.fs*long_duration))        
        mu, sigma = 0, 1        
        long_pulse = lognorm.pdf(time_long_pulse, sigma, scale=np.exp(mu))
        # Resample the long pulse to the desired duration
        single_pulse = resample(long_pulse, int(self.fs*self.cycle_duration))
 
        # Normalize the pulse to have a maximum amplitude of 1
        single_pulse /= np.max(single_pulse)

        waveform = np.tile(single_pulse, self.num_cycles)
        time = np.linspace(0, self.num_cycles*self.cycle_duration,
                           self.num_cycles*self.fs*self.cycle_duration)
        return time, waveform
    
    
    
    