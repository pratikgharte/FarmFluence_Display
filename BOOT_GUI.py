import RPi.GPIO as GPIO
import tkinter as tk
import tkinter.font as TkFont
from tkinter import *
from tkinter import ttk
import time
#from signal import pause
import threading
from AtlasOEM_PH import AtlasOEM_PH
from AtlasOEM_EC import AtlasOEM_EC
import time
from tkinter import messagebox
global fullscreen
from PIL import ImageTk,Image
from tkinter import *
global ph_HIGH
global ph_LOW
import time
import board
import digitalio
import adafruit_max31865
import os
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import Tk, Canvas, Frame, BOTH
#from tkinter.messagebox import showinfo
import time
import threading
from AtlasOEM_PH import AtlasOEM_PH
from AtlasOEM_EC import AtlasOEM_EC
import time
import time
import board
import digitalio
import adafruit_max31865
import os
import datetime as dt
from pymodbus.server.sync import StartTcpServer, ModbusTcpServer
from AtlasOEM_PH import AtlasOEM_PH
import time
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from twisted.internet.task import LoopingCall
from twisted.internet import reactor
import threading
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import Read_PH_OEM
PHT = 0
ECT = 0
global number1
#number1 = 10
number = 0
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number10 =0
ec_val = 0
ph_val = 0
#var10 = 0
GPIO.setwarnings(False)
PH_HIGH = 4
PH_LOW = 17
EC_HIGH = 27
EC_LOW = 22
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.output(EC_HIGH, GPIO.HIGH)
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs)
def helloCallBack1():
    import Read_PH_OEM
# Create figure for plotting
    PHTrend = plt.figure()
    ax = PHTrend.add_subplot(1, 1, 1)
    xs = []
    ys = []
# Initialize communication with TMP102

# This function is called periodically from FuncAnimation
    def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
        PH = round(Read_PH_OEM.main(), 2)

    # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(PH)

    # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

    # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)
        plt.ylim(0,14)
        plt.plot(xs, ys, marker='o', linestyle='--', color='g')
    # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('PH over Time')
        plt.ylabel('PH')

# Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(PHTrend, animate, fargs=(xs, ys), interval=1000)
    plt
    plt.show()
    
def helloCallBack2():
    import Read_EC_OEM
    PHTrend = plt.figure()
    ax = PHTrend.add_subplot(1, 1, 1)
    xs = []
    ys = []
# Initialize communication with TMP102

# This function is called periodically from FuncAnimation
    def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
        PH = round(Read_EC_OEM.main(), 2)

    # Add x and y to lists
        xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(PH)

    # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]

    # Draw x and y lists
        ax.clear()
        ax.plot(xs, ys)
        plt.ylim(0,5000)
        plt.plot(xs, ys, marker='o', linestyle='--', color='g')
    # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('EC over Time')
        plt.ylabel('EC')

# Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(PHTrend, animate, fargs=(xs, ys), interval=1000)
    plt.show()

