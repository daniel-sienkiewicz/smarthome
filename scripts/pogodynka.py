from datetime import datetime
import bme280
import RPi.GPIO as GPIO
import time

index_file = 'webpage/index.html'

def add_to_html(temperature, pressure, humidity):

    global index_file

    # Read in the file
    with open(index_file, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('{{temp}}', str(round(temperature, 2)))
    filedata = filedata.replace('{{cisnienie}}', str(round(pressure, 2)))
    filedata = filedata.replace('{{wilgotnosc}}', str(round(humidity, 2)))
    filedata = filedata.replace('{{data}}', str(datetime.now()))

    # Write the file out again
    with open(index_file, 'w') as file:
        file.write(filedata)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.HIGH)

def recovery():
    GPIO.output(21, GPIO.LOW)
    time.sleep(30)
    GPIO.output(21, GPIO.HIGH)

def main():
    temperature, pressure, humidity = bme280.readBME280All()
    print("Temperatura: {0} C".format(round(temperature, 2)))
    print("Cisnienie: {0} hPa".format(round(pressure, 2)))
    print("Wilgotnosc: {0} %".format(round(humidity, 2)))

    add_to_html(temperature, pressure, humidity)

if __name__ == "__main__":
    setup()
    try:
        main()
        GPIO.cleanup()
    except:
        recovery()
        main()
        GPIO.cleanup()
