'''
Created on 3 Mar 2020

@author: w.delamare
'''


import random
import math
import numpy as np

from Utils import Config as c
from math import radians


###############################
#             INIT
#
# (used by config for dictionaries)
###############################
def InitDragCoef():
    return random.choice(c.DRAGS) + random.random() * c.DRAG_FACTOR

def InitLiftCoef():
    return random.choice(c.LIFTS) + random.random() * c.LIFT_FACTOR

def InitSurface():
    return random.choice(c.WING_AREA) + random.random() * c.WING_FACTOR



###############################
#             GETTERS
#
# (used by dicos)
###############################
def GetMotor(aircraft):
    return c.dico_aircrafts[aircraft]['motor']
    #return random.choice(c.MOTOR_RANGE)

def GetDragCoef(aircraft):
    return c.dico_aircrafts[aircraft]['drag_coef']

def GetLiftCoef(aircraft):
    return c.dico_aircrafts[aircraft]['lift_coef']

def GetMass(aircraft):
    return c.dico_aircrafts[aircraft]['mass']
    #return random.choice(c.MASS) + random.random() * c.MASS_FACTOR

def GetMassFuel(aircraft):
    return c.dico_aircrafts[aircraft]['fuel']

def GetSurface(aircraft):
    return c.dico_aircrafts[aircraft]['surface']



###############################
#       CONVERT
###############################

def LbsToKg(val):
    return val * 0.453592

def KgToLbs(val):
    return val * 2.20462

def FtToM(val):
    return val * 0.3048

def MToFt(val):
    return val * 3.28084

def KnotsToKMH(val):
    return val * 1.852

def KMHToKnots(val):
    return val * 0.539957

def KMHToMS(val):
    return val / 3.6

def MSToKMH(val):
    return val * 3.6

def DegToRad(val):
    return val * 0.0174533

def MToKFT(val):
    return val / 304.8

def DegToK(deg):
    return deg + 273.15

def M2ToFt2(m2):
    return m2 * 10.764

def MSToMPH(ms):
    return ms * 2.237

def WToHP(w):
    return w / 746

def PatoPSI(pa):
    return pa / 6895


def GetSpeed(dico):
    '''
    http://www.movable-type.co.uk/scripts/latlong.html
    and
    https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points 
    phi = latitude
    lambda = longitude
    '''
    res = []

    for ind in range(1, len(dico['longitude'])):
        phi1, lambda1, time1 = dico['latitude'][ind-1], dico['longitude'][ind-1], dico['timestamp'][ind-1]
        phi2, lambda2, time2 = dico['latitude'][ind], dico['longitude'][ind], dico['timestamp'][ind]
        phi1 = radians(phi1)
        phi2 = radians(phi2)
        lambda1 = radians(lambda1)
        lambda2 = radians(lambda2)
        dphi = phi2 - phi1
        dlambda = lambda2 - lambda1
        
        a = math.sin(dphi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0)**2
        cc = 2 * math.asin(math.sqrt(a))#2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        # finally the distance
        d = (c.EARTH_RADIUS + dico['altitude'][ind]) * cc
        # m / s
        speed = d / (time2 - time1)
        res.append(speed)
        # km / h
        # res.append(speed * 3600.0 / 1000.0)
    
    # artificial first point to keep the same length as other metrics
    res = [res[0]] + res
    return res



def GetSpeedUV(dico):
    res = []
    dx, dy, dz = np.diff(dico['u']), np.diff(dico['v']), np.diff(dico['altitude'])
    dt = np.diff(dico['timestamp'])
    vx, vy, vz = dx / dt, dy / dt, dz / dt
    
    vx = np.concatenate(([vx[0]], vx), axis=0)
    vy = np.concatenate(([vy[0]], vy), axis=0)
    vz = np.concatenate(([vz[0]], vz), axis=0)
    
    res = np.sqrt(vx*vx + vy*vy + vz*vz)
    #res = np.concatenate(([res[0]], res), axis=0)
    return vx, vy, vz, res


def GetAirSpeed(dico):
    altitude_m = dico['altitude']
    resx, resy, resz = [], [], []
    res = []
    wind = c.current_air_speed
    for a, sx, sy, sz in zip(altitude_m, dico['vx'], dico['vy'], dico['vz']):
        positions = np.where(a >= c.AIR_LEVELS)
        # get the last one of the first array result
        pos = positions[0][len(positions[0])-1]
        # wind values
        w_speed = KnotsToKMH(np.array(wind['speed'][pos]))
        # change to m / s for SI computations in the next function(s)
        w_speed = KMHToMS(w_speed)
        w_dir = np.array([math.cos(DegToRad(wind['direction'][pos])), math.sin(DegToRad(wind['direction'][pos])), 0])
        # compute
        s = np.array([sx, sy, sz])
        air_speed = np.array(s + w_speed * w_dir)
        # store
        resx.append(air_speed[0])
        resy.append(air_speed[1])
        resz.append(air_speed[2])
        res.append(np.linalg.norm(air_speed))
    
    # km / h
    return resx, resy, resz, np.array(res)






