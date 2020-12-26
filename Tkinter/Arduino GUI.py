import tkinter as tk
from tkinter import ttk
import serial
import threading

# A simple Information Window
class InformWindow:
    def __init__(self,informStr):
        self.window = tk.Tk()
        self.window.title("Info")
        self.window.geometry("220x60")
        label = tk.Label(self.window, text=informStr)
        buttonOK = tk.Button(self.window,text="OK",command=self.processButtonOK)
        label.pack(side = tk.TOP)
        buttonOK.pack(side = tk.BOTTOM)
        self.window.mainloop()

    def processButtonOK(self):
        self.window.destroy()

class mainGUI:
    def __init__(self):
        window = tk.Tk()
        window.title("Arduino GUI Demo")
        self.ardState = False # is arduino open or not

        # a frame contains COM's information, and start/stop button
        frame_COMinf = tk.Frame(window)
        frame_COMinf.grid(row = 1, column = 1)

        labelCOM = tk.Label(frame_COMinf,text="Port: ")
        self.COM = tk.StringVar(value = "COM3")
        ertryCOM = tk.Entry(frame_COMinf, textvariable = self.COM)
        labelCOM.grid(row = 1, column = 1, padx = 5, pady = 3)
        ertryCOM.grid(row = 1, column = 2, padx = 5, pady = 3)

        labelBaudrate = tk.Label(frame_COMinf,text="Baudrate: ")
        self.Baudrate = tk.IntVar(value = 9600)
        ertryBaudrate = tk.Entry(frame_COMinf, textvariable = self.Baudrate)
        labelBaudrate.grid(row = 1, column = 3, padx = 5, pady = 3)
        ertryBaudrate.grid(row = 1, column = 4, padx = 5, pady = 3)

        labelParity = tk.Label(frame_COMinf,text="Parity: ")
        self.Parity = tk.StringVar(value ="NONE")
        comboParity = ttk.Combobox(frame_COMinf, width = 17, textvariable=self.Parity)
        comboParity["values"] = ("NONE","ODD","EVEN","MARK","SPACE")
        comboParity["state"] = "readonly"
        labelParity.grid(row = 2, column = 1, padx = 5, pady = 3)
        comboParity.grid(row = 2, column = 2, padx = 5, pady = 3)

        labelStopbits = tk.Label(frame_COMinf,text="Stopbits: ")
        self.Stopbits = tk.StringVar(value ="1")
        comboStopbits = ttk.Combobox(frame_COMinf, width = 17, textvariable=self.Stopbits)
        comboStopbits["values"] = ("1","1.5","2")
        comboStopbits["state"] = "readonly"
        labelStopbits.grid(row = 2, column = 3, padx = 5, pady = 3)
        comboStopbits.grid(row = 2, column = 4, padx = 5, pady = 3)
        
        self.buttonSS = tk.Button(frame_COMinf, text = "Start", command = self.processButtonSS)
        self.buttonSS.grid(row = 3, column = 4, padx = 5, pady = 3, sticky = tk.E)

        # serial object
        self.ser = serial.Serial()
        # serial read threading
        self.ReadardThread = threading.Thread(target=self.Readard)
        self.ReadardThread.start()

        frameRecv = tk.Frame(window)
        frameRecv.grid(row = 2, column = 1)
        labelOutText = tk.Label(frameRecv,text="Received Data:")
        labelOutText.grid(row = 1, column = 1, padx = 3, pady = 2, sticky = tk.W)

        frameRecvSon = tk.Frame(frameRecv)
        frameRecvSon.grid(row = 2, column =1)
        scrollbarRecv = tk.Scrollbar(frameRecvSon)
        scrollbarRecv.pack(side = tk.RIGHT, fill = tk.Y)
        self.OutputText = tk.Text(frameRecvSon, wrap = tk.WORD, width = 60, height = 20, yscrollcommand = scrollbarRecv.set)
        self.OutputText.pack()

        frameTrans = tk.Frame(window)
        frameTrans.grid(row = 3, column = 1)
        
        labelInText1 = tk.Label(frameTrans,text="RPM:")
        labelInText1.grid(row = 1, column = 1, padx = 0, pady = 2, sticky = tk.W)
        frameTransSon1 = tk.Frame(frameTrans)
        frameTransSon1.grid(row = 2, column =1)
        self.InputText1 = tk.Text(frameTransSon1, wrap = tk.WORD, width = 56, height = 1)
        self.InputText1.pack()
        self.buttonSend = tk.Button(frameTrans, text = "Send", command = self.processButtonSend1)
        self.buttonSend.grid(row = 2, column = 2, padx = 3, pady = 2, sticky = tk.E)

        labelInText2 = tk.Label(frameTrans,text="Temperature (C):")
        labelInText2.grid(row = 3, column = 1, padx = 0, pady = 2, sticky = tk.W)
        frameTransSon2 = tk.Frame(frameTrans)
        frameTransSon2.grid(row = 4, column =1)
        self.InputText2 = tk.Text(frameTransSon2, wrap = tk.WORD, width = 56, height = 1)
        self.InputText2.pack()
        self.buttonSend = tk.Button(frameTrans, text = "Send", command = self.processButtonSend2)
        self.buttonSend.grid(row = 4, column = 2, padx = 3, pady = 2, sticky = tk.E)

        labelInText3 = tk.Label(frameTrans,text="pH:")
        labelInText3.grid(row = 5, column = 1, padx = 0, pady = 2, sticky = tk.W)
        frameTransSon3 = tk.Frame(frameTrans)
        frameTransSon3.grid(row = 6, column = 1)
        self.InputText3 = tk.Text(frameTransSon3, wrap = tk.WORD, width = 56, height = 1)
        self.InputText3.pack()
        self.buttonSend = tk.Button(frameTrans, text = "Send", command = self.processButtonSend3)
        self.buttonSend.grid(row = 6, column = 2, padx = 3, pady = 2, sticky = tk.E)
        
        window.mainloop()

    def processButtonSS(self):
        
        if (self.ardState):
            self.ser.close()
            self.buttonSS["text"] = "Start"
            self.ardState = False
        else:
            # restart serial port
            self.ser.port = self.COM.get()
            self.ser.baudrate = self.Baudrate.get()
            
            strParity = self.Parity.get()
            if (strParity=="NONE"):
                self.ser.parity = serial.PARITY_NONE;
            elif(strParity=="ODD"):
                self.ser.parity = serial.PARITY_ODD;
            elif(strParity=="EVEN"):
                self.ser.parity = serial.PARITY_EVEN;
            elif(strParity=="MARK"):
                self.ser.parity = serial.PARITY_MARK;
            elif(strParity=="SPACE"):
                self.ser.parity = serial.PARITY_SPACE;
                
            strStopbits = self.Stopbits.get()
            if (strStopbits == "1"):
                self.ser.stopbits = serial.STOPBITS_ONE;
            elif (strStopbits == "1.5"):
                self.ser.stopbits = serial.STOPBITS_ONE_POINT_FIVE;
            elif (strStopbits == "2"):
                self.ser.stopbits = serial.STOPBITS_TWO;
            
            try:
                self.ser.open()
            except:
                infromStr = "Can't open "+self.ser.port
                InformWindow(infromStr)
            
            if (self.ser.isOpen()): # open success
                self.buttonSS["text"] = "Stop"
                self.ardState = True

    def processButtonSend1(self):
        if (self.ardState):
            strToSend = self.InputText1.get(1.0,tk.END)
            bytesToSend = strToSend[0:-1].encode(encoding='ascii')
            self.ser.write(bytesToSend)
            print(bytesToSend)
        else:
            infromStr = "Not Connectted!"
            InformWindow(infromStr)

    def processButtonSend2(self):
        if (self.ardState):
            strToSend = self.InputText2.get(1.0,tk.END)
            bytesToSend = strToSend[0:-1].encode(encoding='ascii')
            self.ser.write(bytesToSend)
            print(bytesToSend)
        else:
            infromStr = "Not Connectted!"
            InformWindow(infromStr)
    def processButtonSend3(self):
        if (self.ardState):
            strToSend = self.InputText3.get(1.0,tk.END)
            bytesToSend = strToSend[0:-1].encode(encoding='ascii')
            self.ser.write(bytesToSend)
            print(bytesToSend)
        else:
            infromStr = "Not Connectted!"
            InformWindow(infromStr)

    def Readard(self):
        # print("Threading...")
        while True:
            if (self.ardState):
                try:
                    ch = self.ser.read().decode(encoding='ascii')
                    print(ch,end='')
                    self.OutputText.insert(tk.END,ch)
                except:
                    infromStr = "Something wrong in receiving."
                    InformWindow(infromStr)
                    self.ser.close() # close the serial when catch exception
                    self.buttonSS["text"] = "Start"
                    self.ardState = False
                    

mainGUI()
