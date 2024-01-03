import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

with open('light_sensor_pin.txt', 'r') as file:
    LIGHT_SENSOR_PIN = int(file.read())

LED_STRIP_PIN = 17

GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_STRIP_PIN, GPIO.OUT)

while True:
    with open('light_sensor_pin.txt', 'r') as file:
        light_level = int(file.read())

    with open('r.txt', 'r') as file_r:
        mode = int(file_r.read())

    if mode == 1:
        if light_level < 50:
            GPIO.output(LED_STRIP_PIN, GPIO.HIGH)  
            with open('result.txt', 'a') as file:
                file.write("LED лента включена (режим 1)\n")
        else:
            GPIO.output(LED_STRIP_PIN, GPIO.LOW) 
            with open('result.txt', 'a') as file:
                file.write("LED лента выключена\n")
    elif mode == 2:
        if light_level < 50:
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            time.sleep(10)  
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            time.sleep(10)  
            with open('result.txt', 'a') as file:
                file.write("LED лента включена (режим 2)\n")
        else:
            GPIO.output(LED_STRIP_PIN, GPIO.LOW)  
            with open('result.txt', 'a') as file:
                file.write("LED лента выключена\n")

    time.sleep(1)  

                
