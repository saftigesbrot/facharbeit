import json
import random
import datetime
import time
from datetime import timedelta, datetime
from colorama import *
init(autoreset=True)
generatedData = []

def ProofSettings():
   
   # Überpüftt alle Einstellungen der settings.json Datei auf ihre Kompatibilität

   with open('settings.json','r') as file:
      obj = json.load(file)

   # Proof GeneralSettings
   global hurricaneProbability 
   number = obj['general-settings']['hurricane-probability']

   # Schöner machen
   name = " Hurrikanwahrscheinlichkeit"
   
   ProofSettingsIntSupporter(number, name)
   hurricaneProbability = number

   global hurricaneMultiplicator
   number = obj['general-settings']['hurricane-multiplicator']
   name = " Hurrikanmultiplikator"

   ProofSettingsIntSupporter(number, name)
   hurricaneMultiplicator = number

   global generatedDataFactor
   number = obj['general-settings']['generate-data-factor']
   name = " Datengenerierungsfakor"

   ProofSettingsIntSupporter(number, name)
   generatedDataFactor = number

   global generateDataSets
   number = obj['general-settings']['generated-data-sets']
   name = " Datengenerierungssätze"

   ProofSettingsIntSupporter(number, name)
   generateDataSets = number

   global addingHourse
   number = obj['general-settings']['adding-hourse']
   name = " Hinzuzufügendestundendaten"

   ProofSettingsIntSupporter(number, name)
   addingHourse = number

   # Proof Date
   global startDate
   date = obj['general-settings']['start-date']
   format = "%Y-%m-%d %H:%M:%S.%f"

   try:
      bool(datetime.strptime(date, format))
      print(Fore.GREEN + " Datum erfolgreich geladen! ")
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

   # Proof DayNightCycle
   global nightBeginn
   global nightEnd

   number = obj['day-night-cycle']['night-beginn']
   name = " Nachtbeginndaten"
  
   ProofSettingsDayNightSupporter(number, name)
   nightBeginn = number

   number = obj['day-night-cycle']['night-end']
   name = " Nachtendedaten"

   ProofSettingsDayNightSupporter(number, name)
   nightEnd = number


   # Proof Seasons
   global springTemperature
   global springWindSpeed
   global sommerTemperature
   global sommerWindSpeed
   global autumnTemperature
   global autumnWindSpeed
   global winterTemperature
   global winterWindSpeed

   global springMonths
   global sommerMonths
   global autumnMonths
   global winterMonths

   number = obj['seasons']['spring-temperature']
   name = " Frühlingstemperaturdaten"

   ProofSettingsSeasonsSupporter(number, name)
   springTemperature = number

   number = obj['seasons']['sommer-temperature']
   name = " Sommertemperaturdaten"
   
   ProofSettingsSeasonsSupporter(number, name)
   sommerTemperature = number

   number = obj['seasons']['autumn-temperature']
   name = " Herbsttemperaturdaten"

   ProofSettingsSeasonsSupporter(number, name)
   autumnTemperature = number

   name = obj['seasons']['winter-temperature']
   name = " Wintertemperaturdaten"

   ProofSettingsSeasonsSupporter(number, name)
   winterTemperature = number 

   
   number = obj['seasons']['spring-wind-speed']
   name = " Frühlingswindgeschwindigkeitsdaten"

   ProofSettingsIntSupporter(number, name)
   springWindSpeed = number

   number = obj['seasons']['sommer-wind-speed']
   name = " Sommerwindgeschwindigkeitsdaten"

   ProofSettingsIntSupporter(number, name)
   sommerWindSpeed = number

   number = obj['seasons']['autumn-wind-speed']
   name = " Herbstwindgeschwindigkeitsdaten"

   ProofSettingsIntSupporter(number, name)
   autumnWindSpeed = number

   number = obj['seasons']['winter-wind-speed']
   name = " Winterwindgeschwindigkeitsdaten"

   ProofSettingsIntSupporter(number, name)
   winterWindSpeed = number


   lists = obj['seasons']['spring-months']
   name = " Frühlingsmonatsdaten"

   ProofSettingsListSupporter(lists, name)
   springMonths = lists

   lists = obj['seasons']['sommer-months']
   name = " Sommermonatsdaten"

   ProofSettingsListSupporter(lists, name)
   sommerMonths = lists

   lists = obj['seasons']['autumn-months']
   name = " Herbstmonatsdaten"

   ProofSettingsListSupporter(lists, name)
   autumnMonths = lists
   
   lists = obj['seasons']['winter-months']
   name = " Wintermonatsdaten"

   ProofSettingsListSupporter(lists, name)
   winterMonths = lists
   

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


def ProofSettingsIntSupporter(number, name):
   if type(number) == int and (number == 0 or number > 0):
      Outprint = name + " erfolgreich gelanden! "
      print(Fore.GREEN + Outprint)
   else:
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit()

