from AtlasOEM_EC import AtlasOEM_EC
import time

def main(): 
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
                #PH.write_calibration_request(2)
                #PH.write_calibration_request(0)
                #PH.read_calibration_confirm()
                #messagebox.showinfo("Calibration EC 1413","Calibration in progress Please Wait")
                #time.sleep(1)
                time.sleep(10)
                #PH.write_calibration_request(2)
                EC_ReadCal = EC.read_calibration_confirm()
                
                print("OEM EC CALCONF reading: " + str(EC_ReadCal))
                #tk.messagebox.showinfo(title="Calibration EC",message="Sensor Calibrated Sucessfully")
                #var6.set("Successfully Calibated EC 1413")
            
            
                                
        
if __name__ == '__main__':
    main()

