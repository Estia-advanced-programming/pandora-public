'''
Created on 2 Mar 2020

@author: w.delamare
'''

import os
import sys

from datetime import datetime



'''
To run the script outside Eclipse
(otherwise import pbms)
'''
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
os.chdir(SCRIPT_DIR)

from Utils import Regexp as r
from Utils import Config as c
from Utils import FileGenerator as fg




if __name__ == '__main__':
    
    ## Take care of output folders
    if not os.path.exists(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER):
        os.mkdir(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER)
        
    if not os.path.exists(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION[1]):
        os.mkdir(c.PATH_RESOURCES + "\\" + c.OUT_FOLDER + "\\" + c.CURRENT_CONDITION[1])
    
    
    ## parse acmi file
    f = open(c.PATH_RESOURCES + "\\" + c.ACMI_FILE)
    s = f.read()
    flights = r.GetFlightsIDs(s)
    start_tstp = datetime.strptime(r.GetInitialTimestamp(s[0:500]), '%Y-%m-%dT%H:%M:%SZ')
    f.close()
    
    ## init dictionaries used for consistency across run
    c.InitDicoAircrafts()
    c.InitAirSpeed()
    
    ## process every records
    records = r.GetRecords(s)
    for f_id, f_name in flights:
        f_name = f_name.split(" ")[0]
        if f_name in ["A-10A"]:
            continue
        print("creating file for " + f_id + "_" + f_name)
        fg.GenerateFile(f_id, f_name, records, start_tstp)
        pass