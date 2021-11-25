from os.path import dirname, join as pjoin
from numpy.core.fromnumeric import shape
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy.io import savemat
import numpy as np
from sklearn.utils import shuffle

mat_contents = sio.loadmat('S.mat')
Sinus= mat_contents['data']
Sinusy=np.zeros((Sinus.shape[0],))

mat_contents = sio.loadmat('AFL.mat')
AFL= mat_contents['data']
AFLy=np.zeros((AFL.shape[0],))+1

mat_contents = sio.loadmat('AFIB.mat')
AFIB= mat_contents['data']
AFIBy=np.zeros((AFIB.shape[0],))+2

mat_contents = sio.loadmat('TV.mat')
TV= mat_contents['data'] 
TVy=np.zeros((TV.shape[0],))+3

mat_contents = sio.loadmat('FV.mat')
FV= mat_contents['data'] 
FVy=np.zeros((FV.shape[0],))+4

Y=np.concatenate((Sinusy,AFLy,AFIBy,TVy,FVy))

X=np.concatenate((Sinus,AFL,AFIB,TV,FV))

X, Y = shuffle(X, Y, random_state=0)
p100=X.shape[0]
p70=np.intc(p100*0.7)
p20=np.intc(p100*0.2)//1
p10=np.intc(p100*0.1)//1

X_train=X[0:p70,:]
X_test=X[p70:p70+p20,:]
X_val=X[p70+p20:,:]

Y_train=Y[0:p70]
Y_test=Y[p70:p70+p20]
Y_val=Y[p70+p20:]

savemat("dataset.mat", {"X_train":X_train,"X_test":X_test,"X_val":X_val,
                        "Y_train":Y_train,"Y_test":Y_test,"Y_val":Y_val})