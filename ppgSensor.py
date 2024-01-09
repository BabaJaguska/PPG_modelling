# -*- coding: utf-8 -*-
"""
Created on Thu May 18 20:51:11 2023

@author: mbelic
"""
import numpy as np
import matplotlib.pyplot as plt


class Photodiode:
    def __init__(self, threshold_energy):
        self.threshold_energy = threshold_energy
        self.dark_current = 0.1  # [uA]
        self.num_electrons = 500

    def simulate_current(self, skin_light_properties):
        time, waveform = skin_light_properties.generate_ppg_waveform()
        current = []
        for light_intensity in waveform:
            photon_energy = skin_light_properties.generate_photon_energy(
                skin_light_properties.mean_energy,
                skin_light_properties.photon_energy_stdev,
            )
            photon_energy *= light_intensity
            high_energy_photons = photon_energy > self.threshold_energy
            hits = (
                np.random.rand(skin_light_properties.num_photons)
                < skin_light_properties.hit_probability
            )
            num_hits = np.sum(hits & high_energy_photons)
            num_excited_electrons = min(num_hits, self.num_electrons)
            current_ = (
                num_excited_electrons * 1 / self.num_electrons
                + self.dark_current
            )
            current.append(current_)
        return np.array(current)


class PPGSensor:
    def __init__(self, photodiode):
        self.photodiode = photodiode
        self.current_red = None
        self.current_ir = None

    def calculate_SpO2(
        self, skin_light_properties_red, skin_light_properties_ir
    ):
        # Simulate photodiode current for both red and infrared light
        self.current_red = self.photodiode.simulate_current(
            skin_light_properties_red
        )
        self.current_ir = self.photodiode.simulate_current(
            skin_light_properties_ir
        )
        R = np.mean(self.current_red) / np.mean(self.current_ir)
        SpO2 = 110 - 25 * R  # Some linear relationship for SpO2 calculation
        return np.round(SpO2, 1)

    def plotSignal(self, time, ideal_waveform):
        # Plot simulated photodiode current
        plt.figure(figsize=(8, 4))
        plt.subplot(2, 1, 1)
        plt.plot(time, self.current_red, label="Red Light")
        plt.plot(time, self.current_ir, label="Infrared Light")
        plt.title("Simulated Photodiode Current", size=14)
        plt.xlabel("Time (s)", size=13)
        plt.ylabel("Current (uA)", size=13)
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(time, ideal_waveform)
        plt.title("Ideal waveform")
        plt.tight_layout()
        plt.show()
