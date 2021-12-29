from AtlasOEM_PH import AtlasOEM_PH
import time
global pH_reading
def main():
    while True:
        PH = AtlasOEM_PH() # create an OEM PH object

        PH.write_active_hibernate(1) # tell the circuit to start taking readings

    #while True:
        if PH.read_new_reading_available():              # if we have a new reading
            pH_reading = PH.read_PH_reading()            # get it from the circuit
            #pH1 = float(pH_reading)
            #format_floatpH = "{:.1f}".format(pH1)
            
            print("OEM pH reading: " + str(pH_reading))  # print the reading
            PH.write_new_reading_available(0)   # then clear the new reading register
            #print(pH)
            #return pH_reading                                    # so the circuit can set the register
#             ph_val1 = float(pH_reading)
#             print(ph_val1)
#             phval2 = int(round(ph_val1))
#             print(phval2)
            
            
            
        else:
            #print("waiting")
            time.sleep(2)                      #if theres no reading, wait some time to not poll excessively
            
if __name__ == '__main__':
    main()