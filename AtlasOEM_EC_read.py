from AtlasOEM_EC import AtlasOEM_EC
import time
Temp= 25
def main():
    while True:
        EC = AtlasOEM_EC() # create an OEM PH object

        EC.write_active_hibernate(1) # tell the circuit to start taking readings

    #while True:
        if EC.read_new_reading_available():
                #EC_reading1 = EC.read_temperature_compensation()
               ##### print(" OEM Temp Confirm: " + str(EC_reading3))
                EC_reading4 = EC.read_EC_reading()
                print(" OEM EC Reading: " + str(EC_reading4))
               #print(" OEM TDS Reading " + str(EC_reading5))
               # time.sleep(5)    
               # EC_reading5 = EC.read_salinitiy_reading()# if we have a new reading
               # print(" OEM Salinity Reading " + str(EC_reading5))
               # time.sleep(5)    
                EC.write_new_reading_available(0)   # then clear the new reading register
         
        else:
            #print("waiting")
            time.sleep(2)                      #if theres no reading, wait some time to not poll excessively
            
if __name__ == '__main__':
    main()