# kW 
# hp
def GetEnginePower(names, dico, meta):
    '''
    *************** Weight: 
    W = m (mass) * g (local acceleration in free fall)
    -- g = 9.81
    
    
    *************** Drag: https://en.wikipedia.org/wiki/Drag_equation
    D = 0.5 * Ro (air density) * V^2 (speed relative to the fluid) * A (area) * Cd (drag coefficient)
    
    
    *************** Lift: https://en.wikipedia.org/wiki/Lift_(force)
    L = 0.5 * Ro (air density) * V^2 (true air speed) * S (wing area) * Cl (lift coefficient)
    
    
    *************** Ro: https://en.wikipedia.org/wiki/Density_of_air#Troposphere
    Ro = (p0 * M / R * T0) * (1- L * h / T0) ^ (g * M / (R * L) - 1)
    -- p0 = sea level standard atmospheric pressure, 101325 Pa
    -- T0 =  sea level standard temperature, 288.15 K
    -- g =  earth-surface gravitational acceleration, 9.80665 m/s2
    -- L =  temperature lapse rate, 0.0065 K/m
    -- R = ideal (universal) gas constant, 8.31447 J/(mol-K)
    -- M = molar mass of dry air, 0.0289654 kg/mol
    
    
    ==> Engine Power Ep
    
    Force: Ep = m * a - W - D - L
    Power = Ep * V

    '''
    
    speed = np.array(dico['speed'])
    accel = np.diff(speed) / np.diff(dico['timestamp'], n=1)
    accel = np.concatenate(([accel[0]], accel), axis=0)
    
    speed = np.array([0])
    
    W = (meta['mass_kg']+meta['mass_fuel_kg']) * c.g
    Ro = (c.p0 * c.M / (c.R * c.T0)) * pow((1 - c.L * dico['altitude'] / c.T0), (c.g * c.M / (c.R * c.L) - 1))
    #Ro = tmp1 * tmp2
    D = 0.5 * Ro * (speed+dico['air_speed']) * (speed+dico['air_speed']) * meta['surface_m2'] * meta['drag_coef']
    L = 0.5 * Ro * (speed+dico['air_speed']) * (speed+dico['air_speed']) * meta['surface_m2'] * meta['lift_coef']
    T = (meta['mass_kg']+meta['mass_fuel_kg']) * accel - W - D - L
    
    for i in range(0, meta['nb_motor']):
        names.append("engine" + str(i))
        dico['engine' + str(i)] = np.array(T * dico['air_speed']) / meta['nb_motor']
    
    return names, dico




def GetEnginePower2(names, dico, meta):
    '''
        Compute vector-wise power from thrust forces
    '''
    engines = []
    
    vx, vy, vz = np.array(dico['vx']), np.array(dico['vy']), np.array(dico['vz'])
    air_x, air_y, air_z = np.array(dico['air_x']), np.array(dico['air_y']), np.array(dico['air_z'])
    
    ax = np.diff(vx) / np.diff(dico['timestamp'], n=1), 
    ay = np.diff(vy) / np.diff(dico['timestamp'], n=1)
    az = np.diff(vz) / np.diff(dico['timestamp'], n=1)
    
    # WTF ??
    ax = np.concatenate(([ax[0][0]], ax[0]), axis=0)
    # ok
    ay = np.concatenate(([ay[0]], ay), axis=0)
    az = np.concatenate(([az[0]], az), axis=0)
    
    # WEIGHT
    Wx = 0
    Wy = 0
    Wz = (meta['mass_kg']+meta['mass_fuel_kg']) * c.g
    
    # AIR DENSITY
    Ro = (c.p0 * c.M / (c.R * c.T0)) * pow((1 - c.L * dico['altitude'] / c.T0), (c.g * c.M / (c.R * c.L) - 1))
    
    
    vx, vy, vz = np.array([0]),np.array([0]),np.array([0])