def helloCallBack3():
    channel1 = 4
    channel2 = 17
    channel3 = 27
    channel4 = 22

    GPIO.setup(channel1, GPIO.OUT)
    GPIO.output(channel1, GPIO.LOW)

    GPIO.setup(channel2, GPIO.OUT)
    GPIO.output(channel2, GPIO.LOW)

    GPIO.setup(channel3, GPIO.OUT)
    GPIO.output(channel3, GPIO.LOW)

    GPIO.setup(channel4, GPIO.OUT)
    GPIO.output(channel4, GPIO.LOW)

    #logging.basicConfig()
    #log = logging.getLogger()
    #log.setLevel(logging.DEBUG)


    def run_server():
    # ----------------------------------------------------------------------- #
    # initialize your data store
    # ----------------------------------------------------------------------- #
    #   di=block, co=block, hr=block, ir=block
    #   block = ModbusSequentialDataBlock(0x00, [123]*0x20)
    #   store = ModbusSlaveContext(hr=block)
        block1 = ModbusSequentialDataBlock(0x00, [100] * 0x0F)
        #block2 = ModbusSequentialDataBlock(0x02, [323] * 0x1F)
        block2 = ModbusSequentialDataBlock(0x00, [1] * 0x04),
        store2 = ModbusSlaveContext(hr=block1, di=block2)
            
        slaves = {
        0x02: store2,
        }

        context = ModbusServerContext(slaves=slaves, single=False)

    #   print(block1.values)
    #   print(block2.values)

    # ----------------------------------------------------------------------- #
    # initialize the server information
    # ----------------------------------------------------------------------- #
    # If you don't set this or any fields, they are defaulted to empty strings.
    # ----------------------------------------------------------------------- #
        identity = ModbusDeviceIdentification()
        identity.VendorName = 'Pymodbus'
        identity.ProductCode = 'PM'
        identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
        identity.ProductName = 'Pymodbus Server'
        identity.ModelName = 'Pymodbus Server'


    # ----------------------------------------------------------------------- #
    # run the server you want
    # ----------------------------------------------------------------------- #
    # Tcp:
    # server = StartTcpServer(context, identity=identity, address=('0.0.0.0', 255))

    # start server in a separate thread so that is not blocking
    # server.start_server()

    # to access the blocks for slave 1
    # store_1=server.context[1]

    # to read from the block
    # print("------")
    # print(store_1.getValues(4,0,32))

    # to write to the block
    # store_1.setValues(0x0F, 0, [111, 121, 122, 123, 124])
    # Type-2 Implementationt
        interval = 2
    # loop = LoopingCall(f=updatevalues, a=(context,))
    # loop.start(time, now=True)
        server = ModbusTcpServer(context, identity=identity,
                            address=('0.0.0.0', 5061))
        t = threading.Thread(target=server.serve_forever, daemon=True)
        t.start()
            
    #q = threading.Thread(target=updatevalues, daemon=True)
    #q.start()
    #z = threading.Thread(target=run_server, daemon=True)
    #z.start()

        loop = LoopingCall(f=updatevalues, a=server)
        loop.start(interval, now=True)
        reactor.run()
        

        
    def updatevalues(a):
        from AtlasOEM_PH import AtlasOEM_PH
        from AtlasOEM_EC import AtlasOEM_EC
        global EC_reading1
        global pH_reading1
        global ECread
        global pHread
        PH = AtlasOEM_PH() # create an OEM PH object
        EC = AtlasOEM_EC() # create an OEM EC object
    #DO = AtlasOEM_DO(name = "DO") # create an OEM DO object
    
         # tell the circuits to start taking readings
        
    #DO.write_active_hibernate(1)
        def read_temp():
            
            #global temp
        # Read temperature.
            tempraw = sensor.temperature
            temp = float("{0:.1f}".format(tempraw))
        # Print the value.
        #print("Temperature: {0:0.1f}C".format(temp))
        # Delay for a second.
            #time.sleep(.5)
            return temp
    
       
        def ph_reading():
            PH.write_active_hibernate(1) # tell the circuit to start taking readings
            if PH.read_new_reading_available():              # if we have a new reading
                pH_reading1 = PH.read_PH_reading()
                #if(pH_reading1 > 14):
                    #pH_reading1 = 6.5
                #print("OEM pH reading: " + str(pH_reading1))
                #print("OEM pH reading: " + str(format_floatpH))  # print the reading
                PH.write_new_reading_available(0)   # then clear the new reading register
                #return pH_reading1
                return pH_reading1
                
            else:
            #print("waiting")
                time.sleep(2)       
    
        # return the custom function without calling it, so we can call it when we want readings
        def EC_reading():
            
            EC.write_active_hibernate(1)
            if EC.read_new_reading_available():
                EC_reading1 = EC.read_temperature_compensation()
                #print(" OEM TEMP(Default) COMP: " + str(EC_reading1))
                #time.sleep(5)
                tempraw = sensor.temperature
                temp = float("{0:.0f}".format(tempraw))
                #print(temp)
                EC.write_temperature_compensation(temp)
                EC_reading3 = EC.read_temperature_confirmation
                #print(" OEM Temp Confirm: " + str(EC_reading3))
                EC_reading4 = EC.read_EC_reading()
                #if(EC_reading4 > 5000):
                    #EC_reading4 = 1500
                #print(" OEM EC Reading: " + str(EC_reading4))
                #time.sleep(5)    
                #EC_reading5 = EC.read_TDS_reading()
                #print(" OEM TDS Reading " + str(EC_reading5))
                #time.sleep(5)    
                #EC_reading5 = EC.read_salinitiy_reading()# if we have a new reading
                #print(" OEM Salinity Reading " + str(EC_reading5))
                #time.sleep(5)
                
                
                
                
                #Tempcomp = EC.read_temperature_confirmation()
                #EC.read_TDS_reading()
                #print(" OEM TEMP COMP: " + str(Tempcomp))
            
                #print("OEM EC reading: " + str(EC_reading4))  # print the reading
                EC.write_new_reading_available(0)
                #return EC_reading1
                return EC_reading4
            else:
            #print("waiting")
                time.sleep(2)       
    
        
        
        while True:
        
            ec_val = EC_reading()
            time.sleep(1)
            ph_val = ph_reading()
            time.sleep(1)
            temp_val=read_temp()
            time.sleep(10)     
            
            var2.set("{0:.2f}".format(ph_val))
            var1.set("{0:.0f}".format(ec_val))
            var20.set("{}".format(temp_val))
            
            ph_val1 = float("{0:.2f}".format(ph_val))
            ph_val2 = ph_val1 * 100
            ph_val3 = int(ph_val2)
            #print(ph_val3)
            
            ec_val1 = round(ec_val)
            #print(ec_val1)
            
            temp_val1 = round(temp_val)
            #print(temp_val1)
            
            print("------------START----------")
            cfuncode = 1
            rfuncode = 3
            wfuncode = 16
            slave_id = 0x02
            address = 0x00
        #address1 = 0x01
            contxt = a.context[slave_id]
            values = contxt.getValues(3, address, count=10)
            #values1 = contxt.getValues(1, address, count=10)
            print(values)
            #DI1 = GPIO.input(channel1)
            #DI2 = GPIO.input(channel2)
            #DI3 = GPIO.input(channel3)
            #DI4 = GPIO.input(channel4)
        
        
            #contxt.setValues(1, 0x00, DI1)
            #contxt.setValues(1, 0x01, DI2)
            #contxt.setValues(1, 0x02, DI3)
            #contxt.setValues(1, 0x03, DI4)
            contxt.setValues(3, 0x00, ph_val3)
            contxt.setValues(3, 0x01, ec_val1)
            contxt.setValues(3, 0x02, temp_val1)
            print("-------------END-------------")

    if __name__ == "__main__":
        while True:
            run_server()
            updatevalues()
            #time.sleep(10)
    


