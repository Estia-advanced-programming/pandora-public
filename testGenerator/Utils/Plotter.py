'''
Created on 16 Mar 2020

@author: w.delamare
'''




import numpy as np
import matplotlib.pyplot as plt




def PlotValues(x, y, z, values = None, tstp = None, label=""):
    fig = plt.figure()
    
    if (values is not None):
        ax = fig.add_subplot(311, projection='3d')
    else:
        ax = fig.add_subplot(111, projection='3d')
        
    ax.plot(x, y, z)
    #ax.scatter(x, y, z, marker = '^')
    ax.scatter([x[0], x[len(x)-1]], [y[0], y[len(x)-1]], [z[0], z[len(x)-1]], c=['g', 'r'], marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(label)
    ax.legend()
    
    if (values is not None):
        plt.subplot(3, 1, 2)
        plt.plot(tstp, values)
        #plt.axvline(x=tstp[0], color='r')  
        
        plt.subplot(3, 1, 3)
        deriv = np.diff(values)
        deriv = np.concatenate(([deriv[0]], deriv), axis=0)
        plt.plot(tstp, deriv)
    
      
    plt.show()
    
    


    
def PlotDetection(x, y, z, values = None, tstp = None, label=""):
    fig = plt.figure()
    
    if (values is not None):
        ax = fig.add_subplot(311, projection='3d')
    else:
        ax = fig.add_subplot(111, projection='3d')
        
    ax.plot(x, y, z)
    #ax.scatter(x, y, z, marker = '^')
    ax.scatter([x[0], x[len(x)-1]], [y[0], y[len(x)-1]], [z[0], z[len(x)-1]], c=['g', 'r'], marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(label)
    ax.legend()
    
    if (values is not None):
        plateaux = GetPlateaux(values, tstp)
        print(plateaux)
        
        plt.subplot(3, 1, 2)
        plt.plot(tstp, values)
        for start,end in plateaux:
            plt.axvline(x=tstp[start], color='g')
            plt.axvline(x=tstp[end], color='r')  
        
        plt.subplot(3, 1, 3)
        deriv = np.diff(values)
        deriv = np.concatenate(([deriv[0]], deriv), axis=0)
        plt.plot(tstp, deriv)
    
      
    plt.show()
    
    
time_threshold = 60
deriv_threshold = 1
    
def GetPlateaux(values, tstp):
    deriv = np.diff(values)
    print(deriv)
    # get the minimum deriv values
    mins = np.where(deriv < deriv_threshold)[0]
    
    # make the diff just to check if it is continuous (almost?)
    # continous: deriv = 1
    # almost continous: deriv < thresh
    mins2 = np.diff(mins)
    res = []
    start = None
    end = None
    i = 0
    for dist in mins2:
        if dist == 1:
            if start is None:
                start = mins[i]
            else:
                pass
        else:
            if start is not None:
                end = mins[i]
                res.append([start, end])
                start = None
            else:
                pass
        i += 1
    # filter
    res2 = []
    for start, end in res:
        #if tstp[end] - tstp[start] > time_threshold * (tstp[len(tstp)-1] - tstp[0]):
        if tstp[end] - tstp[start] > time_threshold :
            res2.append([start, end])
    return res2
        
    
    