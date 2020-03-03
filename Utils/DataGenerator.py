'''
Created on 3 Mar 2020

@author: w.delamare
'''


import random
import numpy as np

from Utils import Config as c



def InitDragCoef():
    return random.choice(c.DRAGS) + random.random() / c.DRAG_FACTOR

def InitLiftCoef():
    return random.choice(c.LIFTS) + random.random() / c.LIFT_FACTOR

def InitSurface():
    return random.choice(c.WING_AREA) + random.random() * c.WING_FACTOR



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


# def GetAirSpeed(nb_data):
#     vec = np.array([random.random(), random.random(), random.random()])
#     vec_n = vec / np.linalg.norm(vec)
#     return vec_n * 100.0

def GetAirSpeed(HInM):
    pass

def LbsToKg(val):
    return val * 0.453592

def KgToLbs(val):
    return val * 2.20462

def FtToM(val):
    return val * 0.3048

def MToFt(val):
    return val * 3.28084