def submit(number10):
    
    number2=numbr2.get()
    number10 = int(number2)
    print(number10)
    
        
        
        
def Cal_4_Mode(var3):
    print("Entering CAL 4.0 Mode")
   # var3.set("Please DIP the PH Probe in PH 4.0 Buffer Solution ")
    #var3.set("Entering CAL 4.0 Mode")
    PH = AtlasOEM_PH() # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking readings

            # high again when it acquires a new reading
            
    PH.read_calibration_data()
   
    PH.write_calibration_request(0)
    PH.write_calibration_data(4.00)
    messagebox.showinfo("Calibration 4.0","Please clean the sensor probe and put it in pH 4 Calibration solution")
    #PH.write_calibration_request(0)
    time.sleep(10)
            #PH.write_calibration_request(3)
            #PH.write_calibration_request(2)
            #PH.write_calibration_request(0)
            #PH.read_calibration_confirm()
            #time.sleep(1)
    messagebox.showwarning("Calibration 4.0 in Progress", "Calibration in progress Please Wait for 10 seconds...")
    time.sleep(10)
    
            #PH.write_calibration_request(2)
    pH_ReadCal = PH.read_calibration_confirm()
    pH_CalData = PH.read_calibration_data()
                #return self.read_32(0x08)/1000.0
    print("OEM pH CAL reading: " + str(pH_CalData))
    print("OEM pH CALCONF reading: " + str(pH_ReadCal))
    tk.messagebox.showinfo("Calibration 4.0 Completed","Sensor Calibrated Sucessfully")
    #var3.set("Successfully Calibated LOW POINT PH 4.0")
    
