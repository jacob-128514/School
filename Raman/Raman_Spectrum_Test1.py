import numpy as np
import pandas as pd
import scipy.signal as sp
import matplotlib.pyplot as plt

#USB2000 Ocean Optics Emulator from pypi.org/project/seatease/
import seatease.spectrometers as s

#Declaring spectrometer
spec = s.Spectrometer.from_first_available()

#For getting a specific spectrometer (in case it's not recognizing):
#spec = s.Spectrometer.from_serial_numer("serial number")

#Set integration time:
spec.integration_time_micros(70*1000) # 70 ms

#Converting wavelengths to waveshifts
Laser_wavelength = 532
Length = len(spec.intensities())
waveshifts = np.empty(Length)

for i in range(0, Length):
    waveshifts[i] = ((1/Laser_wavelength)-(1/spec.wavelengths()[i]))*10**7

#Storing intensities and waveshifts
xvalues = np.array(waveshifts)
yvalues = np.array(spec.intensities())

#Finding local maxima (within N data points to filter noise)
N = 100
ymaxes = sp.argrelextrema(yvalues, np.greater, order = N)

#Formatting and displaying plot
plt.plot(xvalues,yvalues)
plt.scatter(xvalues[ymaxes], yvalues[ymaxes], c = 'g')
plt.title('Generic Spectrum')
plt.xlabel("Raman Shift ($\mathregular{cm^{-1}}$)")
plt.ylabel("Intensity")
plt.show()
