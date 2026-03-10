import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
time = np.arange(0,10,dt)

target = 10
position = 0

Kp = 1.2
Ki = 0.2
Kd = 0.05

integral = 0
prev_error = 0

positions = []

for t in time:

    error = target - position
    
    integral += error*dt
    
    derivative = (error - prev_error)/dt
    
    control = Kp*error + Ki*integral + Kd*derivative
    
    position += (control - 0.1*position) * dt
    
    positions.append(position)
    
    prev_error = error


plt.plot(time,positions)
plt.axhline(target,color='r',linestyle='--')
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("PID Control Simulation")
plt.savefig("pid_response.png")
plt.show()