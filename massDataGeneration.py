import json
import random
import datetime
import time
from datetime import date, timedelta, datetime
from colorama import *
init(autoreset=True)
import numpy as np
import sys
sys.setrecursionlimit(2000)

generatedData = []

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
      print(Fore.GREEN + " Datum erfolgreich geladen! \n")
   except ValueError:
      print(Back.RED + " Datum konnten nicht gelanden werden! Exit Code 1 ")
      exit()
   startDate = date

   global savingDataFile
   file = obj['general-settings']['saving-file']
   splittedFileName = file.split(".")

   if type(file) == str and splittedFileName.pop() == "json":
      Outprint = name + " erfolgreich gelanden! "
      print(Fore.GREEN + Outprint)
   else:
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit()
   savingDataFile = file


   # Proof WindDirection
   global windDirection
   windDirections = obj['wind-direction']['wind-directions']
   windDirectionCounter = 0

   for Direction in windDirections:
      windDirectionCounter += 1
   
   if all(isinstance(Direction, str) for Direction in windDirections) == False:
      print(Back.RED + " Windrichtungsdaten konnten nicht gelanden werden! Exit Code 1 ")
   
   if windDirectionCounter == 16: 
      print(Fore.GREEN + " Windrichtungsdaten erfolgreich geladen! ")
   else: 
      print(Back.RED + " Windrichtungsdaten konnten nicht gelanden werden! Exit Code 1 ")
      exit()
   
   windDirection = windDirections

   # Proof Temperature
   global temperatureMinimal
   global temperatureMaximum
   global temperatureMeanValue
   global currentTemperatureMonth

   minimal = obj['temperature']['minimal']
   maximum = obj['temperature']['maximum']

   name = " Temperaturdaten"
   ProofSettingsTypeSupporter(minimal, maximum, name)
   
   temperatureMinimal = minimal
   temperatureMaximum = maximum
   currentTemperatureMonth = ""
   temperatureMeanValue = (minimal + maximum) / 2

   # Proof WindSpeed
   global windSpeedMinimal 
   global windSpeedMaximum
   global currentWindSpeedMonth
   global windSpeedMeanValue

   minimal= obj['wind-speed']['minimal']
   maximum = obj['wind-speed']['maximum']

   name = " Windgeschwindigkeitsdaten"
   ProofSettingsTypeSupporter(minimal, maximum, name)

   windSpeedMinimal = minimal
   windSpeedMaximum = maximum
   currentWindSpeedMonth = ""
   windSpeedMeanValue = (minimal + maximum) / 2

   # Proof AirPressure
   global airPressureMinimal
   global airPressureMaximum
   global airPressureMeanValue

   minimal = obj['air-pressure']['minimal']
   maximum = obj['air-pressure']['maximum']

   name = " Luftdruckdaten"
   ProofSettingsTypeSupporter(minimal, maximum, name)

   airPressureMinimal = minimal
   airPressureMaximum = maximum
   airPressureMeanValue = (minimal + maximum) / 2

   print("\n", Back.GREEN + " Alle Daten erfolgreich geladen! Beginne mit der Datengenerierung! ", "\n")


def ProofSettingsIntSupport(number, name):
   if type(number) == int and (number == 0 or number > 0):
      Outprint = name + " erfolgreich gelanden! "
      print(Fore.GREEN + Outprint)
   else:
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit()


def ProofSettingsTypeSupporter(minimal, maximum, name):
   if type(minimal and maximum) == int and maximum > minimal: 
      Outprint = name + " erfolgreich geladen! "
      print(Fore.GREEN + Outprint)
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


   while generateDataSets != generatedDataFactor:
      if int(generateDataSets) % 500 == 0 and generateDataSets != 0: 
         print(generateDataSets, Back.GREEN + " Datensätze generiert! \n")
         time.sleep(1)

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
   global getTemperatureData
   global getWindSpeedData
   global getAirPressureData

   getTemperatureData = True 
   getWindSpeedData = True
   getAirPressureData = True

   # Generiere das Datum
   GenerateDate()
   global Time
   global isNightBoolean

   # Generiere die Windrichtung 
   GenerateWindDirection()
   global windDirections

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
        "Wind-Direction": windDirections,
        "Temperature": Temperature,
        "Wind-Speed": WindSpeed,
        "Air-Pressure": AirPressure
      }
   )


