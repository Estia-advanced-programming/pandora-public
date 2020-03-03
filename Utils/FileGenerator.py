'''
Created on 3 Mar 2020

@author: w.delamare
'''

import os
import random
import numpy as np
from _datetime import timedelta

from Utils import Config as c
from Utils import Regexp as r
from Utils import DataGenerator as dg



def GetUSDate(tstp):
    return tstp.strftime("%Y-%m-%d")
def GetRUDate(tstp):
    return tstp.strftime("%d-%m-%Y")

def GetUSMass(lbs):
    return lbs
def GetRUMass(lbs):
    return dg.LbsToKg(lbs)

def GetUSDistance(m):
    return dg.MToFt(m)
def GetRUDistance(m):
    return m

def GetUSTemp(deg):
    return deg + 273.15
def GetRUTemp(deg):
    return deg

def GetUSSurface(mm):
    return mm / 0.092903
def GetRUSurface(mm):
    return mm
    
GetDate = None
GetMass = None
GetDistance = None
GetTemp = None
GetSurface = None





def LogDico(f, names, dico):
    s = ""
    names.insert(0, "timestamp")
    # header line
    for n in names:
        s += n + ","
    s = s[0:len(s)-1] + "\n"
    
    # values
    for i in range(0, len(dico[names[0]])):
        for n in names:
            s += str(dico[n][i]) + ","
        s = s[0:len(s)-1] + "\n"
    f.write(s)
  
  
  


def GetHeader(f_id, f_name, start_tstp, meta):
    res = ""
    
    start_city = random.choice(c.CITIES)
    tmp = list(c.CITIES)
    tmp.remove(start_city)
    stop_city = random.choice(tmp)
    travel_date = start_tstp.strftime("%Y-%m-%d")
    
    
    res += "flight id:" + f_id
    res += "\n" + "flight code:" + f_name
    #res += "\n" + "company:" + c.COMPANY
    res += "\n" + "date:" + travel_date
    res += "\n" + "from:" + start_city
    res += "\n" + "to:" + stop_city
    res += "\n" + "motor(s):" + str(meta["nb_motor"])
    res += "\n" + "mass aircraft:" + str(meta['mass'])
    res += "\n" + "mass fuel:" + str(meta['mass'])
    
    res += "\n" + "lift coef:" + str(meta["lift_coef"])
    res += "\n" + "drag coef:" + str(meta["drag_coef"])
    
    res += "\n\n"

    return res




def GetDico(records, names, f_id, start_tstp):
    dico = {}
    dico['timestamp'] = []
    for n in names:
        dico[n] = []
        
    prev_values = [-1 for x in range(0, 10)]
    for rec in records:
        values = r.GetValues(rec, f_id)
        
        if values is not None:
            
            tdelta = timedelta(seconds = float(r.GetTstp(rec)))
            timestp = (start_tstp + tdelta).timestamp()
            dico['timestamp'].append(timestp)
            
            
            values = list(values)
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = prev_values[i]
            prev_values = values
            # log them
            # ...
            
            # save them
            for i in range(0, len(names)):
                dico[names[i]].append(values[i])
            
        else:
            continue
    
    for n in names:
        dico[n] = np.array(dico[n]).astype(float)
    
    return dico






def GetEnginePower(names, dico, meta):
    
    
    dx = np.diff(dico['longitude']) / np.diff(dico['timestamp'])
    dy = np.diff(dico['latitude']) / np.diff(dico['timestamp'])
    dz = np.diff(dico['altitude']) / np.diff(dico['timestamp'])
    speed = np.sqrt(dx**2 + dy**2 + dz**2)
    accel = np.diff(speed) / np.diff(np.diff(dico['timestamp']))
    
    W = meta['mass'] * c.g
    Ro = (c.p0 * c.M / c.R * c.T0) * (1- c.L * dico['altitude'] / c.T0) ^ (c.g * c.M / (c.R * c.L) - 1)
    D = 0.5 * Ro * (speed+dico['air_speed']) * (speed+dico['air_speed']) * meta['surface'] * meta['drag']
    L = 0.5 * Ro * (speed+dico['air_speed']) * (speed+dico['air_speed']) * meta['surface'] * meta['lift']
    T = meta['mass'] * accel - W - D - L
    for i in range(0, meta['nb_motor']):
        names.append("engine" + str(i))
        dico['engine' + str(i)] = []
        
        
        
        

def GenerateFile(f_id, f_name, records, start_tstp):
    
    f_type = "US"
    if f_name in c.US_AIRCRAFTS:
        f_type = "US"
        GetDate = GetUSDate
        GetMass = GetUSMass
        GetDistance = GetUSDistance
        GetTemp = GetUSTemp
        GetSurface = GetUSSurface
    else:
        f_type = "RU"
        GetDate = GetRUDate
        GetMass = GetRUMass
        GetDistance = GetRUDistance
        GetTemp = GetRUTemp
        GetSurface = GetRUSurface
     
    if not os.path.exists(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION + "\\" + f_type):
        os.mkdir(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION + "\\" + f_type)
    
       
    ## Header
    meta = {}
    meta['nb_motor'] = dg.GetMotor(f_name)
    meta["drag_coef"] = dg.GetDragCoef(f_name)
    meta["lift_coef"] = dg.GetLiftCoef(f_name)
    meta["mass"] = GetMass(dg.GetMass(f_name))
    meta["mass fuel"] = GetMass(dg.GetMassFuel(f_name))
    meta['surface'] = GetSurface(dg.GetSurface(f_name))
    
    
        
    
    f = open(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION + "\\" + f_type + "\\" + f_id + "_" + f_name + ".csv", "w+")
    head = GetHeader(f_id, f_name, start_tstp, meta)
    f.write(head)
    
    
    ## Values
    names = ["longitude", "latitude", "altitude", "roll", "pitch", "yaw", "u", "v", "heading"]
    dico = GetDico(records, names, f_id, start_tstp)
    
    # generate air speed
    dico['air_speed'] = np.array([1 for x in dico['timestamp']])
    # then compute engine(s) power
    #names, dico = GetEnginePower(names, dico, meta)
    
    ## convert values if necessary
    # longitude: degree
    # latitude: degree
    # altitude: m
    # roll: degree
    # pitch: degree
    # yaw: degree
    # u: m
    # v: m
    # heading: degree
    dico['altitude'] = GetDistance(dico['altitude'])
    dico['u'] = GetDistance(dico['u'])
    dico['v'] = GetDistance(dico['v'])
    # mass: lbs
    # mass fuel: lbs
    # date: 
    
    LogDico(f, names, dico)
    
    
    f.close()

  