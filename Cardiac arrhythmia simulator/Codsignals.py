# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:41:25 2021

@author: Juan Camilo
"""
import wfdb
import scipy.io as sio
import numpy as np

minI=[27

]
segI=[20
]

minF=[29
]
segF=[8
]

names=[207
]


for i in range(0,len(names)):

    a=wfdb.rdsamp('signals\\'+str(names[i]))


    sinls=a[0]
    pru=sinls[:,0]
    


    ti=minI[i]*60+segI[i]#vecotirzarlo
    tf=minF[i]*60+segF[i]#vecotirzarlo
    fs=360

    mi=(ti*fs)//1
    mf=(tf*fs)//1

    
    Arr=pru[mi:mf]
    Arr=Arr.reshape((1,len(Arr)))

    try:
        mat_contents = sio.loadmat('VS.mat')
        pru=np.concatenate((mat_contents['signal'],Arr),axis=1)
        sio.savemat('VS.mat', {'signal':pru})
        
    
    except:
        sio.savemat('VS.mat', {'signal':Arr})
    
        