def GenerateDate():

   global startDate
   global generateDataSets
   global Time
   global isNightBoolean
   isNightBoolean = False
   global currentMonthTemperature
   global currentMonthWindSpeed

   if generateDataSets == 0:
       lastGeneratedTime = startDate
   else:
       lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
       lastGeneratedTime = generatedData[lastGeneratedLen]["Time"]

        # Beachten, dass durch neue Daten dies nicht mehr funktioniert, da die Time in der Json verrückt wird
    
   NewTime = datetime.strptime(lastGeneratedTime, "%Y-%m-%d %H:%M:%S.%f") + timedelta(hours=24)
   Time = str(NewTime)
      # Abfrage, die bestimmt, ob es Tag oder Nacht ist und entsprechend die Maximaltempetur anpasst. 

   splittedTime = Time.split(" ", )
   splittedTimeHour = splittedTime[1].split(":")
   splittedTimeMonth = splittedTime[0].split("-")
   intSplittedTimeMonth = int(splittedTimeMonth[1])
   intSplittedTimeHour = int(splittedTimeHour[0])


   if intSplittedTimeHour < 7 or intSplittedTimeHour > 20:
      isNightBoolean = True
   
   elif intSplittedTimeHour > 7 and intSplittedTimeHour < 21 or intSplittedTimeHour == 7:
      isNightBoolean = False

   # Aus Settings herraus
   Winter = [12,1,2]
   Frühling = [3,4,5]
   Sommer = [6,7,8]
   Herbst = [9,10,11]

   if intSplittedTimeMonth in Winter:
      currentMonthTemperature = -15
      currentMonthWindSpeed = 180
   
   elif intSplittedTimeMonth in Frühling:
      currentMonthTemperature = 0
      currentMonthWindSpeed = 120

   elif intSplittedTimeMonth in Sommer:
      currentMonthTemperature = 15
      currentMonthWindSpeed = 60

   elif intSplittedTimeMonth in Herbst:
      currentMonthTemperature = 5
      currentMonthWindSpeed = 260

   # print(Back.CYAN + " generateWindDirection ")


def GenerateWindDirection():
   # Getting Data form settings.json 
   global windDirection
   global hurricaneMultiplicator
   global generateDataSets

   if generateDataSets == 0:
      generateDirection = str(round(random.uniform(1,4)))
      generatePreciseDirection = str(round(random.uniform(0,3)))

      generatedWindDirection = generateDirection + "." + generatePreciseDirection
   
      newWindDirection = windDirection[generatedWindDirection]

   else: 
      keyList = [3,0,1] # List all possible new Keys for x.0 and x.3
      lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
      lastGeneratedWindDirection = generatedData[lastGeneratedLen]["Wind-Direction"]

      lastGeneratedWindDirectionKey = list(windDirection.keys())[list(windDirection.values()).index(lastGeneratedWindDirection)]
      splittedLastGeneratedWindDirectionKey = lastGeneratedWindDirectionKey.split(".")

      if splittedLastGeneratedWindDirectionKey[1] ==  "0":
         newWindDirectionSecoundKey = random.choice(keyList)
         
         if newWindDirectionSecoundKey == 0:
            splittedLastGeneratedWindDirectionKey[0] = round(random.uniform(1,4))

      if splittedLastGeneratedWindDirectionKey[1] == "1":
         newWindDirectionSecoundKey = round(random.uniform(0,2))
         
      if splittedLastGeneratedWindDirectionKey[1] == "2":
         newWindDirectionSecoundKey = round(random.uniform(1,3))

      if splittedLastGeneratedWindDirectionKey[1] == "3":   
         newWindDirectionSecoundKey = random.choice(keyList)

         if newWindDirectionSecoundKey == 0:
            splittedLastGeneratedWindDirectionKey[0] = round(random.uniform(1,4))
        

      generatedWindDirection = str(splittedLastGeneratedWindDirectionKey[0]) + "." + str(newWindDirectionSecoundKey)
      newWindDirection = windDirection[generatedWindDirection]

   global windDirections
   windDirections = newWindDirection


   # print(Back.BLUE + " generateWindDirection ")

   # Nur einmal bestimmen, damit die richtung nicht dauerhaft wechselt


