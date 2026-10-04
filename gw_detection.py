#fetching real strain data for GW150914
from gwpy.timeseries import TimeSeries
#GW150914 was detected at GPS time 1126259462
gps_time=1126259462

data=TimeSeries.fetch_open_data('H1', gps_time-16,gps_time+16)
print(data)
