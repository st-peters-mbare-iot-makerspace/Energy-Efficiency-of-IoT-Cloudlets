from time import sleep
import serial
import datetime

ser = serial.Serial('/dev/ttyACM0',19200)
while True:
  if (ser.inWaiting()):
     reading=ser.readline()
     if len(reading)>=52:
        reading=reading[:-2]
     
        now=datetime.datetime.now()
        reading=reading

        readingFile=open('/root/pythonscripts/arduinoreadings','w')
        readingFile.write(reading)
        readingFile.close()
     
        reading=reading+now.isoformat()+"\n"
        readingFile=open('/root/pythonscripts/arduinoreadingstime','a')
        readingFile.writelines(reading)
        readingFile.close()
     else:
        errFile=open('errors','a')
        errFile.write(str(len(reading)))
     sleep(15)
   
      