def ProofSettingsDayNightSupporter(number, name):
   if type(number) == int and (number == 0 or number > 0) and (number == 24 or number < 24):
      Outprint = name + " erfolgreich gelanden! "
      print(Fore.GREEN + Outprint)
   else:
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit()

def ProofSettingsListSupporter(lists, name): 
   listCounter = 0
   for x in lists:
      if type(x) == int and x > 0 and x < 13:
         listCounter = listCounter + 1
      else: 
         Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
         print(Back.RED + Outprint)
         exit() 
   if listCounter == 3:
      Outprint = name + " erfolgreich geladen! "
      print(Fore.GREEN + Outprint)
   else:
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit() 

def ProofSettingsSeasonsSupporter(number, name):
   if type(number) == int: 
      Outprint = name + " erfolgreich geladen! "
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
   global hurricaneBoolean
   hurricaneBoolean = False
   global hurricaneInAction
   hurricaneInAction = False


   while generateDataSets != generatedDataFactor:
      if int(generateDataSets) % 500 == 0 and generateDataSets != 0: 
         print(generateDataSets, Back.GREEN + " Datensätze generiert! \n")
         time.sleep(1)

      hurricaneChance = random.uniform(0,100)

      if hurricaneChance > hurricaneProbability and hurricaneInAction == False:
         # And Abfrage um keine neuen Daten zu generieren wenn noch ein Hurrikan läuft
         hurricaneBoolean = False
         DataGeneration()

      elif hurricaneChance == hurricaneProbability or hurricaneChance < hurricaneProbability or hurricaneInAction == True:
         # or abfrage, ob bereits ein Hurrikan läuft
         hurricaneBoolean = True
         DataGeneration()

      generateDataSets += 1

      # Für jeden Datensatz, der erstellt wird, gibt es eine neue Hurrikan Wahrscheinlichkeit -> Wenn bereits ein Hurrikan vorhanden ist, 
      # sollte dies nicht passieren, da sich sonst zwei Hurrikans überschneiden können
   SaveData()