#     air_x, air_y, air_z = np.array([0]),np.array([0]),np.array([0])
    
    # DRAG
    Dx = 0.5 * Ro * (vx+air_x) * (vx+air_x) * meta['surface_m2'] * meta['drag_coef']
    Dy = 0.5 * Ro * (vy+air_y) * (vy+air_y) * meta['surface_m2'] * meta['drag_coef']
    Dz = 0.5 * Ro * (vz+air_z) * (vz+air_z) * meta['surface_m2'] * meta['drag_coef']
    
    # LIFT
    Lx = 0.5 * Ro * (vx+air_x) * (vx+air_x) * meta['surface_m2'] * meta['lift_coef']
    Ly = 0.5 * Ro * (vy+air_y) * (vy+air_y) * meta['surface_m2'] * meta['lift_coef']
    Lz = 0.5 * Ro * (vz+air_z) * (vz+air_z) * meta['surface_m2'] * meta['lift_coef']
    
    # THRUST
    Tx = (meta['mass_kg']+meta['mass_fuel_kg']) * ax - Wx - Dx - Lx
    Ty = (meta['mass_kg']+meta['mass_fuel_kg']) * ay - Wy - Dy - Ly
    Tz = (meta['mass_kg']+meta['mass_fuel_kg']) * az - Wz - Dz - Lz
    
    for i in range(0, meta['nb_motor']):
        names.append("engine_" + str(i))
        engines.append("engine_" + str(i))
        Px = smooth(Tx * (vx+air_x), 10, "bartlett")
        Py = smooth(Ty * (vy+air_y), 10, "bartlett")
        Pz = smooth(Tz * (vz+air_z), 10, "bartlett")
        val = np.sqrt(Px*Px + Py*Py + Pz*Pz)
        dico['engine_' + str(i)] = np.array(val) / meta['nb_motor']
    
    return engines, names, dico



# https://en.wikipedia.org/wiki/Barometric_formula


# kW 
# hp
def GetEnginePower3(names, dico, meta):
    
    speed = np.array(dico['speed'])
    accel = np.diff(speed[1:]) / np.diff(dico['timestamp'], n=2)
    accel = np.concatenate(([accel[0], accel[0]], accel), axis=0)
    speed = np.array([0])
    W = meta['mass_kg'] * c.g
    Ro = 1.2250  * np.exp(-c.g * c.M * (dico['altitude']-11000)/ (c.R * 288.15 ))
    #Ro = tmp1 * tmp2
    D = 0.5 * Ro * (speed+dico['air_speed']) * (speed+dico['air_speed']) * meta['surface_m2'] * meta['drag_coef']
    L = 0.5 * Ro * (speed+dico['air_speed']) * (speed+dico['air_speed']) * meta['surface_m2'] * meta['lift_coef']
    T = meta['mass_kg'] * accel - W - D - L
    print(np.average(dico['altitude']))
    for i in range(0, meta['nb_motor']):
        names.append("engine" + str(i))
        dico['engine' + str(i)] = np.array(T * dico['speed']) / meta['nb_motor']
    
    return names, dico





def GetTemperatureCockpit(dico, col = "temperature_in"):
    '''
    degree
    '''
    dico[col] = smooth(np.array([c.T_COCKPIT + random.uniform(-c.T_NOISE, c.T_NOISE) for x in range(0, len(dico['longitude']))]), 10, "flat")
    return dico
    


def GetPressureCockpit(dico, col = "pressure_in"):
    '''
    Pa
    '''
    dico[col] = smooth(np.array([c.PRESSURE + random.uniform(-c.PRESSURE_NOISE, c.PRESSURE_NOISE) for x in range(0, len(dico['longitude']))]), 10, "flat")
    return dico


def GetHeartRate(dico, col = "heart_rate"):
    '''
    BPM
    '''
    dico[col] = smooth(np.array([c.BPM + random.uniform(-c.BPM_NOISE, c.BPM_NOISE) for x in range(0, len(dico['longitude']))]), 10, "flat")
    return dico



def GetHumidityCockpit(dico, col = "humidity_in"):
    '''
    %
    '''
    dico[col] = smooth(np.array([c.HUMIDITY + random.uniform(-c.HUMIDITY_NOISE, c.HUMIDITY_NOISE) for x in range(0, len(dico['longitude']))]), 10, "flat")
    return dico



def GetOxygenMask(dico, col = "oxygen_mask"):
    '''
    %
    '''
    alt = MToKFT(dico['altitude'])
    dico[col] = smooth(c.OXYGEN_A + c.OXYGEN_B * alt + random.uniform(-c.OXYGEN_NOISE, c.OXYGEN_NOISE), 10, "flat")
    dico[col][dico[col] > 100] = 100 - random.random()
    return dico





def smooth(x,window_len=11,window='hanning'):
    """smooth the data using a window with requested size.
    
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.
    
    input:
        x: the input signal 
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal
        
    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)
    
    see also: 
    
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter
 
    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise(ValueError, "smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise(ValueError, "Input vector needs to be bigger than window size.")


    if window_len<3:
        return x


    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise(ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")


    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    return y
