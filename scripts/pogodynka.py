from datetime import datetime
import bme280

index_file = 'webpage/index.html'

def add_to_html(temperature, pressure, humidity):

    global index_file

    # Read in the file
    with open(index_file, 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('{{temp}}', temperature)
    filedata = filedata.replace('{{cisnienie}}', pressure)
    filedata = filedata.replace('{{wilgotnosc}}', humidity)
    filedata = filedata.replace('{{data}}', now.strftime("%d/%m/%Y %H:%M:%S"))

    # Write the file out again
    with open(index_file, 'w') as file:
        file.write(filedata)

def main():
    temperature, pressure, humidity = bme280.readBME280All()
    print "Temperatura: ", temperature, "C"
    print "Cisnienia: ", pressure, "hPa"
    print "Wilgotnosc: ", humidity, "%"

    add_to_html(temperature, pressure, humidity)

if __name__ == "__main__":
    main()
