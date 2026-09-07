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

'''x,y=get_trajectory(v0, angle_deg)
range_distance=x[-1] #last x value = where it lands
print(f"The projectile lands{range_distance:.2f} units away.")
#plotting the trajectory
plt.plot(x,y)
plt.xlabel("horizontal dsitance covered")
plt.ylabel("vertical distance covered")
plt.title("Projectile Trajectory")
plt.show()'''

##(2)comparing different launch angles
'''for angle in [30,45,60]:
    x,y= get_trajectory(v0,angle)
    plt.plot(x,y, label=f"{angle} degrees")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("comparing launch angles")
plt.show()'''

#testing complementary angles (range similarity)
'''angle_pairs=[(20,70),(30,60),(40,50)]
for a1,a2 in angle_pairs:
    x1,y1=get_trajectory(v0,a1)
    x2,y2=get_trajectory(v0,a2)

    plt.plot(x1,y1,label=f"{a1}")
    plt.plot(x2,y2, label=f"{a2}", linestyle="--")

    print(f"{a1} lands at {x1[-1]:.2f} units")
    print(f"{a2} lands at {x2[-1]:.2f} units")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Complementary Angle Pairs- Same Range, Different Path")
plt.show()'''

##(3) Euler's method version
'''def get_trajectory_euler(v0,angle_deg, dt=0.01):
    angle= np.radians(angle_deg)
    vx=v0*np.cos(angle)
    vy=v0*np.sin(angle)

    x,y=0,0
    x_list, y_list=[x],[y]

    while y>= 0:
        x+= vx*dt
        y+=vy*dt
        vy-= g*dt
        x_list.append(x)
        y_list.append(y)
    return np.array(x_list), np.array(y_list)

#comparing exact formula with euler
x_exact,y_exact=get_trajectory(v0,45)
x_euler,y_euler=get_trajectory_euler(v0,45)

plt.plot(x_exact,y_exact,label="Exact formula")
plt.plot(x_euler,y_euler, label="Euler's method", linestyle="--")
plt.legend()
plt.title("Exact vs. Euler's Method")
plt.show()
#learnt how changing the 'dt' value significantly impacts the accuracy of the Euler method, larger dt = larger error'''

##(4) real world case with air resistance 
def get_trajectory_drag(v0,angle_deg,k=0.02,dt=0.01): #k=0.02 is a drag coeff
    angle=np.radians(angle_deg)
    vx=v0*np.cos(angle)
    vy=v0*np.sin(angle)

    x,y=0,0
    x_list,y_list=[x],[y]

    while y>=0:
        v=np.sqrt(vx**2 + vy**2)  #current speed
        ax_drag= -k*v*vx #drag's effect on horizontal velocity
        ay_drag= -k*v*vy #drag's effect on vertical velocity

        vx += ax_drag*dt
        vy+= (-g + ay_drag) *dt

        x += vx*dt
        y += vy*dt

        x_list.append(x)
        y_list.append(y)

    return np.array(x_list), np.array(y_list)

#comparing trajectory with air resistance and without
x_exact,y_exact= get_trajectory(v0,45)
x_drag,y_drag=get_trajectory_drag(v0,45)

plt.plot(x_exact,y_exact, label="No air resistance")
plt.plot(x_drag,y_drag, label="With air resistance", linestyle="--")
plt.legend()
plt.title("Effect of Air resistance")
plt.show()
#drag version has a noticeably shorter range
