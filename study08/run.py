import matplotlib.pyplot as plt
import numpy as np

def plot_function(f,tmin,tmax,tlabel=None,xlabel=None,axes=False, **kwargs):
    ts = np.linspace(tmin,tmax,1000)
    if tlabel:
        plt.xlabel(tlabel,fontsize=18)
    if xlabel:
        plt.ylabel(xlabel,fontsize=18)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    if axes:
        total_t = tmax-tmin
        plt.plot([tmin-total_t/10,tmax+total_t/10],[0,0],c='k',linewidth=1)
        plt.xlim(tmin-total_t/10,tmax+total_t/10)
        xmin, xmax = plt.ylim()
        plt.plot([0,0],[xmin,xmax],c='k',linewidth=1)
        plt.yslim(xmin,xmax)

def plot_volume(f,tmin,tmax,axes=False,**kwargs):
    plot_function(f,tmin,tmax,tlabel="time (hr)", xlabel="volume (bbl)", axes=axes, **kwargs)

def plot_flow_rate(f,tmin,tmax,axes=False,**kwargs):
    plot_function(f,tmin,tmax,tlabel="time (hr)", xlabel="flow rate (bbl/hr)", axes=axes, **kwargs)

def average_flow_rate(v,t1,t2):
    return (v(t2)-v(t1))/(t2-t1)
def volume(t):
    return (t-4)**3 / 64 + 3.3
def decreasing_volume(t):
    if t < 5:
        return 10 - (t**2)/5
    else:
        return 0.2*(10-t)**2
def flow_rate(t):
    return 3*(t-4)**2 / 64
def secant_line(f,x1,x2):
    def line(x):
        return f(x)+(x-x1)*((f(x2)-f(x1))/(x2-x1))
    return line
def plot_secant(f,x1,x2,color='k'):
    line=secant_line(f,x1,x2)
    plot_function(line,x1,x2,c=color)
    plt.scatter([x1,x2],[f(x1),f(x2)],c=color)


def interval_flow_rates(v,t1,t2,dt):
    return [
        (t,average_flow_rate(v,t,t+dt))
        for t in np.arange(t1,t2,dt)
    ]
def plot_interval_flow_rates(volume,t1,t2,dt):
    series = interval_flow_rates(volume,t1,t2,dt)
    times = [t for (t,_) in series]
    rates = [q for (_,q) in series]
    plt.scatter(times,rates)
#df/dx
def instantaneour_flow_rate(v,t,digits=6):
    tolerance=10**(-digits)
    h=1
    approx=average_flow_rate(v,t-h,t+h)
    for i in range(0,2*digits):
        h=h/10
        next_approx=average_flow_rate(v,t-h,t+h)
        if abs(next_approx-approx)<tolerance:
            return round(next_approx,digits)
        else:
            approx=next_approx
    raise Exception("Derivative did not converge")
def get_flow_rate_function(v):
    def flow_rate_function(t):
        return instantaneour_flow_rate(v,t)
    return flow_rate_function
def small_volume_change(q,t,dt):
    return q(t)*dt
def volume_change(q,t1,t2,dt):
    return sum(small_volume_change(q,t,dt) 
               for t in np.arange(t1,t2,dt))
def approximate_volume(q,v0,dt,T):
    return v0+volume_change(q,0,T,dt)
def approximate_volume_function(q,v0,dt):
    def function(T):
        return approximate_volume(q,v0,dt,T)
    return function


def get_volume_function(q,v0,digits=6):
    def volume_function(T):
        tolerance=10**(-digits)
        dt=1
        approx=v0+volume_change(q,0,T,dt)
        for i in range(0,digits*2):
            dt=dt/10
            next_approx=v0+volume_change(q,0,T,dt)
            if(abs(next_approx-approx)<tolerance):
                return round(next_approx,digits)
            else:
                approx =next_approx
        raise Exception("Did not converge")
    return volume_function
print(get_volume_function(flow_rate,2.3,digits=6)(1))





