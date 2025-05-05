# PPG_modelling
[![Python Workflow Linux](https://github.com/BabaJaguska/PPG_modelling/actions/workflows/basic_workflow.yaml/badge.svg)](https://github.com/BabaJaguska/PPG_modelling/actions/workflows/basic_workflow.yaml)


If your fitness watch is reporting your heart rate without asking you to touch it with the opposite hand, it's likely using PPG (Photoplethysmography) and not ECG (Electrocardiography). ECG requires electrodes on two sides of the body, while PPG can be measured unilaterally. PPG is also the technology behind the clamp that goes on your finger to measure oxygen saturation.

PPG works by shining light onto the skin and measuring the amount of light that is reflected. The amount of light absorbed by the blood vessels changes with each heartbeat due to the increase in blood volume in the arteries caused by the heart contracting and pushing blood out into the circulatory system. The photons reflected off the skin surface hit the photosensitive diode in the PPG sensor which then produces current when its electrons get excited by the incoming photons, proportional to the intensity of light.

Oxygen saturation is measured using dual-wavelength PPG. The reason for using two wavelengths, typically red and infrared, is that oxygenated and deoxygenated hemoglobin absorb these wavelengths differently - oxygenated hemoglobin absorbs more infrared light, while deoxygenated hemoglobin absorbs more red light. By comparing the absorption at these two wavelengths, the sensor can estimate the level of oxygen saturation in the blood. 

Here's a very simple PPG model in Python. The waveform 📈 is modelled using a log-normal function (A more complex model can be found in (Sološenko et al, 2017, Computers in Biology and Medicine)). Different body absorption of the two wavelengths is represented by different probabilities for the photons to hit the diode, but perhaps there was a better way. 


![image](https://github.com/user-attachments/assets/87040449-ef8d-41c1-8e01-9715a69e9495)
