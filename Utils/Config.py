'''
Created on 3 Mar 2020
    
    All hard-coded values 
    
@author: w.delamare
'''

import os

from Utils import DataGenerator as dg



############################################
# FILES AND DIRECTORIES
############################################

# where is the script being run
PATH_RESOURCES = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# the acmi file to parse
ACMI_FILE = "..\\Samples\\10_normal_flights.txt.acmi"
# ACMI_FILE = "..\\Samples\\10_meteo_bad__flights.txt.acmi"

# the folder in which writing the resulting test files
OUT_FOLDER = "..\\TestFiles"

# sub folder (NORMAL, MISSING_COL, etc)
NORMAL = [0, "Normal"]
BAD_WEATHER = [1,"Bad_Weather"]
MISSING_COLUMN = [2, "Missing_Column"]
MISSING_HEADER = [3, "Missing_Header"]
INCOMPLETE_HEADER = [4, "Incomplete_Header"]
MISSING_COLNAMES = [5, "Missing_Colnames"]
ONE_LINE = [6, "One_Line"]
TWO_LINES = [7, "Two_Lines"]
THREE_LINES = [8, "Three_Lines"]
REVERSE = [9, "Reverse"]
BIG_INT = [10, "Big_Int"]
ASCII = [11, "Ascii"]
CORRUPTED_BINARY = [12, 'Corrupted_Binary']

CURRENT_CONDITION = CORRUPTED_BINARY
num_condition = CURRENT_CONDITION[0]



US_AIRCRAFTS = ["F-14B", "F-14A", "F-15C", "F-15E", "F-16A"]



############################################
# FORMULAE CONSTANTS
############################################

g = 9.81
p0 = 101325
T0 = 288.15
L = -0.0065
R = 8.31447
M = 0.0289654





############################################
# GENERATED DATA VALUES
############################################


# asked google
DRAGS = [x*0.01 for x in range(1, 2, 1)]
DRAG_FACTOR = 0.01

# https://aviation.stackexchange.com/questions/46518/what-is-the-typical-value-of-maximum-lift-coefficient-for-aerobatic-aircraft
LIFTS = [x * 0.1 for x in range(10, 20, 1)]
LIFT_FACTOR = 0.4

# kg
MASS = [x for x in range(10000, 20000, 500)]
MASS_FACTOR = 1000 

# https://en.wikipedia.org/wiki/Wing_loading
# same for drag (asked Philippe)
# m^2
WING_AREA = [x for x in range(20, 25, 1)]
WING_FACTOR = 1

# m
AIR_LEVELS = [dg.FtToM(x) for x in [-1000, 1600, 6600, 26000]]

# m
EARTH_RADIUS = 6371 * 1000

# C
T_COCKPIT = 25
# https://www.researchgate.net/publication/276074552_Simulation_for_temperature_control_of_a_military_aircraft_cockpit_to_avoid_pilot%27s_thermal_stress
# > +10 deg (sometimes > +45 deg) compared to ambient temp.
T_NOISE = 15
T_EVENT = +20


# https://www.google.com/search?client=firefox-b-d&q=heart+rate+data+bpm+fighter+jet+pilot
BPM = 90
BPM_NOISE = 20
BPM_EVENT = +40


# http://www.diva-portal.org/smash/get/diva2:1082610/FULLTEXT01.pdf
PRESSURE = 25000
PRESSURE_NOISE = 5000
PRESSURE_EVENT = -10000
 

# https://www.ncbi.nlm.nih.gov/books/NBK234096/
# relative humidity in %
HUMIDITY = 7.5
HUMIDITY_NOISE = 2


# http://www.iosrjournals.org/iosr-jmce/papers/ICRTEM/ME/Volume-7/MECH-25.pdf?id=7622
OXYGEN_A = 30
OXYGEN_B = 70 / 30
OXYGEN_NOISE = 5







############################################
# DICTIONARIES
############################################
  
# dico_aircrafts = {
#     "F-14B": {"mass": 44040, "fuel": 16200, "motor": 2}
#     , "F-14A":{"mass": 41780, "fuel": 16200, "motor": 2}
#     , "F-15C": {"mass": 29498, "fuel": 13455, "motor": 2}
#     , "F-15E": {"mass": 37637, "fuel": 22589, "motor": 2}
#     , "F-16A": {"mass": 19518, "fuel": 6843, "motor": 1}
#     , "MiG-29A": {"mass": 24079, "fuel": 7443, "motor": 2}
#     , "MiG-23MLD": {"mass": 23259, "fuel": 8378, "motor": 1}
#     , "Su-25T": {"mass": 25344, "fuel": 8356, "motor": 2} 
#     , "Su-27": {"mass": 38581, "fuel": 12324, "motor": 2}
#     , "Tu-142": {"mass": 211644, "fuel": 191802, "motor": 4}
# } 


dico_aircrafts = "boop"

def InitDicoAircrafts():
    global dico_aircrafts
    # lbs
    f = open(PATH_RESOURCES + "\\..\\Data\\aircrafts", "r")
    dico_aircrafts = eval(f.read())
    f.close()
    
    ac = list(dico_aircrafts.keys())[0]
    if 'drag_coef' not in dico_aircrafts[ac].keys():
        print("generating dico values...")
        for ac in dico_aircrafts:
            dico_aircrafts[ac]["drag_coef"] = dg.InitDragCoef()
            dico_aircrafts[ac]["lift_coef"] = dg.InitLiftCoef()
            dico_aircrafts[ac]["surface"] = dg.InitSurface()
        f = open(PATH_RESOURCES + "\\..\\Data\\aircrafts", "w+")
        f.write(str(dico_aircrafts))
        f.close()
        
    else:
        print("getting dico values...")
        
    print(dico_aircrafts)
  


## AIR SPEED

dico_air_speed = "boop"
current_air_speed = "boop"

def InitAirSpeed():
    global dico_air_speed, current_air_speed
    f = open(PATH_RESOURCES + "\\..\\Data\\air_speed", "r")
    dico_air_speed = eval(f.read())
    print(dico_air_speed)
    f.close() 
    ## to change after getting some few files
    if ACMI_FILE in dico_air_speed:
        current_air_speed = dico_air_speed[ACMI_FILE]
    else:
        current_air_speed = dico_air_speed['default']
    
    
    
# random cities for a little bit of realism
CITIES = [
    "anapa-vityazevo"
    , "krymsk"
    , "gelendzhik"
    , "novorossiysk"
    , "krasnodar center"
    , "krasnodar pashkovsky"
    , "maykop-khanskaya"
    , "sochi-adler"
    , "gudauta"
    , "tbilissi-lochini"
    , "vaziani"
    , "soganlug"
    , "mozdok"
    , "nalchik"
    , "beslan"
    , "mineralnyevody"
    , "kutaisi"
    , "kobuleti"
    , "batumi"
    ]





