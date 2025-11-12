from hal import hal_led as led
from hal import hal_input_switch as switch
import time
from time import sleep

def main():
    switch.init()
    led.init()
    while(1):
        if switch.read_slide_switch() == 1:#left
         led.set_output(0, 1)
         time.sleep(0.5)

         led.set_output(0, 0)
         time.sleep(0.5)

         led.set_output(0, 1)
         time.sleep(0.5)

         led.set_output(0, 0)
         time.sleep(0.5)
        elif switch.read_slide_switch() == 0:
         start_time = time.time() 
         while time.time() - start_time < 5:
            led.set_output(0,1)
            time.sleep(0.1)

            led.set_output(0, 0)
            time.sleep(0.1)
         while switch.read_slide_switch() == 0:
          led.set_output(0, 0)
          time.sleep(1)

if __name__ == "__main__":
    main()
