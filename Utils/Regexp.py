'''
Created on 2 Mar 2020

@author: w.delamare
'''


import re


#2f01,T=7.083623|3.9313857|9445.04||0.6|275.6|736932.88|-306500.63|268.8,
#Type=Air+FixedWing,Name=E-3A,Pilot=OVERLORD11,Group=TACS,Color=Blue,Coalition=Enemies,Country=us
re_flight_id = re.compile("^(.*?),.*?,Type\=Air\+FixedWing,Name=(.*?),", re.M)
def GetFlightsIDs(s):
    return re.findall(re_flight_id, s)



# 0,ReferenceTime=2011-06-01T04:00:00Z
re_init_tstp = re.compile("0,ReferenceTime\=(.*)")
def GetInitialTimestamp(s):
    val = re.findall(re_init_tstp, s)[0]
    return val


re_records = re.compile("(^#\d*.*?)(?:^\#\d*|0,AuthenticationKey)", re.M | re.DOTALL)
def GetRecords(s):
    recs = re.findall(re_records, s)
    # discard the first one
    recs = recs[1:]
    return recs
  
re_tstp = re.compile("^#(.*)")  
def GetTstp(rec):
    return re.findall(re_tstp, rec)[0]

def GetValues(rec, f_id):
    #print(rec)
    #print("^" + f_id + ",T=(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?),.*$")
    re_values = re.compile("^" + f_id + ",T=(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?),*.*$", re.M)
    tab = re.findall(re_values, rec)
    if len(tab) > 0:
        return tab[0]
    return None