'''
Created on 3 Mar 2020

@author: w.delamare
'''

import os

from Utils import DataGenerator as dg

'''
FILES AND DIRECTORIES
'''
# where is the script being run
PATH_RESOURCES = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# the acmi file to parse
ACMI_FILE = "..\\Samples\\Tacview-20191108-113901-DCS-MOHICAN_AI_final.txt2.acmi"
# the folder in which writing the resulting test files
OUT_FOLDER = "..\\TestFiles"
# sub folder (NORMAL, MISSING_COL, etc)
CURRENT_CONDITION = "Normal"

US_AIRCRAFTS = ["F-14B", "F-14A", "F-15C", "F-15E", "F-16A"]

'''
CONST
'''

g = 9.81

p0 = 101325
T0 = 288.15
L = 0.0065
R = 8.31447
M = 0.0289654

'''
VALUES
'''
# aircrafts
  
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
dico_air_speed = "boop"
current_air_speed = "boop"

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
  



def InitAirSpeed():
    global dico_air_speed, current_air_speed
    f = open(PATH_RESOURCES + "\\..\\Data\\aircrafts", "r")
    dico_air_speed = eval(f.read())
    f.close() 
    ## to change after getting some few files
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
# asked google
DRAGS = [x*0.01 for x in range(5, 45, 1)]
# https://aviation.stackexchange.com/questions/46518/what-is-the-typical-value-of-maximum-lift-coefficient-for-aerobatic-aircraft
LIFTS = [x * 0.1 for x in range(10, 20, 1)]
# a little bit of noise 
DRAG_FACTOR = 10.0
LIFT_FACTOR = 4.0

MASS = [x for x in range(45000, 70000, 1000)]
MASS_FACTOR = 1000 

# https://en.wikipedia.org/wiki/Wing_loading
# same for drag (asked Philippe)
WING_AREA = [x for x in range(100, 400, 20)]
WING_FACTOR = 50

AIR_LEVELS = [33, 1600, 6600, 26000]