def Cal_7_Mode(var4):
    print("Entering CAL 7.0 Mode")
    #var4.set("Please DIP the PH Probe in PH 7.0 Buffer Solution")
    PH = AtlasOEM_PH() # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking readings

    
    PH.read_calibration_data()
    
    PH.write_calibration_request(1)
    PH.write_calibration_data(7.00)
    messagebox.showinfo("Calibration 7.0","Please clean the sensor probe and put it in pH 7 Calibration solution")
    #PH.write_calibration_request(1)
    time.sleep(10)
            #PH.write_calibration_request(2)
            #PH.write_calibration_request(0)
            #PH.read_calibration_confirm()
            #time.sleep(1)
    messagebox.showwarning("Calibration 7.0","Calibration in progress Please Wait for 10 seconds...")
    time.sleep(10)
            #PH.write_calibration_request(2)
    pH_ReadCal = PH.read_calibration_confirm()
    pH_CalData = PH.read_calibration_data()
    #return self.read_32(0x08)/1000.0
    print("OEM pH CAL reading: " + str(pH_CalData))
    print("OEM pH CALCONF reading: " + str(pH_ReadCal))
    tk.messagebox.showinfo("Calibration 7.0 Completed","Sensor Calibrated Sucessfully")
    #var3.set("Successfully Calibated MID POINT PH 7.0")
    
def Cal_10_Mode(var5):
    print("Entering CAL 10.0 Mode")
    #var5.set("Please DIP the PH Probe in PH 10.0 Buffer Solution")
    PH = AtlasOEM_PH() # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking reading
            
    PH.read_calibration_data()
   
    PH.write_calibration_request(2)
    PH.write_calibration_data(10.00)
    messagebox.showinfo("Calibration 10.0","Please clean the sensor probe and put it in pH 7 Calibration solution")
    #PH.write_calibration_request(1)
    time.sleep(10)
    #PH.write_calibration_request(2)
            #PH.write_calibration_request(2)
            #PH.write_calibration_request(0)
            #PH.read_calibration_confirm()
            #time.sleep(1)
    messagebox.showwarning("Calibration 10.0","Calibration in progress Please Wait for 10 seconds....")
    time.sleep(10)
            #PH.write_calibration_request(2)
    pH_ReadCal = PH.read_calibration_confirm()
    pH_CalData = PH.read_calibration_data()
                #return self.read_32(0x08)/1000.0
    print("OEM pH CAL reading: " + str(pH_CalData))
    print("OEM pH CALCONF reading: " + str(pH_ReadCal))
    tk.messagebox.showinfo("Calibration 10.0","Sensor Calibrated Sucessfully")
    #var5.set("Successfully Calibated MID POINT PH 10.0")
def Cal_EC_Mode(var6):
    print("Entering CAL EC Mode")
    EC = AtlasOEM_EC(name = "EC") # create an OEM EC object
    EC.write_active_hibernate(1)

    

    if EC.read_new_reading_available():   # if we have a new reading
                EC.write_new_reading_available(0)  # then clear the new reading register    # then clear the new reading register 
                EC.read_calibration_data()
                EC_CalData = EC.read_calibration_data()
                print("OEM EC CAL reading: " + str(EC_CalData))
                EC.write_calibration_data(1413)
                EC.write_calibration_request(3)
                messagebox.showinfo("Calibration 10.0","Please clean the sensor probe and put it in pH 7 Calibration solution")
    #PH.write_calibration_request(1)
                time.sleep(10)
                #PH.write_calibration_request(2)
                #PH.write_calibration_request(0)
                #PH.read_calibration_confirm()
                messagebox.showwarning("Calibration EC 1413","Calibration in progress Please Wait for 10 seconds...")
                #time.sleep(1)
                time.sleep(10)
                #PH.write_calibration_request(2)
                EC_ReadCal = EC.read_calibration_confirm()
                
                print("OEM EC CALCONF reading: " + str(EC_ReadCal))
                tk.messagebox.showinfo("Calibration EC","Sensor Calibrated Sucessfully")
                #var6.set("Successfully Calibated EC 1413")
