'''
Created on 2 Mar 2020

@author: w.delamare
'''

import os
import random
from datetime import datetime

from Utils import Regexp as r
from _datetime import timedelta



## CONFIG ##

_PATH_RESOURCES = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
acmi_file = "..\\Samples\\Tacview-20191108-113901-DCS-MOHICAN_AI_final.txt.acmi"
#acmi_file = "..\\Samples\\test.acmi"
res_folder = "..\\TestFiles"


motor_range = (1, 2, 4)
cities = ["Paris", "London", "Tokyo", "Boston", "Madrid", "Biarritz"]
# asked google
drags = [x*0.01 for x in range(5, 45, 1)]
# https://aviation.stackexchange.com/questions/46518/what-is-the-typical-value-of-maximum-lift-coefficient-for-aerobatic-aircraft
lifts = [x * 0.1 for x in range(10, 20, 1)]


flight_type = "Boeing"

#######




''' FORMULAE

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

Ep = m * a - W - D - L


''' 


def GetHeader(f_id, f_name, start_tstp):
    res = ""
    
    nb_motor = str(random.choice(motor_range))
    start_city = random.choice(cities)
    tmp = list(cities)
    tmp.remove(start_city)
    stop_city = random.choice(tmp)
    travel_date = start_tstp.strftime("%Y-%m-%d")
    
    drag = random.choice(drags) + random.random() / 10.0
    lift = random.choice(lifts) + random.random() / 4.0
    
    res += "flight id:" + f_id
    res += "\n" + "flight code:" + f_name
    res += "\n" + "flight type:" + flight_type
    res += "\n" + "date:" + travel_date
    res += "\n" + "from:" + start_city
    res += "\n" + "to:" + stop_city
    res += "\n" + "motor(s):" + nb_motor
    
    res += "\n" + "lift coef:" + str(lift)
    res += "\n" + "drag coef:" + str(drag)
    
    res += "\n\n"

    return res





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
    

def GenerateFile(f_id, f_name, records, start_tstp):
    f = open(_PATH_RESOURCES + "\\" + res_folder + "\\" + flight_type + "\\" + f_id + "_" + f_name + ".csv", "w+")
    head = GetHeader(f_id, f_name, start_tstp)
    f.write(head)
    
    longitudes = []
    latitudes = []
    altitudes = []
    roll = []
    pitch = []
    yaw = []
    us = []
    vs = []
    headings = []
    dico = {}
    dico['timestamp'] = []
    names = ["longitude", "latitude", "altitude", "roll", "pitch", "yaw", "u", "v", "heading"]
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
         
    
    LogDico(f, names, dico)
    
    
    f.close()

    


if __name__ == '__main__':
    f = open(_PATH_RESOURCES + "\\" + acmi_file)
    s = f.read()
    flights = r.GetFlightsIDs(s)
    start_tstp = datetime.strptime(r.GetInitialTimestamp(s[0:500]), '%Y-%m-%dT%H:%M:%SZ')
    f.close()
    
    if not os.path.exists(_PATH_RESOURCES + "\\" + res_folder):
        os.mkdir(_PATH_RESOURCES + "\\" + res_folder)
        
    if not os.path.exists(_PATH_RESOURCES + "\\" + res_folder + "\\" + flight_type):
        os.mkdir(_PATH_RESOURCES + "\\" + res_folder + "\\" + flight_type)
    
    records = r.GetRecords(s)
    
    for f_id, f_name in flights:
        GenerateFile(f_id, f_name, records, start_tstp)
        pass