def GenerateTemperature():
   # Getting Data from settings.json
   global temperatureMinimal
   global temperatureMaximum
   global hurricaneMultiplicator
   global getTemperatureData
   global temperatureMeanValue
   global isNightBoolean
   global currentMonthTemperature
   global currentTemperatureMonth
   global lastGeneratedTemperature

   if generateDataSets == 0:
      lastGeneratedTemperature = currentMonthTemperature
      currentTemperatureMonth = currentMonthTemperature

      if isNightBoolean == True and (lastGeneratedTemperature/5) *4 >= temperatureMinimal:
         lastGeneratedTemperature = (lastGeneratedTemperature/5) *4

   else:
      if getTemperatureData == True: 
         lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
         lastGeneratedTemperature = generatedData[lastGeneratedLen]["Temperature"]

      lastGeneratedTemperatureMinimal = lastGeneratedTemperature - 2 
      lastGeneratedTemperatureMaximum = lastGeneratedTemperature + 2 

      if lastGeneratedTemperature < temperatureMeanValue:
               
         if temperatureMinimal < lastGeneratedTemperatureMinimal: 
            lastGeneratedTemperature = round(random.uniform(lastGeneratedTemperatureMinimal, lastGeneratedTemperatureMaximum))

            if isNightBoolean == True and (lastGeneratedTemperature/5) *4 >= temperatureMinimal:
               lastGeneratedTemperature = (lastGeneratedTemperature/5) *4

            if currentTemperatureMonth != currentMonthTemperature:
               lastGeneratedTemperature = currentMonthTemperature
               currentTemperatureMonth = currentMonthTemperature

         elif temperatureMinimal > lastGeneratedTemperatureMinimal or temperatureMinimal == lastGeneratedTemperatureMinimal:
            lastGeneratedTemperature += 3
            getTemperatureData = not getTemperatureData 
            GenerateTemperature()

      elif lastGeneratedTemperature == temperatureMeanValue or lastGeneratedTemperature > temperatureMeanValue: 
               
         if temperatureMaximum > lastGeneratedTemperatureMaximum:
            lastGeneratedTemperature = round(random.uniform(lastGeneratedTemperatureMinimal, lastGeneratedTemperatureMaximum))

            if isNightBoolean == True and (lastGeneratedTemperature/5) *4 <= temperatureMaximum:
               lastGeneratedTemperature = (lastGeneratedTemperature/5) *4
            
            if currentTemperatureMonth != currentMonthTemperature:
               lastGeneratedTemperature = currentMonthTemperature
               currentTemperatureMonth = currentMonthTemperature

         elif temperatureMaximum < lastGeneratedTemperatureMaximum or temperatureMaximum == lastGeneratedTemperatureMaximum:
            lastGeneratedTemperature -= 3
            getTemperatureData = not getTemperatureData
            GenerateTemperature()
        
   global Temperature
   Temperature = lastGeneratedTemperature



