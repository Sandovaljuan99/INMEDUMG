#Cardiac arrhythmia simulator

in this folder you have the files:

###database
files in .mat format that are used to create the database which are extracted from different physionet repositories mainly from BIH.

###Codsignals
It is a file which is used to concatenate the databases with the help of the algorithms presented, where the times are chosen manually by observing the ECG graph in order to choose the best portion of the tracing.
###IGPY
It is the graphical interface developed for desktop in order to work in a more enjoyable way, since it was thought that the screen implemented in the project would be a rasberry touch, this does not have the serial communication only presents a simulation of sending through printouts on console.
###IGPYR
It is the graphical interface that runs on the rasberry where it takes into account an I2C protocol that goes to a DAC in a circuit, which allows to recreate the signals.
