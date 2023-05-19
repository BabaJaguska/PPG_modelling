from ppgSensor import PPGSensor, Photodiode
from skinLightProperties import SkinLightProperties


# Constants
threshold_energy = 1.1 # [eV]
num_cycles, cycle_duration = 20, 1
mean_energy_red, hit_probability_red = 1.9, 0.2
mean_energy_ir, hit_probability_ir  = 1.2, 0.48

# Instantiate sensor and skin properties
photodiode = Photodiode(threshold_energy)
skin_light_red = SkinLightProperties(num_cycles, cycle_duration,
                                     mean_energy_red, hit_probability_red)
skin_light_ir = SkinLightProperties(num_cycles, cycle_duration,
                                    mean_energy_ir, hit_probability_ir)
ppg_sensor = PPGSensor(photodiode)

# Calculate SpO2
SpO2 = ppg_sensor.calculate_SpO2(skin_light_red, skin_light_ir)
print("Simulated SpO2: ", SpO2)

# Plot the signal
time, ideal_waveform = skin_light_red.generate_ppg_waveform()
ppg_sensor.plotSignal(time, ideal_waveform)


