import numpy as np

data = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, dtype=str)

time = data[:,0]
temperature = data[:,1].astype(float)
humidity = data[:,2].astype(float)
battery = data[:,3].astype(float)

print("Sensor statistics:")
print("temperature avg=", np.mean(temperature), "min=", np.min(temperature), "max=", np.max(temperature))
print("humidity avg=", np.mean(humidity), "min=", np.min(humidity), "max=", np.max(humidity))
print("battery avg=", np.mean(battery), "min=", np.min(battery), "max=", np.max(battery))

max_temp_time = time[np.argmax(temperature)]
print("Time of highest temperature:", max_temp_time)

low_battery = np.sum(battery < 30)
print("Number of times battery < 30%:", low_battery)
