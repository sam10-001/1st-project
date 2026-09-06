#code to simulate projectile motion using python
'''equations needed: 
x=u*cos(theta)*t 
y=u*sin(theta)*t-0.5*g*t^2 
t=2*u*np.sin(theta)/g

'''
import numpy as np
import matplotlib.pyplot as plt
g=9.8 #gravity, m/s^2

##(1)computing the trajectory
def get_trajectory(v0, angle_deg): #v0=initial velocity, angle_deg=angle in degrees
    angle=np.radians(angle_deg)     
    t_flight=2*v0*np.sin(angle)/g   #time of flight
    t=np.linspace(0,t_flight,100)
    x=v0*np.cos(angle)*t
    y=v0*np.sin(angle)*t-0.5*g*t**2
    return x,y
#now we take input from user and find the trajectory
v0=float(input("Enter initial velocity"))
angle_deg=float(input("Enter launch angle in degrees"))

x,y=get_trajectory(v0, angle_deg)
range_distance=x[-1] #last x value = where it lands
print(f"The projectile lands{range_distance:.2f} units away.")
#plotting the trajectory
plt.plot(x,y)
plt.xlabel("horizontal dsitance covered")
plt.ylabel("vertical distance covered")
plt.title("Projectile Trajectory")
plt.show()

##(2)comparing different launch angles
for angle in [30,45,60]:
    x,y= get_trajectory(v0,angle)
    plt.plot(x,y, label=f"{angle} degrees")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("comparing launch angles")
plt.show()
