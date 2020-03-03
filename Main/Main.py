'''
Created on 2 Mar 2020

@author: w.delamare
'''

import os
import sys

from datetime import datetime



PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
os.chdir(SCRIPT_DIR)



from Utils import Regexp as r
from Utils import Config as c
from Utils import FileGenerator as fg






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


  


if __name__ == '__main__':
    
    ## out folders
    if not os.path.exists(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER):
        os.mkdir(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER)
        
    if not os.path.exists(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION):
        os.mkdir(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION)
    
    
    ## parse acmi file
    f = open(c.PATH_RESOURCES + "\\" + c.ACMI_FILE)
    s = f.read()
    flights = r.GetFlightsIDs(s)
    start_tstp = datetime.strptime(r.GetInitialTimestamp(s[0:500]), '%Y-%m-%dT%H:%M:%SZ')
    f.close()
    
    c.InitDicoAircrafts()
    ## process every records
    records = r.GetRecords(s)
    for f_id, f_name in flights:
        f_name = f_name.split(" ")[0]
        print("creating file for " + f_id + "_" + f_name)
        fg.GenerateFile(f_id, f_name, records, start_tstp)
        pass