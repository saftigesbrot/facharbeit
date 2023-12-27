import json
import random
import datetime
import time
from datetime import date, timedelta
from colorama import *
init(autoreset=True)

generatedDataFactor = 0
StartDate = "2023-04-23 15:18:28.044869"
generatedData = []
GeneratedDataSets = 0

# generatedData: Durch len(generatedData) kann die Anzahl der Tage welche bereits generiert wurde bestimmt werden

def MainGeneration():

   with open('settings.json','r') as file:
    obj = json.load(file)
   
   hurricaneProbability = obj['general-settings']['hurricane-probability']
   #try statt if/else

   if hurricaneProbability == 0 or hurricaneProbability > 0:
      print(Back.GREEN + " Daten erfolgreich geladen! ")
   else:
      print(Back.RED + " Daten konnten nicht gelanden werden! ")
      exit()

   # while GeneratedDataSets != generatedDataFactor:

    # Zufällige Wachrscheinlichkeit ob ein Hurrikan stattfindet oder nicht
    # Settings Document 

    # GenerateDate()
    # GenerateWindDirection()
    # GenerateTemperature()
    # GenerateWindSpeed()
    # GenerateAirPressure()

    # generatedData.append(StringifyNewTime)

    # GeneratedDataSets = GeneratedDataSets + 1
   
   SaveData()

def GenerateDate():

   if GeneratedDataSets == 0:
       lastGeneratedTime = StartDate
   else:
       lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
       lastGeneratedTime = generatedData[lastGeneratedLen]
        # Beachten, dass durch neue Daten dies nicht mehr funktioniert, da die Time in der Json verrückt wird
    
   NewTime = datetime.datetime.strptime(lastGeneratedTime, "%Y-%m-%d %H:%M:%S.%f") + timedelta(minutes=1)
   StringifyNewTime = str(NewTime)

def GenerateWindDirection():
   print(Back.BLUE + " GenerateWindDirection ")
   # Nur einmal bestimmen, damit die richtung nicht dauerhaft wechselt

def GenerateTemperature():
   print(Back.RED + " GenerateTemperatur ")
   # muss sich an der erste den vorherigen Temperaturen orientieren, um ein realisitisches

def GenerateWindSpeed():
   print(Back.YELLOW + " GenerateWindSpeed ")

def GenerateAirPressure():
   print(Back.MAGENTA + " GenerateAirPressure ")

def SaveData():
    JSONData = json.dumps(generatedData, indent=4)

    SavingFile = open("massDataGeneration.json", "w")
    SavingFile.write(JSONData)
    SavingFile.close()

MainGeneration()