def DataGeneration():
   global getTemperatureData
   global getWindSpeedData
   global getAirPressureData
   global hurricaneInAction
   global hurricaneBoolean
   global generateDataSets

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

   if hurricaneBoolean == True and hurricaneInAction == True:
      actionHurricane()

   elif hurricaneBoolean == True and hurricaneInAction == False:
      startHurricane()

   elif hurricaneBoolean == False and hurricaneInAction == False:
      hurricaneInAction = False
      # hurricaneInAction muss bereits voher "False" sein

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
        "Air-Pressure": AirPressure,
        "Datasets": generateDataSets
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

   global springMonths
   global sommerMonths
   global autumnMonths
   global winterMonths

   global springTemperature
   global springWindSpeed
   global sommerTemperature
   global sommerWindSpeed
   global autumnTemperature
   global autumnWindSpeed
   global winterTemperature
   global winterWindSpeed

   global nightBeginn
   global nightEnd
   global addingHourse

   if generateDataSets == 0:
       lastGeneratedTime = startDate
   else:
       lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
       lastGeneratedTime = generatedData[lastGeneratedLen]["Time"]

        # Beachten, dass durch neue Daten dies nicht mehr funktioniert, da die Time in der Json verrückt wird
    
   NewTime = datetime.strptime(lastGeneratedTime, "%Y-%m-%d %H:%M:%S.%f") + timedelta(hours=addingHourse)
   Time = str(NewTime)
      # Abfrage, die bestimmt, ob es Tag oder Nacht ist und entsprechend die Maximaltempetur anpasst. 

   splittedTime = Time.split(" ", )
   splittedTimeHour = splittedTime[1].split(":")
   splittedTimeMonth = splittedTime[0].split("-")
   intSplittedTimeMonth = int(splittedTimeMonth[1])
   intSplittedTimeHour = int(splittedTimeHour[0])


   if intSplittedTimeHour < nightEnd or intSplittedTimeHour > nightBeginn:
      isNightBoolean = True
   
   elif intSplittedTimeHour > nightEnd and intSplittedTimeHour < nightBeginn or intSplittedTimeHour == nightEnd:
      isNightBoolean = False

   # Aus Settings herraus
  
   if intSplittedTimeMonth in springMonths:
      currentMonthTemperature = springTemperature
      currentMonthWindSpeed = springWindSpeed

   elif intSplittedTimeMonth in sommerMonths:
      currentMonthTemperature = sommerTemperature
      currentMonthWindSpeed = sommerWindSpeed

   elif intSplittedTimeMonth in autumnMonths:
      currentMonthTemperature = autumnTemperature
      currentMonthWindSpeed = autumnWindSpeed

   elif intSplittedTimeMonth in winterMonths:
      currentMonthTemperature = winterTemperature
      currentMonthWindSpeed = winterWindSpeed

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
   global hurricaneInAction

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

            # if hurricaneInAction == True and lastGeneratedTemperature * hurricaneMultiplicator >= temperatureMinimal:
            #    lastGeneratedTemperature = lastGeneratedTemperature * hurricaneMultiplicator
            #    # Der Multiplikator muss so eingesetzt werden, dass auch wirklich ein Hurrikan entsteht 

            # if hurricaneInAction == True and lastGeneratedTemperature * hurricaneMultiplicator < temperatureMinimal:
            #    lastGeneratedTemperature = lastGeneratedTemperature    

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

            if hurricaneInAction == True and lastGeneratedTemperature * hurricaneMultiplicator <= temperatureMaximum:
               lastGeneratedTemperature = lastGeneratedTemperature * hurricaneMultiplicator

            if hurricaneInAction == True and lastGeneratedTemperature * hurricaneMultiplicator > temperatureMaximum:
               lastGeneratedTemperature = lastGeneratedTemperature

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
   hurricaneMultiplicatorForWindSpeed = hurricaneMultiplicator
   global generateDataSets
   global getWindSpeedData
   global windSpeedMeanValue
   global isNightBoolean
   global currentMonthWindSpeed
   global currentWindSpeedMonth
   global lastGeneratedWindSpeed
   global blockingElifLoop
   global hurricaneInAction

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

            if currentWindSpeedMonth != currentMonthWindSpeed:
               lastGeneratedWindSpeed = currentMonthWindSpeed
               currentWindSpeedMonth = currentMonthWindSpeed

            if isNightBoolean == True and (lastGeneratedWindSpeed/5) *4 >= windSpeedMinimal:
               lastGeneratedWindSpeed = (lastGeneratedWindSpeed/5) *4
            
            # if hurricaneInAction == True and lastGeneratedWindSpeed * hurricaneMultiplicator >= windSpeedMinimal:
            #    lastGeneratedWindSpeed = lastGeneratedWindSpeed * hurricaneMultiplicator

            # if hurricaneInAction == True and lastGeneratedWindSpeed * hurricaneMultiplicator < windSpeedMinimal:
            #    lastGeneratedWindSpeed = lastGeneratedWindSpeed  


         elif windSpeedMinimal > lastGeneratedWindSpeedMinimal or windSpeedMinimal == lastGeneratedWindSpeedMinimal:
            lastGeneratedWindSpeed += 25
            getWindSpeedData = not getWindSpeedData
            GenerateWindSpeed()
       
       elif lastGeneratedWindSpeed > windSpeedMeanValue or lastGeneratedWindSpeed == windSpeedMeanValue:
         
         if windSpeedMaximum > lastGeneratedWindSpeedMaximum:
            lastGeneratedWindSpeed = round(random.uniform(lastGeneratedWindSpeedMinimal, lastGeneratedWindSpeedMaximum))
            
            if currentWindSpeedMonth != currentMonthWindSpeed:
              lastGeneratedWindSpeed = currentMonthWindSpeed
              currentWindSpeedMonth = currentMonthWindSpeed
            
            if isNightBoolean == True and (lastGeneratedWindSpeed/5)*4 <= windSpeedMaximum:
               lastGeneratedWindSpeed = (lastGeneratedWindSpeed/5)*4

            if hurricaneInAction == True and lastGeneratedWindSpeed * hurricaneMultiplicatorForWindSpeed <= windSpeedMaximum:
               lastGeneratedWindSpeed = lastGeneratedWindSpeed * hurricaneMultiplicatorForWindSpeed

            if hurricaneInAction == True and lastGeneratedWindSpeed * hurricaneMultiplicatorForWindSpeed > windSpeedMaximum:
               lastGeneratedWindSpeed = lastGeneratedWindSpeed 

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
   global hurricaneInAction

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

def startHurricane():
   # Hier beginnt ein neuer Hurrikane
   global Temperature
   global WindSpeed
   global AirPressure
   global hurricaneInAction
   global hurricaneLength
   global hurricaneBoolean
   global hurricaneInAction
   global generateDataSets

   # print(generateDataSets)
   hurricaneLength = round(random.uniform(1,10))
   hurricaneInAction = True

   GenerateTemperature()
   GenerateWindSpeed()
   GenerateAirPressure()

   # Abfangen, dass der hurricane nicht endet, wenn die Werte zu groß werden
   
   hurricaneLength -= 1 

def actionHurricane():
   global hurricaneLength
   global Temperature
   global WindSpeed
   global AirPressure
   global hurricaneInAction
   global hurricaneBoolean
   global generateDataSets

   if hurricaneLength != 0:
      GenerateTemperature()
      GenerateWindSpeed()
      GenerateAirPressure()
      hurricaneLength -= 1

   elif hurricaneLength == 0:
      hurricaneInAction = False
      hurricaneBoolean = False

   # Hier wird der hurricane fortgeführt


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