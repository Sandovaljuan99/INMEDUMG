# -*- coding: utf-8 -*-
"""
Ventricular tachycardia, ventricular bigeminy, Atrial fibrillation, 
Atrial fibrillation, Ventricular trigeminy, Ventricular escape	, 
Normal sinus rhythm, Sinus arrhythmia, Ventricular couplet
"""
import tkinter as tk
import scipy.io as sio
from PIL import Image, ImageTk
class App():
    ancho=760
    alto=760
    estado=False
    contadores=[0,0,0,0,0,0,0,0,0]#son los que van a contar el numero de dato que se ejecuta
    #se va a cosiacar las señales
    Signal=0
    
    def __init__(self):
        #cargar las variables .mat
        self.raiz=tk.Tk()
        self.importData()
        
        self.frame=tk.Frame(self.raiz,bg="white")
        self.frame.config(width=self.ancho,height=self.alto)
        self.frame.pack()
        
        
        
        self.titulo=tk.Label(self.frame,bg="white",text="Dispositivo Generador de Arritmias Cardiacas")
        self.titulo.config(font=("Grotesque",24)) 
        self.titulo.place(x=0,y=0,width=self.ancho,height=self.alto//16)
        
        
        self.opcion = tk.IntVar()
        
        names=["Taquicardia ventricualar","Bigeminismo Ventricular","Fibrilacion atrial","Flutter atrial","Trigeminismo Ventricular",
               "Escape Ventricular","Ritmo Sinusal","Arritmia Sinusal","Couplet Ventricular"]
        
        for i in range(1,10):
            tk.Radiobutton(self.frame, text=names[i-1],font=("Grotesque",16) ,variable=self.opcion,bg="white",anchor="w",
                       value=i, command=self.selec).place(x=50,y=self.alto//8+(i-1)*self.alto//20,
                                                              width=self.ancho//2.5,height=self.alto//32)
                                                          
        temp=Image.open('LOGO_UMNG.png')
        temp=temp.resize((200, 250), Image.ANTIALIAS)
        self.imagen = ImageTk.PhotoImage(temp)
        
        tk.Label(self.raiz, image=self.imagen,bg="white").place(x=450,y=140)
            
        self.nombres=tk.Label(self.frame,bg="white",text="Juan Camilo Sandoval Cabrera\nNohora Camila Sarmiento Palma",anchor="e")
        self.nombres.config(font=("Grotesque",12)) 
        self.nombres.place(x=420,y=420,width=self.ancho//3,height=self.alto//16)
    
        
        
        
        tk.Button(self.frame, text="Iniciar",font=("Grotesque",16),command=self.Estado_DataON).place(x=270,y=600)
        tk.Button(self.frame, text="Pausar",font=("Grotesque",16),command=self.Estado_DataOFF).place(x=400,y=600)
        
        
        self.titulo.after(700,self.Enviar_Data)
        
    
    
    def Estado_DataON(self):
        self.estado=True
        
    def Estado_DataOFF(self):
        self.estado=False
        
    def Enviar_Data(self):
        delay=3
        op=self.opcion.get()
        c=op-1
        if self.estado:
            print(self.Signal[0,self.contadores[c]])
            self.contadores[c]+=1
            if c==7:
                delay=4

        
        self.titulo.after(delay,self.Enviar_Data)
        
    
        
    def selec(self):
        op=self.opcion.get()#el lunes hacer el selector
        if op==1:
            self.Signal=self.VT #variables de las señales
        elif op==2:
            self.Signal=self.VB #variables de las señales
        elif op==3:
            self.Signal=self.AFIB #variables de las señales    
        elif op==4:
            self.Signal=self.AFL #variables de las señales
        elif op==5:
            self.Signal=self.VTRI #variables de las señales
        elif op==6:
            self.Signal=self.VES #variables de las señales
        elif op==7:
            self.Signal=self.S #variables de las señales
        elif op==8:
            self.Signal=self.SARR #variables de las señales
        elif op==9:
            self.Signal=self.VCOUP #variables de las señales
        
    
    def iniciar(self):
        self.raiz.mainloop()
        
    def importData(self):
        AFIB=sio.loadmat('AFIB.mat')
        self.AFIB=AFIB['SignalNorm']
       
        AFL=sio.loadmat('AFL.mat')
        self.AFL=AFL['SignalNorm']

        S=sio.loadmat('S.mat')
        self.S=S['SignalNorm']

        VES=sio.loadmat('VS.mat')
        self.VES=VES['SignalNorm']

        
        VCOUP=sio.loadmat('VCop.mat')
        self.VCOUP=VCOUP['SignalNorm']
        
        VT=sio.loadmat('TV.mat')
        self.VT=VT['SignalNorm']

        SARR=sio.loadmat('SARR.mat')
        self.SARR=SARR['SignalNorm']

        VB=sio.loadmat('VB.mat')
        self.VB=VB['SignalNorm']

        #VT=sio.loadmat('VT.mat')#SE PERDIO
        #self.VT=VT['SignalNorm']

        VTRI=sio.loadmat('VTRI.mat')
        self.VTRI=VTRI['SignalNorm']

        



def main():
    mi_app = App()
    mi_app.iniciar()

if __name__ == '__main__':
    main()
