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
import struct



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
    return dg.DegToK(deg)
def GetRUTemp(deg):
    return deg

def GetUSSurface(m2):
    return dg.M2ToFt2(m2)
def GetRUSurface(m2):
    return m2
    
def GetUSPercentage(P):
    return P / 100
def GetRUPercentage(P):
    return P

def GetUSSpeed(ms):
    return dg.MSToMPH(ms)
def GetRUSpeed(ms):
    return ms

def GetUSPower(w):
    return dg.WToHP(w)
def GetRUPower(w):
    return w

def GetUSPressure(pa):
    return dg.PatoPSI(pa)
def GetRUPressure(pa):
    return pa

GetDate = None
GetMass = None
GetDistance = None
GetTemp = None
GetSurface = None
GetPercentage = None
GetSpeed = None
GetPower = None
GetPressure = None




def LogDico(f, names, dico):
    '''
        Once everything is ready, call this function to automatically log everything in dico according to name in f
        f: the file (already opened for writing)
        names: array with header column names
        dico: dic of arrays (all the same length)
    '''
    
    s = ""
    # header line
    if c.CURRENT_CONDITION[0] != c.MISSING_COLNAMES[0]:
        for n in names:
            s += n + ","
        s = s[0:len(s)-1] + "\n"
    
    # values
    the_range = range(0, len(dico[names[0]]))
    
    if c.CURRENT_CONDITION[0] == c.ONE_LINE[0]:
        the_range = random.sample(the_range, 1)
    elif c.CURRENT_CONDITION[0] == c.TWO_LINES[0]:
        the_range = random.sample(the_range, 2)
    elif c.CURRENT_CONDITION[0] == c.THREE_LINES[0]:
        the_range = random.sample(the_range, 3)
    elif c.CURRENT_CONDITION[0] == c.REVERSE[0]:
        the_range = range(len(dico[names[0]])-1, -1, -1)
        
    for i in the_range:
        for n in names:
            s += str(dico[n][i]) + ","
        s = s[0:len(s)-1] + "\n"
        
    if c.CURRENT_CONDITION[0] == c.ASCII[0]:
        s = s.replace(".", "⋅")

    if c.CURRENT_CONDITION[0] == c.CORRUPTED_BINARY[0]:
        # f.write(struct.pack(str(len(s)) + "B", *s))
        s = s.replace("\n", "\r")
        return
    
    
    
    f.write(s)
  
  
  


def GetHeader(f_id, f_name, start_tstp, meta):
    '''
        Take care of writing the header part
        Return a string (the header)
    '''
    
    res = ""
    
    start_city = random.choice(c.CITIES)
    tmp = list(c.CITIES)
    tmp.remove(start_city)
    stop_city = random.choice(tmp)
    travel_date = start_tstp.strftime("%Y-%m-%d")
    
    
    
    res += "flight id:" + f_id
    res += "\n" + "flight code:" + f_name
    res += "\n" + "origin:" + str(meta['origin'])
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
    '''
        Parse the ACMI file values and take care of missing date
        Create also the timestamp column according to the start_tstp previously parsed
    '''
    
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






        
        
        
        

