import webiopi
import datetime

GPIO = webiopi.GPIO

LIGHT = 17 # GPIO pin using BCM numbering
LUZAZUL = 17
HOUR_ON  = 8  # Turn Light ON at 08:00
HOUR_OFF = 18 # Turn Light OFF at 18:00
hora_on_azul = 8
hora_off_azul = 22
# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT, GPIO.OUT)
    #GPIO.setFunction(LUZAZUL, GPIO.OUT)
    
    # retrieve current datetime
    now = datetime.datetime.now()

    # test if we are between ON time and tun the light ON
    if ((now.hour >= HOUR_ON) and (now.hour < HOUR_OFF)):
        GPIO.digitalWrite(LIGHT, GPIO.HIGH)
    if ((now.hour >= hora_on_azul) and (now.hour < hora_off_azul)):
        GPIO.digitalWrite (LUZAZUL, GPIO.HIGH)
# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT, GPIO.HIGH) 
    if ((now.hour == hora_on_azul) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LUZAZUL) == GPIO.LOW):
            GPIO.digitalWrite(LUZAZUL, GPIO.HIGH)
    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT, GPIO.LOW)
    if ((now.hour == hora_off_azul) and (now.minute == 0) and (now.secon == 0)):
        if  (GPIO.digitalRead(LUZAZUL) == GPIO.HIGH):
            GPIO.digitalWrite(LUZAZUL, GPIO.LOW)
    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
    GPIO.digitalWrite(LUZAZUL, GPIO.LOW)
@webiopi.macro
def getLightHours():
    return "%d;%d;%d;%d" % (HOUR_ON, HOUR_OFF, hora_on_azul, hora_off_azul)
   
@webiopi.macro
def setLightHours(on, off):
    global HOUR_ON, HOUR_OFF
    HOUR_ON = int(on)
    HOUR_OFF = int(off)º
    return getLightHours()
