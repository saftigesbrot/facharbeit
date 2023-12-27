import json
import random
import datetime
import time
from datetime import date, timedelta, datetime
from colorama import *
init(autoreset=True)

generatedData = []

# Mit Settings.json verbinden


def ProofSettings():
   
   # Überpüftt alle Einstellungen der settings.json Datei auf ihre Kompatibilität

   with open('settings.json','r') as file:
      obj = json.load(file)

   # Proof GeneralSettings
   global hurricaneProbability 
   number = obj['general-settings']['hurricane-probability']
   name = " Hurrikanwahrscheinlichkeit"
   
   ProofSettingsIntSupport(number, name)
   hurricaneProbability = number

   global hurricaneMultiplicator
   number = obj['general-settings']['hurricane-multiplicator']
   name = " Hurrikanmultiplikator"

   ProofSettingsIntSupport(number, name)
   hurricaneMultiplicator = number

   global generatedDataFactor
   number = obj['general-settings']['generate-data-factor']
   name = " Datengenerierungsfakor"

   ProofSettingsIntSupport(number, name)
   generatedDataFactor = number

   global generateDataSets
   number = obj['general-settings']['generated-data-sets']
   name = " Datengenerierungssätze"

   ProofSettingsIntSupport(number, name)
   generateDataSets = number

   # Proof Date
   global startDate
   date = obj['general-settings']['start-date']
   format = "%Y-%m-%d %H:%M:%S.%f"

   try:
      bool(datetime.strptime(date, format))
      print(Back.GREEN + " Datum erfolgreich geladen! ")
   except ValueError:
      print(Back.RED + " Datum konnten nicht gelanden werden! Exit Code 1 ")
      exit()
   startDate = date


   # Proof WindDirection
   global windDirection
   windDirections = obj['wind-direction']['wind-directions']
   windDirectionCounter = 0

   for Direction in windDirections:
      windDirectionCounter += 1
   
   if all(isinstance(Direction, str) for Direction in windDirections) == False:
      print(Back.RED + " Windrichtungsdaten konnten nicht gelanden werden! Exit Code 1 ")
   
   if windDirectionCounter == 16: 
      print(Back.GREEN + " Windrichtungsdaten erfolgreich geladen! ")
   else: 
      print(Back.RED + " Windrichtungsdaten konnten nicht gelanden werden! Exit Code 1 ")
      exit()
   
   windDirection = windDirections

   # Proof Temperature
   global temperatureMinimal
   global temperatureMaximum

   minimal = obj['temperature']['minimal']
   maximum = obj['temperature']['maximum']

   name = " Temperaturdaten"
   ProofSettingsTypeSupporter(minimal, maximum, name)

   temperatureMinimal = minimal
   temperatureMaximum = maximum

   # Proof WindSpeed
   global windSpeedMinimal 
   global windSpeedMaximum

   minimal= obj['wind-speed']['minimal']
   maximum = obj['wind-speed']['maximum']

   name = " Windgeschwindigkeitsdaten"
   ProofSettingsTypeSupporter(minimal, maximum, name)

   windSpeedMinimal = minimal
   windSpeedMaximum = maximum

   # Proof AirPressure
   global airPressureMinimal
   global airPressureMaximum

   minimal = obj['air-pressure']['minimal']
   maximum = obj['air-pressure']['maximum']

   name = " Luftdruckdaten"
   ProofSettingsTypeSupporter(minimal, maximum, name)

   airPressureMinimal = minimal
   airPressureMaximum = maximum


def ProofSettingsIntSupport(number, name):
   if type(number) == int and (number == 0 or number > 0):
      Outprint = name + " erfolgreich gelanden! "
      print(Back.GREEN + Outprint)
   else:
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit()


def ProofSettingsTypeSupporter(minimal, maximum, name):
   if type(minimal and maximum) == int and maximum > minimal: 
      Outprint = name + " erfolgreich geladen! "
      print(Back.GREEN + Outprint)
   else: 
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit() 



def MainGeneration():

   # Überprüft die Einstellungen und bestimmt die Variablen
   ProofSettings()

   # Übernimmt die Variablen
   global generateDataSets
   global hurricaneProbability
   global hurricaneMultiplicator
   global generatedDataFactor

   global StringifyNewTime

   while generateDataSets != generatedDataFactor:
      hurricaneChance = round(random.uniform(0,100))

      if hurricaneChance > hurricaneProbability:
         hurricaneBoolean = False
         DataGeneration(hurricaneBoolean)

      elif hurricaneChance == hurricaneProbability or hurricaneChance < hurricaneProbability:
         hurricaneBoolean = True
         DataGeneration(hurricaneBoolean)

      generateDataSets += 1
   SaveData()

