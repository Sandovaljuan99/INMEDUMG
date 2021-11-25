from os.path import dirname, join as pjoin
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.io import savemat
import numpy as np



mat_contents = sio.loadmat('TV.mat')
data= mat_contents['SignalNorm']
print(data.shape)
l=data.shape[1]
wsz=640
N_ventanas=l//640
data_u=640*N_ventanas
data=data[0,0:data_u]

data=data.reshape((N_ventanas,wsz))
print(data.shape)

for i in range(0,data.shape[0]):
    Vmin=min(data[i,:])
    data[i,:]-=Vmin
    Vmax=max(data[i,:])
    data[i,:]/=Vmax
plt.plot(data[0,:])
plt.show()
    

savemat("TV.mat", {"data":data})