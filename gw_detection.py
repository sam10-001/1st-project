'''if you choose to let python automatically download strain data use following code (NOTE:network issue might cause problems)
#download the data
import os
from gwpy.timeseries import TimeSeries
gps_time=1126259462
filename="gw150914_data.hdf5"
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
'''import matplotlib.pyplot as plt
plot=data.plot()
plt.xlabel("time")
plt.ylabel("Strain")
plt.title('Raw H1 Strain Data around GW150914')
plt.show()'''