def Cal_DeletePH_Mode():
    PH = AtlasOEM_PH() # create an OEM PH object

    PH.write_active_hibernate(1) # tell the circuit to start taking readings

            # high again when it acquires a new reading
            
    PH.read_calibration_data()
    
    PH.write_calibration_request(0)
    PH.write_calibration_data(0)
            #PH.write_calibration_request(3)
            #PH.write_calibration_request(2)
            #PH.write_calibration_request(0)
            #PH.read_calibration_confirm()
            #time.sleep(1)
    time.sleep(5)
            #PH.write_calibration_request(2)
    pH_ReadCal = PH.read_calibration_confirm()
    pH_CalData = PH.read_calibration_data()
                #return self.read_32(0x08)/1000.0
    print("OEM pH CAL reading: " + str(pH_CalData))
    print("OEM pH CALCONF reading: " + str(pH_ReadCal))
    


    
def PH_plus():
    global number
    maxN = 14
    number += 0.5
    number = min(maxN, number)
    numbr.set(text=number)
    print(number)

def PH_minus():
    global number
    minN = 0
    number -= 0.5
    number = max(minN, number)
    numbr.set(text=number)
    print(number)
    
def PH_plus1():
    global number1
    maxN = 14
    number1 += 0.5
    number1 = min(maxN, number1)
    label6.config(text=number1)
    print(number1)

def PH_minus1():
    global number1
    minN = 0
    number1 -= 0.5
    number1 = max(minN, number1)
    label6.config(text=number1)
    print(number1)
    
def EC_plus():
    global number2
    maxN = 5000
    number2 += 10
    number2 = min(maxN, number2)
    numbr2.set(text=number2)
    print(number2)

def EC_minus():
    global number2
    minN = 0
    number2 -= 10
    number2 = max(minN, number2)
    numbr2.set(text=number2)
    print(number2)
    
def EC_plus1():
    global number3
    maxN = 5000
    number3 += 0
    number3 = min(maxN, number3)
    label8.config(text=number3)
    print(number3)

def EC_minus1():
    global number3
    minN = 0
    number3 -= 0
    number3 = max(minN, number3)
    label8.config(text=number3)
    print(number3)

def start_Cal4_Mode(var3):
    t = threading.Thread(target=Cal_4_Mode, args=(var3,))
    t.start()
    
def start_Cal7_Mode(var4):
    t = threading.Thread(target=Cal_7_Mode, args=(var4,))
    t.start()
    
def start_Cal10_Mode(var5):
    t = threading.Thread(target=Cal_10_Mode, args=(var5,))
    t.start()
    
def start_CalEC_Mode(var6):
    t = threading.Thread(target=Cal_EC_Mode, args=(var6,))
    t.start()
def start_CalDeletePH_Mode(var7):
    t = threading.Thread(target=Cal_DeletePH_Mode, args=(var7,))
    t.start()

#Thread(target = loop2).terminate()    
# create the thread
#task = threading.Thread(target=read_sensor, daemon=True)
task1 = threading.Thread(target=helloCallBack3, daemon=True)
#task2 = threading.Thread(target=submit1, daemon=True)
#task2.start()
#task.start()
task1.start()
root = tk.Tk()
from Preload import *
##root.geometry('800x400')
#bg = PhotoImage(file = "farmfluence-Logo.png")
#canvas1 = Canvas(root, width = 800,
                 #height = 450)
#canvas1.grid(row=0,column=1)
#canvas1.pack(fill=Tkinter.BOTH)
  
# Display image
#canvas1.create_image(0, 0, image = bg, anchor = "nw")
  
# Add Text
#canvas1.create_text( 200, 250, text = "Welcome")
#root.geometry("1024x800")
##root.title("PH EC Controller")
#bg = PhotoImage(file ="farmfluence-Logo.png")
var2 = tk.StringVar()#PH
var1 = tk.StringVar()#EC
var20 = tk.StringVar() #Temp
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()
var6 = tk.StringVar()
numbr=tk.StringVar()
numbr2=tk.StringVar()
numbr3=tk.StringVar()
numbr4=tk.StringVar()



