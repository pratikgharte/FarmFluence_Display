from AtlasOEM_PH import AtlasOEM_PH
from AtlasOEM_EC import AtlasOEM_EC
import digitalio
import adafruit_max31865
import board
global pH_reading1
global ECread
global pHread
import board
import time 
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs)
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
        print("Temperature: {0:0.1f}C".format(temp))
        # Delay for a second.
            #time.sleep(.5)
        return temp
    
       
def ph_reading():
        PH.write_active_hibernate(1) # tell the circuit to start taking readings
        if PH.read_new_reading_available():              # if we have a new reading
            pH_reading1 = PH.read_PH_reading()
                #if(pH_reading1 > 14):
                    #pH_reading1 = 6.5
            print("OEM pH reading: " + str(pH_reading1))
                #print("OEM pH reading: " + str(format_floatpH))  # print the reading
            
            PH.write_new_reading_available(0)   # then clear the new reading register
                #return pH_reading1
            return pH_reading1
                
        else:
            #print("waiting")
            time.sleep(.5)       
    
        # return the custom function without calling it, so we can call it when we want readings
def EC_reading():
            
    #while True:
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
            print(" OEM EC Reading: " + str(EC_reading4))
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
                time.sleep(.5)       
    
        
        
while True:
        
            ec_val = EC_reading()
            time.sleep(1)
            ph_val = ph_reading()
            time.sleep(1)
            temp_val=read_temp()