def GenerateWindSpeed():
   global windSpeedMinimal
   global windSpeedMaximum
   global hurricaneMultiplicator
   global generateDataSets
   global getWindSpeedData
   global windSpeedMeanValue
   global isNightBoolean
   global currentMonthWindSpeed
   global currentWindSpeedMonth
   global lastGeneratedWindSpeed
   global blockingElifLoop

   if generateDataSets == 0:
      lastGeneratedWindSpeed = currentMonthWindSpeed
      currentWindSpeedMonth = currentMonthWindSpeed

      if isNightBoolean == True and (lastGeneratedWindSpeed/5) *4 >= windSpeedMinimal:
         lastGeneratedWindSpeed = (lastGeneratedWindSpeed/5) *4

   else:
       if getWindSpeedData == True:
         lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
         lastGeneratedWindSpeed = generatedData[lastGeneratedLen]["Wind-Speed"]

       lastGeneratedWindSpeedMinimal = lastGeneratedWindSpeed - 20
       lastGeneratedWindSpeedMaximum = lastGeneratedWindSpeed + 20

       if lastGeneratedWindSpeed < windSpeedMeanValue:

         if windSpeedMinimal < lastGeneratedWindSpeedMinimal:
            lastGeneratedWindSpeed = round(random.uniform(lastGeneratedWindSpeedMinimal, lastGeneratedWindSpeedMaximum))

            if isNightBoolean == True and (lastGeneratedWindSpeed/5) *4 >= windSpeedMinimal:
               lastGeneratedWindSpeed = (lastGeneratedWindSpeed/5) *4

            if currentWindSpeedMonth != currentMonthWindSpeed:
               lastGeneratedWindSpeed = currentMonthWindSpeed
               currentWindSpeedMonth = currentMonthWindSpeed

         elif windSpeedMinimal > lastGeneratedWindSpeedMinimal or windSpeedMinimal == lastGeneratedWindSpeedMinimal:
            lastGeneratedWindSpeed += 25
            getWindSpeedData = not getWindSpeedData
            GenerateWindSpeed()
       
       elif lastGeneratedWindSpeed > windSpeedMeanValue or lastGeneratedWindSpeed == windSpeedMeanValue:
         
         if windSpeedMaximum > lastGeneratedWindSpeedMaximum:
            lastGeneratedWindSpeed = round(random.uniform(lastGeneratedWindSpeedMinimal, lastGeneratedWindSpeedMaximum))

            if isNightBoolean == True and (lastGeneratedWindSpeed/5)*4 <= windSpeedMaximum:
               lastGeneratedWindSpeed = (lastGeneratedWindSpeed/5)*4

            if currentWindSpeedMonth != currentMonthWindSpeed:
              lastGeneratedWindSpeed = currentMonthWindSpeed
              currentWindSpeedMonth = currentMonthWindSpeed

         elif windSpeedMaximum < lastGeneratedWindSpeedMaximum or windSpeedMaximum == lastGeneratedWindSpeedMaximum:
            lastGeneratedWindSpeed -= 25
            getWindSpeedData = not getWindSpeedData
            GenerateWindSpeed()



   global WindSpeed
   WindSpeed = lastGeneratedWindSpeed


def GenerateAirPressure():
   global airPressureMinimal
   global airPressureMaximum
   global hurricaneMultiplicator
   global generateDataSets
   global getAirPressureData
   global airPressureMeanValue

   if generateDataSets == 0:
       global lastGeneratedAirPressure
       lastGeneratedAirPressure = round(random.uniform(airPressureMinimal,airPressureMaximum))

   else:
       if getAirPressureData == True: 
         lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
         lastGeneratedAirPressure = generatedData[lastGeneratedLen]["Air-Pressure"]

       lastGeneratedAirPressureMinimal = lastGeneratedAirPressure - 20
       lastGeneratedAirPressureMaximum = lastGeneratedAirPressure + 20
      
       if lastGeneratedAirPressure < airPressureMeanValue:
          
          if airPressureMinimal < lastGeneratedAirPressureMinimal:
            lastGeneratedAirPressure = round(random.uniform(lastGeneratedAirPressureMinimal, lastGeneratedAirPressureMaximum))

          elif airPressureMinimal > lastGeneratedAirPressureMinimal or airPressureMinimal == lastGeneratedAirPressureMinimal:
            lastGeneratedAirPressure += 25
            getAirPressureData = not getAirPressureData 
            GenerateAirPressure()

       elif lastGeneratedAirPressure > airPressureMeanValue or lastGeneratedAirPressure == airPressureMeanValue:
          
          if airPressureMaximum > lastGeneratedAirPressureMaximum:
            lastGeneratedAirPressure = round(random.uniform(lastGeneratedAirPressureMinimal, lastGeneratedAirPressureMaximum))

          elif airPressureMaximum < lastGeneratedAirPressureMaximum or airPressureMaximum == lastGeneratedAirPressureMaximum: 
            lastGeneratedAirPressure -= 25
            getAirPressureData = not getAirPressureData 
            GenerateAirPressure()

   global AirPressure
   AirPressure = lastGeneratedAirPressure


def SaveData():
    global generateDataSets
    global savingDataFile

    print(generateDataSets, Back.GREEN + " Datensätze generiert! \n")

    JSONData = json.dumps(generatedData,indent=4, separators=(',',': '))
    SavingFile = open(savingDataFile, "w")
    SavingFile.write(JSONData)
    SavingFile.close()

    print("", Back.GREEN + " Datengenerierung erfolgreich abgeschlossen und gespeichert! ", "\n")

MainGeneration()