def GenerateFile(f_id, f_name, records, start_tstp):
    
    f_type = "US"
    if f_name in c.US_AIRCRAFTS:
        f_type = "US"
        GetDate = GetUSDate
        GetMass = GetUSMass
        GetDistance = GetUSDistance
        GetTemp = GetUSTemp
        GetSurface = GetUSSurface
        GetPercentage = GetUSPercentage
        GetSpeed = GetUSSpeed
        GetPower = GetUSPower
        GetPressure = GetUSPressure
    else:
        f_type = "RU"
        GetDate = GetRUDate
        GetMass = GetRUMass
        GetDistance = GetRUDistance
        GetTemp = GetRUTemp
        GetSurface = GetRUSurface
        GetPercentage = GetRUPercentage
        GetSpeed = GetRUSpeed
        GetPower = GetRUPower
        GetPressure = GetRUPressure
     
    if not os.path.exists(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION[1] + "\\" + f_type):
        os.mkdir(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION[1] + "\\" + f_type)
    
       
    ## Header
    meta = {}
    meta['origin'] = f_type
    meta['nb_motor'] = dg.GetMotor(f_name)
    meta["drag_coef"] = dg.GetDragCoef(f_name)
    meta["lift_coef"] = dg.GetLiftCoef(f_name)
    meta["mass"] = GetMass(dg.GetMass(f_name))          # from lbs
    meta["mass fuel"] = GetMass(dg.GetMassFuel(f_name)) # from lbs
    meta['surface'] = GetSurface(dg.GetSurface(f_name)) # from m2
    # for computations only
    meta["mass_kg"] = dg.LbsToKg(dg.GetMass(f_name))
    meta["mass_fuel_kg"] = dg.LbsToKg(dg.GetMassFuel(f_name))
    meta["surface_m2"] = dg.GetSurface(f_name)
    
        
    
    
    ## Values
    #        [degree,     degree,     m,          degree,    degree, deg, m,    m,  degree]
    names = ["longitude", "latitude", "altitude", "roll", "pitch", "yaw", "u", "v", "heading"]
    dico = GetDico(records, names, f_id, start_tstp)
    
    # get speed
    # m / s
    #names.append("speed_uv")
    dico['vx'], dico['vy'], dico['vz'], dico['speed_uv'] = dg.GetSpeedUV(dico)
    
    # generate air speed 
    # m / s
    names.append("air_speed")
    dico['air_x'], dico['air_y'], dico['air_z'], dico['air_speed'] = dg.GetAirSpeed(dico)

    # then compute engine(s) power
    # W
    engines, names, dico = dg.GetEnginePower2(names, dico, meta)
    
    
    # COCKPIT
    
    # celsius
    col = "temperature_in"
    names.append(col)
    dico = dg.GetTemperatureCockpit(dico, col)

    # % (e.g., 70)
    col = "humidity_in"
    names.append(col)
    dico = dg.GetHumidityCockpit(dico, col)
    
    # Pa
    col = "pressure_in"
    names.append(col)
    dico = dg.GetPressureCockpit(dico, col)
    
    # BPM
    col = "heart_rate"
    names.append(col)
    dico = dg.GetHeartRate(dico, col)
    
    # % (e.g., 70)
    col = "oxygen_mask"
    names.append(col)
    dico = dg.GetOxygenMask(dico, col)
    
    
    ## convert values if necessary
    ## use agnostic function (so check them again!)
    dico['altitude'] = GetDistance(dico['altitude'])
    dico['u'] = GetDistance(dico['u'])
    dico['v'] = GetDistance(dico['v'])
    
    dico['air_speed'] = GetSpeed(dico['air_speed'])
    for e in engines:
        dico[e] = GetPower(dico[e])
    
    dico['temperature_in'] = GetTemp(dico['temperature_in'])
    dico['humidity_in'] = GetPercentage(dico['humidity_in'])
    dico['pressure_in'] = GetPressure(dico['pressure_in'])
    dico['oxygen_mask'] = GetPercentage(dico['oxygen_mask'])
    
    
    
    names.insert(0, "timestamp")
    
    f = None 
    head = GetHeader(f_id, f_name, start_tstp, meta)
    
    if c.CURRENT_CONDITION[0] == c.NORMAL[0]:
        f = open(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION[1] + "\\" + f_type + "\\" + str(c.num_condition) + "_" + f_id + "_" + f_name + ".csv", "w+")
        f.write(head)
        LogDico(f, names, dico)
        f.close()
        return
    
    elif c.CURRENT_CONDITION[0] == c.MISSING_HEADER[0]:
        f = open(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION[1] + "\\" + f_type + "\\" + str(c.num_condition) + "_" + f_id + "_" + f_name + ".csv", "w+")
        #f.write(head)
        LogDico(f, names, dico)
        f.close()
        return
    
    elif c.CURRENT_CONDITION[0] == c.INCOMPLETE_HEADER[0]:
        tab = head.split('\n')
        for cur in range(0, len(tab)):
            t2 = [x for i,x in enumerate(tab) if i != cur]
            s = "\n".join(t2)
            f = open(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION[1] + "\\" + f_type + "\\" + str(c.num_condition) + "_" + str(cur) + f_id + "_" + f_name + ".csv", "w+")
            f.write(head)
            LogDico(f, names, dico)
            f.close()
        return

    elif c.CURRENT_CONDITION[0] == c.MISSING_COLUMN[0]:
        for removed in range(0, len(names)):
            print(str(removed) + " / " + str(len(names)))
            names2 = list(names)
            names2.pop(removed)
            dico2 = {}
            for cur in names2:
                dico2[cur] = dico[cur]
            f = open(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION[1] + "\\" + f_type + "\\" + str(c.num_condition) + "_" + str(removed) + f_id + "_" + f_name + ".csv", "w+")
            f.write(head)
            LogDico(f, names2, dico2)
            f.close()
        return

    else:
        f = open(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION[1] + "\\" + f_type + "\\" + str(c.num_condition) + "_" + f_id + "_" + f_name + ".csv", "w+", encoding='utf-8')
        f.write(head)
        LogDico(f, names, dico)
        f.close()
        return

  