##label = tk.Label(root, text=number, width=5, height=2, font=('calibri', 15, 'bold'))
##label.grid(row=3,column=11)
##label3 = tk.Label(root, text="PH HIGH", width=10, height=2, font=('calibri', 12, 'bold'))
##label3.grid(row=2,column=11)
##label4 = tk.Label(root, text="Thresholds", width=10, height=2, font=('calibri', 15, 'bold'))
##label4.grid(row=1,column=12)
##label5 = tk.Label(root, text="PH LOW", width=10, height=2, font=('calibri', 12, 'bold'))
##label5.grid(row=5,column=11)
##label6 = tk.Label(root, text=number1, width=5, height=2, font=('calibri', 15, 'bold'))
##label6.grid(row=6,column=11)
##label7 = tk.Label(root, text=number2, width=5, height=2, font=('calibri', 15, 'bold'))
##label7.grid(row=3,column=12)
##label8 = tk.Label(root, text=number3, width=5, height=2, font=('calibri', 15, 'bold'))
##label8.grid(row=6,column=12)
##label5 = tk.Label(root, text="EC HIGH", width=10, height=2, font=('calibri', 12, 'bold'))
##label5.grid(row=2,column=12)
##label5 = tk.Label(root, text="EC LOW", width=10, height=2, font=('calibri', 12, 'bold'))
##label5.grid(row=5,column=12)
###label = tk.Label(root, text="PH_HIGH Input")
###label.grid(row=4,column=10)
##b = tk.Button(root, text="Cal 4.0", width=8, height=1, bg="black", fg = "white",font=("calibri",14), command=lambda: start_Cal4_Mode(var3))
##b.grid(row=2,column=0)
##c = tk.Button(root, text="Cal 7.0", width=8, height=1, bg="black", fg = "white",font=("calibri",14), command=lambda: start_Cal7_Mode(var4))
##c.grid(row=1,column=0)
##d = tk.Button(root, text="Cal 10.0", width=8, height=1, bg="black", fg = "white",font=("calibri",14), command=lambda: start_Cal10_Mode(var5))
##d.grid(row=3,column=0)
##e = tk.Button(root, text="Cal  EC", width=8, height=1, bg="black", fg = "white",font=("calibri",14), command=lambda: start_CalEC_Mode(var6))
##e.grid(row=4,column=0)
##b1=tk.Button(root, text="Trend PH",bg="black", fg = "white",font=("calibri",14),command=helloCallBack1)
##b1.grid(row=5, column=0)
##b2=tk.Button(root, text="Trend EC",bg="black", fg = "white",font=("calibri",14),command=helloCallBack2)
##b2.grid(row=6, column=0)
###b3=tk.Button(frame, text="Trend Temperature", font=dfont,bg="white",command=animate)
###b3.grid(row=28, column=2, padx=5, pady=5)
##PH_plus = tk.Button(root, text="PH +", bg="black", fg = "white", command=PH_plus, font=("calibri", 12))
##PH_plus.grid(row=4,column=10)
##PH_minus = tk.Button(root, text="PH -", bg="black", fg = "white", command=PH_minus, font=("calibri", 12))
##PH_minus.grid(row=4,column=11)
##
##PH_plus1 = tk.Button(root, text="PH +", bg="black", fg = "white", command=PH_plus1, font=("calibri", 12))
##PH_plus1.grid(row=7,column=10)
##PH_minus1 = tk.Button(root, text="PH -", bg="black", fg = "white", command=PH_minus1, font=("calibri", 12))
##PH_minus1.grid(row=7,column=11)
##
##EC_plus = tk.Button(root, text="EC +", bg="black", fg = "white", command=EC_plus, font=("calibri", 12))
##EC_plus.grid(row=4,column=12)
##EC_minus = tk.Button(root, text="EC -", bg="black", fg = "white", command=EC_minus, font=("calibri", 12))
##EC_minus.grid(row=4,column=13)
##
##EC_plus1 = tk.Button(root, text="EC +", bg="black", fg = "white", command=EC_plus1, font=("calibri", 12))
##EC_plus1.grid(row=7,column=12)
##EC_minus1 = tk.Button(root, text="EC -", bg="black", fg = "white", command=EC_minus1, font=("calibri", 12))
##EC_minus1.grid(row=7,column=13)
#################################
#################################
#################################
class MainScreen:
    def __init__(self, win):
        load_C = Label(root, bg="#eaebef", image=loadingScreen,height=450, width=800)
        load_C.image=mainScreen
        load_C.place(x=0,y=0)
        root.after(2000,self.main_Screen)
    def main_Screen(self):
        main_C = Label(root, bg="#eaebef", image=mainScreen,height=450, width=800)
        main_C.image=mainScreen
        main_C.place(x=0,y=0)

        lbl = tk.Label(main_C, textvariable=var2, width=5,bg='#d6dbbd',anchor='center', height=1, font=('calibri', 20, 'bold')) ##PH Display
        lbl.place(x=120,y=180)
        lbl1 = tk.Label(main_C, textvariable=var1, width=10,bg='#d6dbbd', height=1,anchor='center', font=('calibri', 20, 'bold'))##EC Display
        lbl1.place(x=320,y=180)
        lbl2 = tk.Label(main_C, textvariable=var20, width=5,bg='#d6dbbd', height=1,anchor='center', font=('calibri', 20, 'bold'))## Temp Display
        lbl2.place(x=590,y=180)
        
        
        
        menu_Btn=Button(main_C,image=menuBtn,command=self.menu_Screen,relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        menu_Btn.place(x=20,y=380)
    def menu_Screen(self):
        def delete(): 
           entry_PH.delete(0, 'end')
           entry_PHLOW.delete(0, 'end')
           entry_EC.delete(0, 'end')
           entry_ECLOW.delete(0, 'end')
        def backspace():#Delete one digit at a time into perticular entry field
            pass
        '''def btn_click(item):
            global expression
            expression = expression + str(item)
            input_text.set(expression)'''
        """def delete1(): 
           entry_PHLOW.delete(0, 'end')
        def delete2(): 
           entry_EC.delete(0, 'end')
        def delete3(): 
           entry_ECLOW.delete(0, 'end')"""
        def KeyPress(i):
            from pynput.keyboard import Key, Controller
            keyboard=Controller()
            keyboard.press(str(i))
            keyboard.release(str(i))
            
        
        menu_C = Label(root, bg="#eaebef", image=menuScreen,height=450, width=800)
        menu_C.image=mainScreen
        menu_C.place(x=0,y=0)
        lbl4 = Label(root, text="PH HIGH", width=11,bg='#eaebef', height=1,anchor='center', font=('calibri', 20, 'bold'))## Temp Display
        lbl4.place(x=20,y=100)
        
        lbl5 = Label(root, text="EC HIGH", width=11,bg='#eaebef', height=1,anchor='center', font=('calibri', 20, 'bold'))## Temp Display
        lbl5.place(x=200,y=100)
        
        lbl6 = Label(root, text="PH LOW", width=11,bg='#eaebef', height=1,anchor='center', font=('calibri', 20, 'bold'))## Temp Display
        lbl6.place(x=20,y=200)
        
        lbl7 = Label(root, text="EC LOW", width=11,bg='#eaebef', height=1,anchor='center', font=('calibri', 20, 'bold'))## Temp Display
        lbl7.place(x=200,y=200)
        #highPH_Btn=Button(menu_C,image=highBtn,command=PH_plus,relief=FLAT,#PH_PLUS
                        #fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        #highPH_Btn.place(x=20,y=100)
        entry_PH = Entry (menu_C,textvariable=numbr,relief=SUNKEN,font=('calibri', 20, 'bold'),highlightbackground='BLACK',
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=1,justify=CENTER)
        entry_PH.place(x=20,y=140,height=45,width=160)
        
        entry_PHLOW = Entry (menu_C,textvariable=numbr3,relief=SUNKEN,font=('calibri', 20, 'bold'),highlightbackground='BLACK',
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=1,justify=CENTER)
        entry_PHLOW.place(x=20,y=240,height=45,width=160)
        #lowPH_Btn=Button(menu_C,image=lowBtn,command=PH_minus,relief=FLAT,
                        #fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)##PH_MINUS
        #lowPH_Btn.place(x=20,y=240)
        cal4_Btn=Button(menu_C,image=cal4Btn,command=lambda: start_Cal4_Mode(var3),relief=FLAT,##CAL 4
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        cal4_Btn.place(x=380,y=160)
        cal7_Btn=Button(menu_C,image=cal7Btn,command=lambda: start_Cal7_Mode(var4),relief=FLAT,##CAL 7
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        cal7_Btn.place(x=380,y=100)
        
        cal10_Btn=Button(menu_C,image=emptBtn,command=lambda: start_Cal10_Mode(var5),relief=FLAT,
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        cal10_Btn.place(x=380,y=220)

        #highEC_Btn=Button(menu_C,image=highBtn,command=EC_plus,relief=FLAT, ##EC_PLUS
                        #fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        #highEC_Btn.place(x=200,y=100)
        entry_EC= Entry (menu_C,textvariable=numbr2,relief=SUNKEN,font=('calibri', 20, 'bold'),highlightbackground='BLACK',
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=1,justify=CENTER)
        
        entry_EC.place(x=200,y=140,height=45,width=160)
        
        entry_ECLOW= Entry (menu_C,textvariable=numbr4,relief=SUNKEN,font=('calibri', 20, 'bold'),highlightbackground='BLACK',
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=1,justify=CENTER)
        
        entry_ECLOW.place(x=200,y=240,height=45,width=160)
        #lowEC_Btn=Button(menu_C,image=lowBtn,command=EC_minus,relief=FLAT, ## EC_MINUS
                        #fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        #lowEC_Btn.place(x=200,y=240)
        calEC_Btn=Button(menu_C,image=cal14Btn,command=lambda: start_CalEC_Mode(var6),relief=FLAT, ## Calculate EC
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        calEC_Btn.place(x=380,y=280)
        #empty_Btn=Button(menu_C,image=emptBtn,command=self.menu_Screen,relief=FLAT,  ##Back to main screen
                        #fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        #empty_Btn.place(x=200,y=380)

        #reset_Btn=Button(menu_C,image=resetBtn,command=self.menu_Screen,relief=FLAT,###Reset command here
                        #fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        #reset_Btn.place(x=380,y=100)
        #reboot_Btn=Button(menu_C,image=rebootBtn,relief=FLAT,###Reboot button, add your own command here
                        #fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        #reboot_Btn.place(x=380,y=170)
        #graph_Btn=Button(menu_C,image=menuBtn,command=helloCallBack1,relief=FLAT,###PH graph screen button
                        #fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
       # graph_Btn.place(x=380,y=240)
        empty_Btn2=Button(menu_C,image=lowBtn,command=self.main_Screen,relief=FLAT,  ###Back to main screen button
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=0)
        empty_Btn2.place(x=110,y=350)
        submit_btn=Button(menu_C,text="Submit",height=2, width=5,command=lambda: submit(number1),activebackground='medium orchid', ## Calculate EC
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=1)
        
        submit_btn.place(x=630,y=370)
        
        clear_btn=Button(menu_C,text="Clear",height=2, width=5,command=delete,activebackground='medium orchid', ## Calculate EC
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=1)
        clear_btn.place(x=700,y=370)
        button51=Button(menu_C,text=".",height=2, width=5,command=str("."),activebackground='medium orchid', ## Calculate EC
                        fg='BLACK',bg='#F7F7F7',bd=0,highlightthickness=0,borderwidth=1)
        button51.place(x=560,y=370)
        
        buttons=[0,0,0,0,0,0,0,0,0,0]
        frame = Frame(root)
        frame.place(x=560,y=100)
        a=0
        for j in range(3):
            for i in range(3):
                buttons[a]=Button(frame,text=str(a),bg='#eaebef',height=3,width=5,command=lambda j=a:KeyPress(j),activebackground='medium orchid')
                buttons[a].grid(column=i,row=j)
                a=a+1
                buttons[9]=Button(frame,text=str(9),width=22,bg='#eaebef',height=3,command=lambda j=a:KeyPress(j),activebackground='medium orchid')
                buttons[9].grid(column=0,row=4,columnspan=3)
                
    
mywin=MainScreen(root)
root.title('Budan Farms')
root.geometry("800x450+0+0")
#root.attributes("-fullscreen", True)
root.mainloop()