def DataGeneration(hurricaneBoolean):
 
   # Generiere das Datum
   GenerateDate()
   global Time

   # Generiere die Windrichtung 
   GenerateWindDirection()

   # Generiere die Temperatur
   GenerateTemperature()
   global Temperature

   # Generiere die Windgeschwindgikeit 
   GenerateWindSpeed()
   global WindSpeed

   # Generiere den Luftdruck
   GenerateAirPressure()
   global AirPressure

   generatedData.append(
      {
        "Time": Time,
        "Wind-Direction": "NNO",
        "Temperature": Temperature,
        "Wind-Speed": WindSpeed,
        "Air-Pressure": AirPressure
      }
   )



def GenerateDate():

   global startDate
   global generateDataSets

   if generateDataSets == 0:
       lastGeneratedTime = startDate
   else:
       lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
       lastGeneratedTime = generatedData[lastGeneratedLen]["Time"]

        # Beachten, dass durch neue Daten dies nicht mehr funktioniert, da die Time in der Json verrückt wird
    
   NewTime = datetime.strptime(lastGeneratedTime, "%Y-%m-%d %H:%M:%S.%f") + timedelta(hours=1)
   
   global Time
   Time = str(NewTime)

   print(Back.CYAN + " generateWindDirection ")


def GenerateWindDirection():
   # Getting Data form settings.json 
   global windDirection
   global hurricaneMultiplicator
   global generateDataSets
   
   print(Back.BLUE + " generateWindDirection ")

   # Nur einmal bestimmen, damit die richtung nicht dauerhaft wechselt

def GenerateTemperature():
   # Getting Data from settings.json
   global temperatureMinimal
   global temperatureMaximum
   global hurricaneMultiplicator

   if generateDataSets == 0:
       lastGeneratedTemperature = round(random.uniform(temperatureMinimal,temperatureMaximum))

   else:
       lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
       lastGeneratedTemperature = generatedData[lastGeneratedLen]["Temperature"]

       lastGeneratedTemperatureMinimal = lastGeneratedTemperature - 2 
       lastGeneratedTemperatureMaximum = lastGeneratedTemperature + 2 

       if temperatureMinimal <= lastGeneratedTemperatureMinimal or temperatureMaximum >= lastGeneratedTemperatureMaximum:
         lastGeneratedTemperature = round(random.uniform(lastGeneratedTemperatureMinimal, lastGeneratedTemperatureMaximum))


   global Temperature
   Temperature = lastGeneratedTemperature


   print(Back.RED + " generateTemperatur ")

def GenerateWindSpeed():
   global windSpeedMinimal
   global windSpeedMaximum
   global hurricaneMultiplicator
   global generateDataSets

   if generateDataSets == 0:
       lastGeneratedWindSpeed = round(random.uniform(windSpeedMinimal,windSpeedMaximum))

   else:
       lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
       lastGeneratedWindSpeed = generatedData[lastGeneratedLen]["Wind-Speed"]

       lastGeneratedWindSpeedMinimal = lastGeneratedWindSpeed - 20
       lastGeneratedWindSpeedMaximum = lastGeneratedWindSpeed + 20

       if windSpeedMinimal <= lastGeneratedWindSpeedMinimal or windSpeedMaximum >= lastGeneratedWindSpeedMaximum:
         lastGeneratedWindSpeed = round(random.uniform(lastGeneratedWindSpeedMinimal, lastGeneratedWindSpeedMaximum))


   global WindSpeed
   WindSpeed = lastGeneratedWindSpeed


   print(Back.YELLOW + " generateWindSpeed ")

def GenerateAirPressure():
   global airPressureMinimal
   global airPressureMaximum
   global hurricaneMultiplicator
   global generateDataSets


   if generateDataSets == 0:
       lastGeneratedAirPressure = round(random.uniform(airPressureMinimal,airPressureMaximum))

   else:
       lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
       lastGeneratedAirPressure = generatedData[lastGeneratedLen]["Air-Pressure"]

       lastGeneratedAirPressureMinimal = lastGeneratedAirPressure - 20
       lastGeneratedAirPressureMaximum = lastGeneratedAirPressure + 20

       if airPressureMinimal <= lastGeneratedAirPressureMinimal or airPressureMaximum >= lastGeneratedAirPressureMaximum:
         lastGeneratedAirPressure = round(random.uniform(lastGeneratedAirPressureMinimal, lastGeneratedAirPressureMaximum))


   global AirPressure
   AirPressure = lastGeneratedAirPressure

   print(Back.MAGENTA + " generateAirPressure ")

def SaveData():
    JSONData = json.dumps(generatedData,indent=4, separators=(',',': '))

    SavingFile = open("massDataGeneration.json", "w")
    SavingFile.write(JSONData)
    SavingFile.close()

MainGeneration()