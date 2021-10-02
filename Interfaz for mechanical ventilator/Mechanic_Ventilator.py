# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:43:53 2021

@author: Juan Camilo
"""

import time
from tkinter import *
import random
import math
import tkinter as tk
from functools import partial
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Indicador():
    
    

        
    
    def __init__(self,nowValue,x,y,widgLen,widgHigh,maxValue,minValue,outerColor,nameValue,root,bg,posL,posS,rel=1):
        self.nowValue=nowValue
        self.minValue=minValue
        self.x=x
        self.y=y
        self.widgLen=widgLen
        self.widgHigh=widgHigh
        self.maxValue=maxValue
        self.outerColor=outerColor
        self.nameValue=nameValue
        self.root=root
        self.bg=bg
        self.c = Canvas(self.root,width=self.widgLen,height=self.widgHigh,bg=self.bg, highlightthickness=0, relief='ridge')
        self.c.place(x=self.x,y=self.y)
        self.Actualizar(self.nowValue)
        
        self.Lab=Label(self.root,text=nameValue,font=("verdana",10),bg='#1684C2',fg='white').place(x=posL[0],y=posL[1])#Titulo Frecuencia
        
        self.sli = Scale(self.root, from_=self.minValue, to=self.maxValue,showvalue=0, orient=HORIZONTAL,sliderlength=10,width=20,length=180,command=self.sel,resolution=rel)
        self.sli.place(x=posS[0],y=posS[1])
        
       
        
        self.sli.set(self.nowValue+self.minValue)
        
    def Actualizar(self,val):
       
        self.nowValue=val
        
        if(self.nowValue < self.minValue): self.nowValue=self.minValue
        if(self.nowValue > self.maxValue): self.nowValue=self.maxValue-1
        self.nowValue=val-self.minValue
        devValue=float(180) / float(self.maxValue-self.minValue)
        mesureValue = devValue * self.nowValue
        x1 = self.widgLen/2
        y1 = self.widgHigh/2 + 10
        x2 = 10
        y2 = self.widgHigh/2 + 10
        angle = math.pi * int(mesureValue) / 180;
        newx = ((x2-x1)*math.cos(angle)-(y2-y1)*math.sin(angle)) + x1
        newy = ((x2-x1)*math.sin(angle)+(y2-y1)*math.cos(angle)) + y1
            
        self.c.create_oval(1 , 1,self.widgLen-1 ,self.widgHigh-1,width=2,fill=self.bg,outline=self.outerColor)
        self.c.create_text(7,y1,font="Verdana 10",anchor="w",justify=CENTER,fill=self.outerColor,text=str(self.minValue))
        self.c.create_text(self.widgLen-30,y1,font="Verdana 10",anchor="w",justify=CENTER,fill=self.outerColor,text=str(self.maxValue))
        self.c.create_text(self.widgLen/2-10,10,font="Verdana 10",anchor="w",justify=CENTER,fill=self.outerColor,text=str(self.minValue+(self.maxValue-self.minValue)//2))
        self.c.create_text(self.widgLen/8,self.widgHigh/4,font="Verdana 10",anchor="w",justify=CENTER,fill=self.outerColor,text=str((self.minValue+(self.maxValue-self.minValue)//4)))
        self.c.create_text(self.widgLen/2+self.widgLen/4,self.widgHigh/4,font="Verdana 10",anchor="w",justify=CENTER,fill=self.outerColor,text=str(self.maxValue-(self.maxValue-self.minValue)//4))
        #self.c.create_text(self.widgLen/2-20,self.widgHigh-40,font="Verdana 14",anchor="w",justify=CENTER,fill=self.outerColor,text=str(self.nowValue))
        self.c.create_rectangle(0,self.widgHigh/2+18,self.widgLen ,self.widgHigh,fill=self.bg,outline=self.bg)
        self.c.create_text(self.widgLen/2-10,self.widgHigh-50,font="Verdana 12",anchor="w",justify=CENTER,fill=self.outerColor,text=str(self.nowValue+self.minValue))
        #self.c.create_text(100,self.widgHigh-80,font="Verdana 10",anchor="w",justify=CENTER,fill=self.outerColor,text=str(self.nameValue))
        self.c.create_oval(x1 - 10, y1 - 10, x1+ 10,y1 + 10,fill=self.outerColor,outline=self.outerColor)
        self.c.create_line(x1,y1,newx,newy,width=5,fill=self.outerColor)
        
        
        
    def GetID(self):
        return self.c
    
    def setMinVal(self,val):
        self.minValue=val
    def setMaxVal(self,val):
        self.maxValue=val
    def sel(self,now):
        self.nowValue=self.sli.get()
        self.Actualizar(self.nowValue)
    
    def Change_Value(self,val):
        self.nowValue=val
        self.Actualizar(self.nowValue)
        self.sli.set(self.nowValue+self.minValue)
    
    def get_val(self):
        return self.nowValue+self.minValue
        
class Controles_CMV():
    

    
    
    
    def __init__(self,root):
        
        
        self.frecuencia=[5,80,15] #min max actual
        self.VT=[20,2000,500]
        self.I=[1,4,1]
        self.E=[1,9,2]
        self.PEEP=[0,35,5]
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]
        self.TI=1.33
        self.TE=2.67
        
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
    
        self.Ifrecuencia=Indicador(self.frecuencia[2],50,50,180,180,self.frecuencia[1],self.frecuencia[0],
                                   "white","Frecuencia c/min",self.Ventana_Controles,"#1684C2",[80,20],[50,190]) #indicador de la frecuencia
        self.I_VT=Indicador(self.VT[2],260,50,180,180,self.VT[1],self.VT[0],
            
                               "white","VT ml",self.Ventana_Controles,"#1684C2",[320,20],[260,190]) #indicador de VT
        self.I_I=Indicador(self.I[2],470,50,180,180,self.I[1],self.I[0],
                                   "white","I",self.Ventana_Controles,"#1684C2",[530,20],[470,190],0.1) #indicador de INSPIRACION
        
        self.E_I=Indicador(self.E[2],680,50,180,180,self.E[1],self.E[0],
                                   "white","E",self.Ventana_Controles,"#1684C2",[700,20],[680,190]) #indicador de E
        
        self.I_Flujo=Indicador(self.Flujo[2],50,350,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[100,320],[50,490]) #indicador de FLUJO
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],260,350,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[320,320],[260,490]) #indicador de VT
        
        self.I_PEEP=Indicador(self.PEEP[2],470,350,180,180,self.PEEP[1],self.PEEP[0],
                                   "white","PEEP  cmH2O",self.Ventana_Controles,"#1684C2",[510,320],[470,490]) #indicador de PEEP
        
        self.Ventana_Controles.after(200,self.Mod)
        


    def get_Label(self):
        return  self.Ventana_Controles
    
    
    def Mod(self):
        
        if(self.I_I.get_val()>1 and self.E_I.get_val()>1):
            self.E_I.Change_Value(1)
            
        
        self.frecuencia[2]=self.Ifrecuencia.get_val()
        self.I[2]=self.I_I.get_val()
        self.E[2]=self.E_I.get_val()
        self.VT[2]=self.I_VT.get_val()
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        self.PEEP[2]=self.I_PEEP.get_val()
        temp=60/self.frecuencia[2]
        self.TI=temp*self.I[2]/(self.E[2]+self.I[2])
        self.TE=temp*self.E[2]/(self.E[2]+self.I[2])
            
        self.Ventana_Controles.after(1,self.Mod)
    
    def getIE(self):
        return [self.I[2],self.E[2]]
    def getTimes(self):
        return [self.TI, self.TE]
        
class Controles_SIMV():  

    
    
    
    def __init__(self,root):
        
        self.psoporte=[0,60,0]
        self.frecuencia=[1,80,10] #min max actual
        self.VT=[20,2000,700]
        self.I=1
        self.E=2
        self.PEEP=[0,35,5]
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]
        self.TI=[0.10,12,2]
        self.TE=4
        
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
        
        self.I_psoporte=Indicador(self.psoporte[2],680,50,180,180,self.psoporte[1],self.psoporte[0],
                                   "white","Psoporte cmH2o",self.Ventana_Controles,"#1684C2",[700,20],[680,190]) #indicador de la presion soporte
    
        self.Ifrecuencia=Indicador(self.frecuencia[2],50,50,180,180,self.frecuencia[1],self.frecuencia[0],
                                   "white","Frecuencia c/min",self.Ventana_Controles,"#1684C2",[80,20],[50,190]) #indicador de la frecuencia
        self.I_VT=Indicador(self.VT[2],260,50,180,180,self.VT[1],self.VT[0],
            
                               "white","VT ml",self.Ventana_Controles,"#1684C2",[320,20],[260,190]) #indicador de VT
        self.I_TI=Indicador(self.TI[2],470,50,180,180,self.TI[1],self.TI[0],
                                   "white","TI",self.Ventana_Controles,"#1684C2",[530,20],[470,190],0.1) #indicador de INSPIRACION
        
        self.I_Flujo=Indicador(self.Flujo[2],50,350,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[100,320],[50,490]) #indicador de FLUJO
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],260,350,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[320,320],[260,490]) #indicador de VT
        
        self.I_PEEP=Indicador(self.PEEP[2],470,350,180,180,self.PEEP[1],self.PEEP[0],
                                   "white","PEEP  cmH2O",self.Ventana_Controles,"#1684C2",[510,320],[470,490]) #indicador de PEEP
        
        self.Ventana_Controles.after(200,self.Mod)
        
    def getIE(self):
        return [self.I,self.E]
    def getTimes(self):
        return [self.TI[2], self.TE]

    def get_Label(self):
        return  self.Ventana_Controles
    
    def Mod(self):
        
        self.psoporte[2]=self.I_psoporte.get_val()
        self.frecuencia[2]=self.Ifrecuencia.get_val()
        self.VT[2]=self.I_VT.get_val()
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        self.PEEP[2]=self.I_PEEP.get_val()
        temp=60/self.frecuencia[2]
        if self.I_TI.get_val()>=temp:
            self.I_TI.Change_Value(temp-0.2)
            self.TI[2]=temp-0.2
        else: 
            self.TI[2]=self.I_TI.get_val()
            
        self.TE=temp-self.TI[2]
        self.I=self.TI[2]/self.TE
        self.E=self.TE/self.TI[2]
        
        if self.I<=1:
            self.I=1
        if self.E<=1:
            self.E=1
        
        #print(self.I,":",self.E)
    
        self.Ventana_Controles.after(1,self.Mod)
                        
class Controles_PCV():
        
    
    def __init__(self,root):
        
        
        self.frecuencia=[5,80,30] #min max actual
        self.pcontrol=[5,60,15]
        self.I=[1,4,1]
        self.E=[1,9,2]
        self.PEEP=[0,35,5]
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]
        self.TI=0.67
        self.TE=1.33
        
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
    
        self.Ifrecuencia=Indicador(self.frecuencia[2],50,50,180,180,self.frecuencia[1],self.frecuencia[0],
                                   "white","Frecuencia c/min",self.Ventana_Controles,"#1684C2",[80,20],[50,190]) #indicador de la frecuencia
        self.I_pcontrol=Indicador(self.pcontrol[2],260,50,180,180,self.pcontrol[1],self.pcontrol[0],
                               "white","Pcontrol  cmH2O",self.Ventana_Controles,"#1684C2",[320,20],[260,190]) #indicador de VT
        self.I_I=Indicador(self.I[2],470,50,180,180,self.I[1],self.I[0],
                                   "white","I",self.Ventana_Controles,"#1684C2",[530,20],[470,190],0.1) #indicador de INSPIRACION
        
        self.E_I=Indicador(self.E[2],680,50,180,180,self.E[1],self.E[0],
                                   "white","E",self.Ventana_Controles,"#1684C2",[700,20],[680,190]) #indicador de E
        
        self.I_Flujo=Indicador(self.Flujo[2],50,350,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[100,320],[50,490]) #indicador de FLUJO
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],260,350,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[320,320],[260,490]) #indicador de VT
        
        self.I_PEEP=Indicador(self.PEEP[2],470,350,180,180,self.PEEP[1],self.PEEP[0],
                                   "white","PEEP  cmH2O",self.Ventana_Controles,"#1684C2",[510,320],[470,490]) #indicador de PEEP
        
        self.Ventana_Controles.after(200,self.Mod)
        
    def getIE(self):
        return [self.I[2],self.E[2]]
    def getTimes(self):
        return [self.TI, self.TE]

    def get_Label(self):
        return  self.Ventana_Controles
    
    def Mod(self):
        
        if(self.I_I.get_val()>1 and self.E_I.get_val()>1):
            self.E_I.Change_Value(1)
            
        
        self.frecuencia[2]=self.Ifrecuencia.get_val()
        self.I[2]=self.I_I.get_val()
        self.E[2]=self.E_I.get_val()
        self.pcontrol[2]=self.I_pcontrol.get_val()
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        self.PEEP[2]=self.I_PEEP.get_val()
        temp=60/self.frecuencia[2]
        self.TI=temp*self.I[2]/(self.E[2]+self.I[2])
        self.TE=temp*self.E[2]/(self.E[2]+self.I[2])
            
        self.Ventana_Controles.after(1,self.Mod)       
     
class Controles_PSIMV():  

    
    
    
    def __init__(self,root):
        
        self.psoporte=[0,60,0]
        self.frecuencia=[1,80,30] #min max actual
        self.pinsp=[5,60,15]
        self.I=1
        self.E=1.9
        self.PEEP=[0,35,5]
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]
        self.TI=[0.10,12,0.7]
        self.TE=1.30
        
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
        
        self.I_psoporte=Indicador(self.psoporte[2],680,50,180,180,self.psoporte[1],self.psoporte[0],
                                   "white","Psoporte cmH2o",self.Ventana_Controles,"#1684C2",[700,20],[680,190]) #indicador de la presion soporte
    
        self.Ifrecuencia=Indicador(self.frecuencia[2],50,50,180,180,self.frecuencia[1],self.frecuencia[0],
                                   "white","Frecuencia c/min",self.Ventana_Controles,"#1684C2",[80,20],[50,190]) #indicador de la frecuencia
        self.I_pinsp=Indicador(self.pinsp[2],260,50,180,180,self.pinsp[1],self.pinsp[0],
                               "white","Pinsp cmH2o",self.Ventana_Controles,"#1684C2",[320,20],[260,190]) #indicador de VT
        self.I_TI=Indicador(self.TI[2],470,50,180,180,self.TI[1],self.TI[0],
                                   "white","TI",self.Ventana_Controles,"#1684C2",[530,20],[470,190],0.1) #indicador de INSPIRACION
        
        self.I_Flujo=Indicador(self.Flujo[2],50,350,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[100,320],[50,490]) #indicador de FLUJO
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],260,350,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[320,320],[260,490]) #indicador de VT
        
        self.I_PEEP=Indicador(self.PEEP[2],470,350,180,180,self.PEEP[1],self.PEEP[0],
                                   "white","PEEP  cmH2O",self.Ventana_Controles,"#1684C2",[510,320],[470,490]) #indicador de PEEP
        
        self.Ventana_Controles.after(200,self.Mod)
        
    def getIE(self):
        return [self.I,self.E]
    def getTimes(self):
        return [self.TI[2], self.TE]
    
    def get_Label(self):
        return  self.Ventana_Controles
    
    def Mod(self):
        

        self.frecuencia[2]=self.Ifrecuencia.get_val()
        self.pinsp[2]=self.I_pinsp.get_val()
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        self.PEEP[2]=self.I_PEEP.get_val()
        temp=60/self.frecuencia[2]
        if self.I_TI.get_val()>=temp:
            self.I_TI.Change_Value(temp-0.2)
            self.TI[2]=temp-0.2
        else: 
            self.TI[2]=self.I_TI.get_val()
            
        self.TE=temp-self.TI[2]
        self.I=self.TI[2]/self.TE
        self.E=self.TE/self.TI[2]
        
        if self.I<=1:
            self.I=1
        if self.E<=1:
            self.E=1
        
        #print(self.I,":",self.E)
    
        self.Ventana_Controles.after(1,self.Mod)

class Controles_ESPON():  

    
    
    
    def __init__(self,root):
        
        self.psoporte=[0,60,15]
        self.PEEP=[0,35,5]
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]

        
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
        
        self.I_psoporte=Indicador(self.psoporte[2],680,50,180,180,self.psoporte[1],self.psoporte[0],
                                   "white","Psoporte cmH2o",self.Ventana_Controles,"#1684C2",[700,20],[680,190]) #indicador de la presion soporte
    

        
        self.I_Flujo=Indicador(self.Flujo[2],50,50,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[100,20],[50,190]) #indicador de FLUJO
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],260,50,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[320,20],[260,190]) #indicador de VT
        
        self.I_PEEP=Indicador(self.PEEP[2],470,50,180,180,self.PEEP[1],self.PEEP[0],
                                   "white","PEEP  cmH2O",self.Ventana_Controles,"#1684C2",[510,20],[470,190]) #indicador de PEEP
        
        self.Ventana_Controles.after(200,self.Mod)
        


    def get_Label(self):
        return  self.Ventana_Controles
    
    def Mod(self):
        
        self.psoporte[2]=self.I_psoporte.get_val()
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        self.PEEP[2]=self.I_PEEP.get_val()
    
    
        self.Ventana_Controles.after(1,self.Mod)

class Controles_DuoPAP():  
    
    def __init__(self,root):
        
        self.psoporte=[0,60,15]
        self.frecuencia=[1,80,10] #min max actual
        self.palta=[0,60,20] #presion alta
        self.Talto=[0.10,40,1] # tiempo alto
        self.I=1
        self.E=5
        self.PEEP=[0,35,5]
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]
        self.TE=5
        
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
        
        self.I_psoporte=Indicador(self.psoporte[2],680,50,180,180,self.psoporte[1],self.psoporte[0],
                                   "white","Psoporte cmH2o",self.Ventana_Controles,"#1684C2",[700,20],[680,190]) #indicador de la presion soporte
        
        self.Ifrecuencia=Indicador(self.frecuencia[2],50,50,180,180,self.frecuencia[1],self.frecuencia[0],
                                   "white","Frecuencia c/min",self.Ventana_Controles,"#1684C2",[80,20],[50,190]) #indicador de la frecuencia
        self.I_palta=Indicador(self.palta[2],260,50,180,180,self.palta[1],self.palta[0],
                               "white","P alta cmH2o",self.Ventana_Controles,"#1684C2",[320,20],[260,190]) #indicador de VT
        self.I_Talto=Indicador(self.Talto[2],470,50,180,180,self.Talto[1],self.Talto[0],
                                   "white","T alto s",self.Ventana_Controles,"#1684C2",[530,20],[470,190],0.1) #indicador de INSPIRACION
        
        self.I_Flujo=Indicador(self.Flujo[2],50,350,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[100,320],[50,490]) #indicador de FLUJO
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],260,350,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[320,320],[260,490]) #indicador de VT
        
        self.I_PEEP=Indicador(self.PEEP[2],470,350,180,180,self.PEEP[1],self.PEEP[0],
                                   "white","PEEP  cmH2O",self.Ventana_Controles,"#1684C2",[510,320],[470,490]) #indicador de PEEP
        
        self.Ventana_Controles.after(200,self.Mod)
        
    def getIE(self):
        return [self.I,self.E]
    def getTimes(self):
        return [self.Talto[2], self.TE]

    def get_Label(self):
        return  self.Ventana_Controles
    
    def Mod(self):
        

        self.frecuencia[2]=self.Ifrecuencia.get_val()
        self.palta[2]=self.I_palta.get_val()
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        self.PEEP[2]=self.I_PEEP.get_val()
        temp=60/self.frecuencia[2]
        if self.I_Talto.get_val()>=temp:
            self.I_Talto.Change_Value(temp-0.2)
            self.Talto[2]=temp-0.2
        else: 
            self.Talto[2]=self.I_Talto.get_val()
            
        self.TE=temp-self.Talto[2]
        self.I=self.Talto[2]/self.TE
        self.E=self.TE/self.Talto[2]
        
        if self.I<=1:
            self.I=1
        if self.E<=1:
            self.E=1
        
        #print(self.I,":",self.E)
    
        self.Ventana_Controles.after(1,self.Mod)

class Controles_APRV():
    
    def __init__(self,root):
        
        
        self.frecuencia=15 #min max actual
        self.palta=[0,60,20] #presion alta
        self.I=1
        self.E=2.1
        self.pbaja=[0,35,5] #PEEP
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]
        self.Talto=[0.10,40,1.3] #tiempo inspiracion
        self.Tbajo=[0.20,40,2.7] # tiempo espiracion
        
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
    
        self.I_pbaja=Indicador(self.pbaja[2],50,50,180,180,self.pbaja[1],self.pbaja[0],
                                   "white","P baja cmH2o",self.Ventana_Controles,"#1684C2",[80,20],[50,190]) #indicador de p baja
        self.I_palta=Indicador(self.palta[2],260,50,180,180,self.palta[1],self.palta[0],
                               "white","P alta cmH2o",self.Ventana_Controles,"#1684C2",[320,20],[260,190]) #indicador de  p alta
        
        self.I_Talto=Indicador(self.Talto[2],470,50,180,180,self.Talto[1],self.Talto[0],
                                   "white","T alto s",self.Ventana_Controles,"#1684C2",[530,20],[470,190],0.1) #indicador de INSPIRACION
        
        self.I_Tbajo=Indicador(self.Tbajo[2],680,50,180,180,self.Tbajo[1],self.Tbajo[0],
                                   "white","T bajo s",self.Ventana_Controles,"#1684C2",[700,20],[680,190],0.1) #indicador de E
        
        self.I_Flujo=Indicador(self.Flujo[2],50,350,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[100,320],[50,490]) #indicador de FLUJO
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],260,350,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[320,320],[260,490]) #indicador de VT
        
        
        self.Ventana_Controles.after(200,self.Mod)

    def getIE(self):
        return [self.I,self.E]
    def getTimes(self):
        return [self.Talto[2], self.Tbajo[2]]
    
    def get_Label(self):
        return  self.Ventana_Controles
    
    def Mod(self):
        
        self.palta[2]=self.I_palta.get_val()
        self.pbaja[2]=self.I_pbaja.get_val()
        
        self.Talto[2]=self.I_Talto.get_val()
        self.Tbajo[2]=self.I_Tbajo.get_val()
        temp=self.Talto[2]+self.Tbajo[2]
        self.frecuencia=60/temp
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        
        self.I=self.Talto[2]/self.Tbajo[2]
        self.E=self.Tbajo[2]/self.Talto[2]
        
        if self.I<=1:
            self.I=1
        if self.E<=1:
            self.E=1
        
        #print(self.I,":",self.E)
        #print(self.frecuencia)
            
        self.Ventana_Controles.after(1,self.Mod)

class Controles_ASV():
    
    
        
    
    def __init__(self,root):
        
        
        self.LIMpasv=[5,60,30] # limite presion asv
        self.Pvolmin=[25,350,55] # % de volumen minuto
        self.volmin=3.9
        self.PEEP=[0,35,5]
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]
        
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
    
        self.I_LIMpasv=Indicador(self.LIMpasv[2],50,50,180,180,self.LIMpasv[1],self.LIMpasv[0],
                                   "white"," Lim. PASV cmH2o",self.Ventana_Controles,"#1684C2",[80,20],[50,190]) #indicador de la frecuencia
        self.I_Pvolmin=Indicador(self.Pvolmin[2],260,50,180,180,self.Pvolmin[1],self.Pvolmin[0],
                               "white","% VolMin",self.Ventana_Controles,"#1684C2",[320,20],[260,190]) #indicador de VT
        self.I_Flujo=Indicador(self.Flujo[2],470,50,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[530,20],[470,190],0.1) #indicador de INSPIRACION
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],680,50,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[700,20],[680,190]) #indicador de E
        
        self.I_PEEP=Indicador(self.PEEP[2],50,350,180,180,self.PEEP[1],self.PEEP[0],
                                   "white","PEEP  cmH2O",self.Ventana_Controles,"#1684C2",[100,320],[50,490]) #indicador de FLUJO
        
        
        self.Ventana_Controles.after(200,self.Mod)
        


    def get_Label(self):
        return  self.Ventana_Controles
    
    def Mod(self):
        
        
    
        self.LIMpasv[2]=self.I_LIMpasv.get_val()
        self.Pvolmin[2]=self.I_Pvolmin.get_val()
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        self.PEEP[2]=self.I_PEEP.get_val()

            
        self.Ventana_Controles.after(1,self.Mod)       

class Controles_NIV():
    
    
    def __init__(self,root):
        
        
        
        self.Psoporte=[0,60,15]
        self.PEEP=[0,35,5]
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]
       
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
    
        self.I_Psoporte=Indicador(self.Psoporte[2],50,50,180,180,self.Psoporte[1],self.Psoporte[0],
                                   "white"," Lim. PASV cmH2o",self.Ventana_Controles,"#1684C2",[80,20],[50,190]) #indicador de la frecuencia
        
        self.I_Flujo=Indicador(self.Flujo[2],260,50,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[320,20],[260,190]) #indicador de FLUJO
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],470,50,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[530,20],[470,190]) #indicador de VT
        
        self.I_PEEP=Indicador(self.PEEP[2],680,50,180,180,self.PEEP[1],self.PEEP[0],
                                   "white","PEEP  cmH2O",self.Ventana_Controles,"#1684C2",[700,20],[680,190]) #indicador de PEEP
        
        self.Ventana_Controles.after(200,self.Mod)
        


    def get_Label(self):
        return  self.Ventana_Controles
    
    def Mod(self):
        
        self.Psoporte[2]=self.I_Psoporte.get_val()
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        self.PEEP[2]=self.I_PEEP.get_val()

            
        self.Ventana_Controles.after(1,self.Mod)

class Controles_NIVST():  

    
    
    
    def __init__(self,root):
        
        self.pinsp=[0,60,0]
        self.frecuencia=[1,80,10] #min max actual
        self.I=1
        self.E=2
        self.PEEP=[0,35,5]
        self.Flujo=[1,20,5]
        self.Oxigeno=[21,100,50]
        self.TI=[0.10,12,2]
        self.TE=4
        
        self.root=root
        
        self.Ventana_Controles=Frame(self.root,bg="#1684C2",width=1100,height=580)
        
        self.I_pinsp=Indicador(self.pinsp[2],470,50,180,180,self.pinsp[1],self.pinsp[0],
                                   "white","Pinsp cmH2o",self.Ventana_Controles,"#1684C2",[510,20],[470,190]) #indicador de la presion soporte
    
        self.Ifrecuencia=Indicador(self.frecuencia[2],50,50,180,180,self.frecuencia[1],self.frecuencia[0],
                                   "white","Frecuencia c/min",self.Ventana_Controles,"#1684C2",[80,20],[50,190]) #indicador de la frecuencia

        self.I_TI=Indicador(self.TI[2],260,50,180,180,self.TI[1],self.TI[0],
                                   "white","TI",self.Ventana_Controles,"#1684C2",[320,20],[260,190],0.1) #indicador de INSPIRACION
        
        self.I_Flujo=Indicador(self.Flujo[2],50,350,180,180,self.Flujo[1],self.Flujo[0],
                                   "white","Flujo L/min",self.Ventana_Controles,"#1684C2",[100,320],[50,490]) #indicador de FLUJO
        
        self.I_Oxigeno=Indicador(self.Oxigeno[2],260,350,180,180,self.Oxigeno[1],self.Oxigeno[0],
                                   "white","Oxigeno %",self.Ventana_Controles,"#1684C2",[320,320],[260,490]) #indicador de VT
        
        self.I_PEEP=Indicador(self.PEEP[2],470,350,180,180,self.PEEP[1],self.PEEP[0],
                                   "white","PEEP  cmH2O",self.Ventana_Controles,"#1684C2",[510,320],[470,490]) #indicador de PEEP
        
        self.Ventana_Controles.after(200,self.Mod)
        
    def getIE(self):
        return [self.I,self.E]
    def getTimes(self):
        return [self.TI[2], self.TE]
    def get_Label(self):
        return  self.Ventana_Controles
    
    def Mod(self):
        
        self.pinsp[2]=self.I_pinsp.get_val()
        self.frecuencia[2]=self.Ifrecuencia.get_val()
        self.Flujo[2]=self.I_Flujo.get_val()
        self.Oxigeno[2]=self.I_Oxigeno.get_val()
        self.PEEP[2]=self.I_PEEP.get_val()
        temp=60/self.frecuencia[2]
        if self.I_TI.get_val()>=temp:
            self.I_TI.Change_Value(temp-0.2)
            self.TI[2]=temp-0.2
        else: 
            self.TI[2]=self.I_TI.get_val()
            
        self.TE=temp-self.TI[2]
        self.I=self.TI[2]/self.TE
        self.E=self.TE/self.TI[2]
        
        if self.I<=1:
            self.I=1
        if self.E<=1:
            self.E=1
        
        #print(self.I,":",self.E)
    
        self.Ventana_Controles.after(1,self.Mod)

class Alarma():
    
    def __init__(self,root,name,maxV,minV,tol,valAcS1,valAcS2,a,b,h=12,rel=1):
        self.minVal=minV
        self.maxVal=maxV
        self.name=name
        self.root=root
        self.tol=tol
        self.valAcS1=valAcS1
        self.valAcS2=valAcS2
        
        
        self.ValS1=[self.valAcS2+self.tol,self.maxVal,self.valAcS1]
        self.ValS2=[self.minVal,self.valAcS1-self.tol,self.valAcS2]
        

        Label(self.root,text=self.name,font=("Verdana",12),bg='#1684C2',fg='white',width=h).place(x=a+15,y=b)
        self.sl1 = Scale(self.root, from_=self.ValS1[1], to=self.ValS1[0],showvalue=1, orient=VERTICAL,sliderlength=10,width=20,length=180,resolution=rel,label='Max',bg='#1684C2',fg='white',command=self.ChangeS1)
        self.sl1.set(self.ValS1[2])
        self.sl1.place(x=a,y=b+40)
        
        self.sl2 = Scale(self.root, from_=self.ValS2[1], to=self.ValS2[0],showvalue=1, orient=VERTICAL,sliderlength=10,width=20,length=180,resolution=rel,label='Min',bg='#1684C2',fg='white',command=self.ChangeS2)
        self.sl2.set(self.ValS2[2])
        self.sl2.place(x=a+79,y=b+40)
        
    def ChangeS1(self,nw):
        temp=self.sl1.get()
        self.ValS1[2]=temp
        self.sl2.config(from_=self.ValS1[2]-self.tol)
        
    def ChangeS2(self,nw):
        temp=self.sl2.get()
        self.ValS2[2]=temp
        self.sl1.config(to=self.ValS2[2]+self.tol)

class Ventilator(): #cambiar nombre
    def __init__(self):
        

        
        
        
        self.root=Tk()
        self.root.resizable(0,0)
        self.root.geometry("1280x720")
        self.root.configure(background='white')
        self.estado=0
        self.op=0
        
        
        
        #Conf. paciente
        self.Ventana_Paciente=Frame(self.root,bg="#1684C2",width=1100,height=580)

        self.PCI=30
        self.estatura=170
        self.sexo=1
        
        def CalPCI(pru):
            if(self.sexo==1):
                self.PCI=50+0.9*(self.slestatura.get()-152.4)
                self.PCI=self.PCI//1
            else:
                self.PCI=45.5+0.9*(self.slestatura.get()-152.4)
                self.PCI=self.PCI//1
                
            
            self.PCII.config(text="PCI: "+str(self.PCI))
        def defsexoM():
            self.sexo=1
            self.b1.config(bg='#8799A3')
            self.b2.config(bg='#EEEEEE')
            CalPCI(1)
            
        def defsexoF():
            self.b2.config(bg='#8799A3')
            self.b1.config(bg='#EEEEEE')
            self.sexo=0
            CalPCI(1)
           

            
            
        self.b1=Button(self.Ventana_Paciente,text='Masculino',bg='#8799A3',font=("Verdana",20),command=defsexoM,height=2,width=10)
        self.b1.place(x=300,y=150)
        self.b2=Button(self.Ventana_Paciente,text='Femenino',font=("Verdana",20),command=defsexoF,height=2,width=10)
        self.b2.place(x=600,y=150)
        
        self.slestatura = Scale(self.root, from_=30, to=250,showvalue=1,bg='#1684C2',font=("Verdana",14),fg="white",orient=HORIZONTAL,sliderlength=10,width=30,length=480,label='Estatura (cm)',command=CalPCI)
        self.slestatura.set(170)
        self.slestatura.place(x=300,y=300)
        
        self.PCII=Label(self.Ventana_Paciente,text="PCI: "+str(50),font=("Verdana",20),bg='#1684C2',fg='white')
        self.PCII.place(x=485,y=400)
        
            
        #Controles
        
        self.modoCMV=Controles_CMV(self.root)
        self.modoSIMV=Controles_SIMV(self.root)
        self.modoPCV=Controles_PCV(self.root)
        self.modoPSIMV=Controles_PSIMV(self.root)
        self.modoESPON=Controles_ESPON(self.root)
        self.modoDuoPAP=Controles_DuoPAP(self.root)
        self.modoAPRV=Controles_APRV(self.root)
        self.modoASV = Controles_ASV(self.root)
        self.NIV=Controles_NIV(self.root)
        self.NIVST=Controles_NIVST(self.root)
        

        self.ventanas=[self.modoCMV,self.modoSIMV,self.modoPCV,self.modoPSIMV, self.modoESPON, self.modoDuoPAP,self.modoAPRV, self.modoASV ,self.NIV,self.NIVST]
        self.titulos=['CMV','SIMV','PCV','PSIMV', 'ESPON', 'DuoPAP', 'APRV', 'ASV', 'NIV', 'NIVST'] 
        #               0      1     2      3        4        5        6       7      8       9
        
        self.Ventana_Controles=self.ventanas[0].get_Label()
        

        
        
        
        
        
        
        
        
        # Alarmas
        self.Ventana_Alarmas=Frame(self.root,bg="#1684C2",width=1100,height=580)
      
        self.A_presion=Alarma(self.Ventana_Alarmas,'Presión',70,4,1,40,5,20,30,12)
        
        self.A_Vol_MinESP=Alarma(self.Ventana_Alarmas,'VolMinEsp',50,0.1,0.5,10,4,320,30,rel=0.1)
        
        self.A_ftotal=Alarma(self.Ventana_Alarmas,'ftotal',100,0,1,10,0,620,30)
        
        self.A_Vt=Alarma(self.Ventana_Alarmas,'ftotal',3000,0,5,440,0,900,30,rel=5)
        
        self.A_CO2=Alarma(self.Ventana_Alarmas,'PetCO2',100,0,1,50,30,170,300,rel=5)
        
        #Monitorizacion
        self.Ventana_Monitorizacion=Frame(self.root,bg="#1684C2",width=1100,height=580)

        figure = plt.Figure(figsize=(10,2.8), dpi=100,facecolor='#1684C2')
        self.ax1 = figure.add_subplot(111)
        self.ax1.tick_params(colors='white')
        self.ax1.grid(True,color='black'),self.ax1.set_xlabel('$Muestra$',color='white'),self.ax1.set_ylabel('$Temperatura$',color='white')
        self.line1 = FigureCanvasTkAgg(figure,self.Ventana_Monitorizacion)
        self.line1.get_tk_widget().place(x=0,y=0)
        
        
        
        figure = plt.Figure(figsize=(10,2.8), dpi=100,facecolor='#1684C2')
        self.ax2 = figure.add_subplot(111)
        self.ax2.tick_params(colors='white')
        self.ax2.grid(True,color='black'),self.ax2.set_xlabel('$Muestra$',color='white'),self.ax2.set_ylabel('$Temperatura$',color='white')
        self.line2 = FigureCanvasTkAgg(figure,self.Ventana_Monitorizacion)
        self.line2.get_tk_widget().place(x=0,y=278)
        
        #ax.set_xlim([0,100])
#ax.set_ylim([20,32])
#ax.set_xlabel('$Muestra$'),ax.set_ylabel('$Temperatura$')
#ax.set_title('$Respiracion$')
        
        
        
        
        
        #modo
        self.Ventana_Modo=Frame(self.root,bg="#1684C2",width=1100,height=580)
        #tiene 7
        wh=10
        hg=1
        Label(self.Ventana_Modo,text="Ventilación Controlada por presión bifásica", bg='#1684C2',font=("Verdana",16), fg="white").place(x=310,y=20)
        Button(self.Ventana_Modo,text="PCV+",font=("Verdana",20),command=partial(self.Change_Alarmas,2),width=wh, height=hg).place(x=10,y=70)
        Button(self.Ventana_Modo,text="PSIMV+",font=("Verdana",20),command=partial(self.Change_Alarmas,3),width=wh, height=hg).place(x=220,y=70)
        Button(self.Ventana_Modo,text="ESPONT" ,font=("Verdana",20),command=partial(self.Change_Alarmas,4),width=wh, height=hg).place(x=430,y=70)
        Button(self.Ventana_Modo,text="DuoPAP" ,font=("Verdana",20),command=partial(self.Change_Alarmas,5),width=wh, height=hg).place(x=640,y=70)
        Button(self.Ventana_Modo,text="APRV",font=("Verdana",20),command=partial(self.Change_Alarmas,6),width=wh, height=hg).place(x=850,y=70)
        
        
        Label(self.Ventana_Modo,text="Ventilación Controlada por Volumen", bg='#1684C2',font=("Verdana",16), fg="white").place(x=350,y=150)
        Button(self.Ventana_Modo,text="(S)CMV+",font=("Verdana",20),command=partial(self.Change_Alarmas,0),width=wh, height=hg).place(x=220,y=200)
        Button(self.Ventana_Modo,text="SIMV+",font=("Verdana",20),command=partial(self.Change_Alarmas,1),width=wh, height=hg).place(x=640,y=200)
    
        Label(self.Ventana_Modo,text="Ventilación no invasiva", bg='#1684C2',font=("Verdana",16), fg="white").place(x=405,y=270)
        Button(self.Ventana_Modo,text="NIV",font=("Verdana",20),command=partial(self.Change_Alarmas,8),width=wh, height=hg).place(x=220,y=320)
        Button(self.Ventana_Modo,text="ANIV-ST",font=("Verdana",20),command=partial(self.Change_Alarmas,9),width=wh, height=hg).place(x=640,y=320)
        
        Label(self.Ventana_Modo,text="Ventilación inteligente", bg='#1684C2',font=("Verdana",16), fg="white").place(x=408,y=400)
        Button(self.Ventana_Modo,text="ASV",font=("Verdana",20),command=partial(self.Change_Alarmas,7),width=wh, height=hg).place(x=430,y=450)
        

        
        self.Current_Ventana=self.Ventana_Modo
        self.Current_Ventana.place(x=0,y=0)
        
        #botones
        self.Ventana_Botones=Frame(self.root, bg="blue",width=1280, height=140)
        self.Ventana_Botones.place(x=0,y=580)
        
        Button(self.Ventana_Botones, text="Config Paciente",width=20,height=5,font=("Verdana",15),command=self.V_Paciente,bg='#A7B7C1').place(x=0, y=0)
        Button(self.Ventana_Botones, text="Controles",width=20,height=5,font=("Verdana",15),command=self.V_Control,bg='#A7B7C1').place(x=256, y=0)
        Button(self.Ventana_Botones, text="Alarmas",width=20,height=5,font=("Verdana",15),command=self.V_Alarmas,bg='#A7B7C1').place(x=256*2, y=0)
        Button(self.Ventana_Botones, text="Monitorizacion",width=20,height=5,font=("Verdana",15), command=self.V_Monitorizacion,bg='#A7B7C1').place(x=256*3, y=0)
        Button(self.Ventana_Botones, text="Modo",width=20,height=5,font=("Verdana",15), command=self.V_Modo,bg='#A7B7C1').place(x=256*4, y=0)
        
        
        #cosas varias
        
        self.Ventana_Varios=Frame(self.root, bg="#32A9EE",width=1280-1100, height=580)
        self.Ventana_Varios.place(x=1100,y=0)
        self.Start=Button(self.Ventana_Varios, text="Inicio Ventilacion",width=15,height=3,font=("Verdana",14),bg='#A7B7C1', command=self.loop)
        self.Start.place(x=0, y=0)
        self.ModoI=Label(self.Ventana_Varios, text="Modo:ASV",font=("Verdana",14),width=15,height=3, bg="#32A9EE")
        self.ModoI.place(x=0,y=100)
        self.I_EI=Label(self.Ventana_Varios, text="Relación IE 1:2",font=("Verdana",14),width=15,height=3, bg="#32A9EE")
        self.I_EI.place(x=0,y=200)
        self.I_TI=Label(self.Ventana_Varios, text="TI(seg): 3",font=("Verdana",14),width=15,height=2, bg="#32A9EE")
        self.I_TI.place(x=0,y=280)
        self.I_TE=Label(self.Ventana_Varios, text="TE(seg): 3",font=("Verdana",14),width=15,height=2, bg="#32A9EE")
        self.I_TE.place(x=0,y=350)
        
        Button(self.Ventana_Varios,text="Apagar alarmas",width=15,height=2,font=("Verdana",14),bg='#A7B7C1').place(x=0,y=420)
        Button(self.Ventana_Varios,text="Standby",width=15,height=2,font=("Verdana",14),command=self.off,bg='#A7B7C1').place(x=0,y=500)
        
        self.I_EI.after(300,self.change_vals)
        
        
        
        
        
        
        
        
    # Mostrar el frame correspondiente segun el boton
    def loop(self):
        self.estado=1
        print("Inicia Ventilacion")
        
    def mostrar(self):
        #self.Indicador1.GetID().place_forget()
        self.r2.place_forget()
        
    def V_Paciente(self):
        self.Current_Ventana.place_forget()
        self.Current_Ventana=self.Ventana_Paciente
        self.Current_Ventana.place(x=0,y=0)
        
    def V_Control(self):
        self.Current_Ventana.place_forget()
        self.Current_Ventana=self.Ventana_Controles
        self.Current_Ventana.place(x=0,y=0)
        
    def V_Alarmas(self):
        self.Current_Ventana.place_forget()
        self.Current_Ventana=self.Ventana_Alarmas
        self.Current_Ventana.place(x=0,y=0)
    def V_Monitorizacion(self):
        self.Current_Ventana.place_forget()
        self.Current_Ventana=self.Ventana_Monitorizacion
        self.Current_Ventana.place(x=0,y=0)
    def V_Modo(self):
        self.Current_Ventana.place_forget()
        self.Current_Ventana=self.Ventana_Modo
        self.Current_Ventana.place(x=0,y=0)
    
    def Change_Alarmas(self,op):
        self.Ventana_Controles.place_forget()
        self.Ventana_Controles=self.ventanas[op].get_Label()
        self.Ventana_Controles.place(x=0,y=0)
        self.ModoI.config(text='Modo:'+self.titulos[op])
        self.op=op
        
        
    def change_vals(self):
        #Cambio I:E
        if((self.op != 4) and (self.op !=7)  and (self.op != 8)):

            temp=self.ventanas[self.op].getIE()
            self.I_EI.config(text='Relación IE '+str(round(temp[0],2))+":"+str(round(temp[1],2)))
            temp=self.ventanas[self.op].getTimes()
            self.I_TI.config(text='TI(seg): '+str(round(temp[0],2)))
            self.I_TE.config(text='TE(seg): '+str(round(temp[1],2)))
        else:
            self.I_EI.config(text='Relación IE ?:?')
            self.I_TI.config(text='TI(seg): ?')
            self.I_TE.config(text='TE(seg): ?')
        self.I_EI.after(500,self.change_vals)
    
    def off(self):
        self.estado=0
        print("Se apago la ventilación")
    
    def run(self):
        self.root.mainloop()



