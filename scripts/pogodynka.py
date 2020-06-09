from datetime import datetime
import bme280

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

def main():
    temperature, pressure, humidity = bme280.readBME280All()
    print("Temperatura: {0} C".format(round(temperature, 2)))
    print("Cisnienie: {0} hPa".format(round(pressure, 2)))
    print("Wilgotnosc: {0} %".format(round(humidity, 2)))

    add_to_html(temperature, pressure, humidity)

if __name__ == "__main__":
    main()
