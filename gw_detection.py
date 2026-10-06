'''if you choose to let python automatically download strain data use following code (NOTE:network issue might cause problems)
#download the data
import os'''
from gwpy.timeseries import TimeSeries
gps_time=1126259462
'''filename="gw150914_data.hdf5"
if os.path.exists(filename):
    data=TimeSeries.read(filename)

else:
    data=TimeSeries.fetch_open_data('H1',gps_time-16,gps_time+16)
    data.write(filename)
print(data)'''

#using data from local file
from gwpy.timeseries import TimeSeries
import h5py
import numpy as np

filename="gw150914_data.hdf5"

with h5py.File(filename,'r') as f:
    strain=f['strain']['Strain'][:]
    gps_start=f['meta']['GPSstart'][()]
    duration=f['meta']['Duration'][()]
sample_rate=len(strain)/duration
data=TimeSeries(strain,sample_rate=sample_rate,t0=gps_start,name='H1:Strain')
print(data)

#plotting the data
import matplotlib.pyplot as plt
plot=data.plot()
plt.xlabel("Time")
plt.ylabel("Strain")
plt.title('Raw H1 Strain Data around GW150914')
plt.show()
'''this gives a really dense,messy, noisy looking squiggle with gw signal of very low amplitude, we need to apply some signal processing to see the gw signal'''

#whitening
white_data=data.whiten()
plot=white_data.plot()
plt.xlabel("time")
plt.ylabel("whitened strain")
plt.title("whitened H1 strain data around GW150914")
plt.show()

#bandpass filter + zoom into the actual merger time
bandpassed=white_data.bandpass(50,300)

#GW150914 merger happens right around gps_time itself
zoomed=bandpassed.crop(gps_time-0.2,gps_time+0.1)
plot=zoomed.plot()
plt.xlabel("time")
plt.ylabel("filtered strain")
plt.title("filtered H1 strain near GW150914 merger")
plt.show()