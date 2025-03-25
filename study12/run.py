from draw2d import *
from draw3d import *
from vectors import add,scale
from math import *

import matplotlib.pyplot as plt

def trajectory(theta,speed=20,height=20,dt=0.01,g=-9.81):
    vx=speed*cos(pi*theta/180)
    vz=speed*sin(pi*theta/180)
    t,x,z=0,0,height
    ts,xs,zs=[t],[x],[z]
    while z>=0:
        t+=dt
        vz+=g*dt
        x+=vx*dt
        z+=vz*dt
        ts.append(t)
        xs.append(x)
        zs.append(z)
    return ts,xs,zs

def plot_trajectory_metric(find_data,angles,height=0):
    datas=[find_data(trajectory(theta,height=height)) for theta in angles]
    plt.scatter(angles,datas)
    plt.show()
def landing_position(traj):
    return traj[1][-1]
def hand_time(traj):
    return traj[0][-1]
def max_height(traj):
    return max(traj[2])
def z(t):
    return 20*sin(45*pi/180)*t+(-9.81/2)*t**2
def r(theta):
    return (-2*20*20/-9.81)*sin(theta*pi/180)*cos(theta*pi/180)
angles=range(0,90,5)

plot_trajectory_metric(landing_position,angles,height=10)