import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LIGHT_SENSOR_PIN = 18
LED_STRIP_PIN = 17

GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)
GPIO.setup (LIGHT_STRIP_PIN, GPIO.OUT)

def check_light_level():
    if GPIO.input(LIGHT_SENSOR_PIN) == GPIO.LOW:
        return "dark"
    else:
        return "bright"

    try:
        while True:
            light_level=check_light_level()

            if light_level == "dark":
                GPIO.output(LED_STRIP_PIN, GPIO.HIGH)
            else:
                    GPIO.output(LED_STRIP_PIN, GPIO.LOW)
                    time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
                