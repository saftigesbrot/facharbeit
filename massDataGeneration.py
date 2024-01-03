# Importiert das "JSON" Modul -> Speichern/Lesen von Daten mit einer JSON Datei
import json 
# Importiert das "Random" Modul -> Erstellen von zufälligen Zahlen
import random 
# Importiert das "datetime" Modul -> Erstellen Zeitangaben
import datetime 
# Importiert das "time" Modul -> Unterbrechen des Algorithmus
import time  
# Importiert die Module "timedelta, datetime" -> Addieren und Formatieren von Zeitangaben
from datetime import timedelta, datetime 
# Importiert das "colorama" Modul -> Farbiger Text in der Ausgabe / Konsole
from colorama import * 
init(autoreset=True) 
# Variable zum zwischenspeichern der generierten Daten 
generatedData = [] 

# Überpüftt alle Einstellungen der settings.json Datei auf ihre Kompatibilität
def ProofSettings(): 

   # Lädt die Einstellungen aus der "settings.json" und speichert sie in der Variable "obj"
   with open('settings.json','r') as file: 
      obj = json.load(file)

   # Lädt die Hurrikan Wahrscheinlichkeit aus der "obj" Variable, und prüft mithilfe der 
   # "ProofSettingsIntSupporter" Funktion die Richtig- und Vollständigkeit. Anschließend 
   # wird die Wahrscheinlichkeit in die Globale Variable "hurricaneProbability" gespeichert.
   global hurricaneProbability 
   number = obj['general-settings']['hurricane-probability']
   name = " Hurrikanwahrscheinlichkeit"
   
   ProofSettingsIntSupporter(number, name)
   hurricaneProbability = number

   # Lädt den Hurrikan Multiplikator aus der "obj" Variable, und prüft mithilfe der 
   # "ProofSettingsIntSupporter" Funktion die Richtig- und Vollständigkeit. Anschließend 
   # wird der Multiplikator in die Globale Variable "hurricaneMultiplicator" gespeichert.
   global hurricaneMultiplicator
   number = obj['general-settings']['hurricane-multiplicator']
   name = " Hurrikanmultiplikator"

   ProofSettingsIntSupporter(number, name)
   hurricaneMultiplicator = number

   # Lädt den Faktor, wieviele Daten generiert werden sollen, aus der "obj" Variable, und 
   # prüft mithilfe der "ProofSettingsIntSupporter" Funktion die Richtig- und Vollständigkeit. 
   # Anschließend wird der Faktor in die Globale Variable "generatedDataFactor" gespeichert.
   global generatedDataFactor
   number = obj['general-settings']['generate-data-factor']
   name = " Datengenerierungsfakor"

   ProofSettingsIntSupporter(number, name)
   generatedDataFactor = number

   # Lädt den Faktor, wieviele Daten bereits generiert wurden, aus der "obj" Variable, und 
   # prüft mithilfe der "ProofSettingsIntSupporter" Funktion die Richtig- und Vollständigkeit. 
   # Anschließend wird der Faktor in die Globale Variable "generateDataSets" gespeichert.
   global generateDataSets
   number = obj['general-settings']['generated-data-sets']
   name = " Datengenerierungssätze"

   ProofSettingsIntSupporter(number, name)
   generateDataSets = number

   # Lädt die Anzahl der Stunden, die pro Datensatz hinzugefügt werden sollen, aus der 
   # "obj" Variable, und prüft mithilfe der "ProofSettingsIntSupporter" Funktion die Richtig- 
   # und Vollständigkeit. Anschließend wird die Anzahl der Stunden in die Globale Variable 
   # "addingHourse" gespeichert.
   global addingHourse
   number = obj['general-settings']['adding-hourse']
   name = " Hinzuzufügendestundendaten"

   ProofSettingsIntSupporter(number, name)
   addingHourse = number

   # Lädt das Start Datum und überprüft ob dieses mit dem Format übereinstimmt. Wenn 
   # dies nicht der Fall ist, wird ein Error ausgegeben mit dem Exit Code "1" und das 
   # Programm wird beendet. Wenn das Datum erfolgreich geladen wurde wird es in der 
   # Globalen Variable "startDate" gespeichert.
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

   # Lädt die Datei, in der die Daten gespeichert werden sollen und überprüft, ob es
   # sich um einen string handelt und ob die Endung ".json" entspricht. Wenn dies 
   # nicht der Fall ist, wird ein Error ausgegeben mit dem Exit Code "1" und das 
   # Programm wird beendet. Wenn die Datei erfolgreich geladen wurde, wird sie in die
   # Globale Variable "savingDataFile" gespeichert.
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

   # Lädt den Tages und Nacht beginn und überprüft diese mithilfe der 
   # "ProofSettingsDayNightSupporter" Funktion auf ihre Richtig- und Vollständigkeit.
   # Anschlißend wird der Beginn der Nacht in die Globale Variable "nightBeginn" und
   # das Ende der Nacht in die Globale Variable "nightEnd" geladen. 
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


   # Lädt die Temperaturen der jeweiligen Jahreszeiten und überprüft diese mit der 
   # "ProofSettingsSeasonsSupporter" Funktion auf ihre Richtig- und Vollständigkeit. 
   # Anschließend wird die Temperatur der Monate in die jeweiligen Globalen Variablen 
   # gespeichert. 
   global springTemperature
   number = obj['seasons']['spring-temperature']
   name = " Frühlingstemperaturdaten"

   ProofSettingsSeasonsSupporter(number, name)
   springTemperature = number

   global sommerTemperature
   number = obj['seasons']['sommer-temperature']
   name = " Sommertemperaturdaten"
   
   ProofSettingsSeasonsSupporter(number, name)
   sommerTemperature = number

   global autumnTemperature
   number = obj['seasons']['autumn-temperature']
   name = " Herbsttemperaturdaten"

   ProofSettingsSeasonsSupporter(number, name)
   autumnTemperature = number

   global winterTemperature
   name = obj['seasons']['winter-temperature']
   name = " Wintertemperaturdaten"

   ProofSettingsSeasonsSupporter(number, name)
   winterTemperature = number 

   # Lädt die Windgeschwindigkeit der jeweiligen Jahreszeiten und überprüft diese 
   # mit der "ProofSettingsIntSupporter" Funktion auf ihre Richtig- und Vollständigkeit. 
   # Anschließend wird die Windgeschwindigkeit der Monate in die jeweiligen Globalen 
   # Variablen gespeichert. 
   global springWindSpeed
   number = obj['seasons']['spring-wind-speed']
   name = " Frühlingswindgeschwindigkeitsdaten"

   ProofSettingsIntSupporter(number, name)
   springWindSpeed = number

   global sommerWindSpeed
   number = obj['seasons']['sommer-wind-speed']
   name = " Sommerwindgeschwindigkeitsdaten"

   ProofSettingsIntSupporter(number, name)
   sommerWindSpeed = number

   global autumnWindSpeed
   number = obj['seasons']['autumn-wind-speed']
   name = " Herbstwindgeschwindigkeitsdaten"

   ProofSettingsIntSupporter(number, name)
   autumnWindSpeed = number

   global winterWindSpeed
   number = obj['seasons']['winter-wind-speed']
   name = " Winterwindgeschwindigkeitsdaten"

   ProofSettingsIntSupporter(number, name)
   winterWindSpeed = number

   # Lädt die Monate der jeweiligen Jahreszeiten und überprüft diese mithilfe 
   # der "ProofSettingsListSupporter" Funktion auf ihre Richtig- und Vollständigkeit. 
   # Anschließend werden die Monate in die jeweiligen Globalen Variablen gespeichert. 
   global springMonths
   lists = obj['seasons']['spring-months']
   name = " Frühlingsmonatsdaten"

   ProofSettingsListSupporter(lists, name)
   springMonths = lists

   global sommerMonths
   lists = obj['seasons']['sommer-months']
   name = " Sommermonatsdaten"

   ProofSettingsListSupporter(lists, name)
   sommerMonths = lists

   global autumnMonths
   lists = obj['seasons']['autumn-months']
   name = " Herbstmonatsdaten"

   ProofSettingsListSupporter(lists, name)
   autumnMonths = lists

   global winterMonths
   lists = obj['seasons']['winter-months']
   name = " Wintermonatsdaten"

   ProofSettingsListSupporter(lists, name)
   winterMonths = lists
   

   # Lädt die Windrichtungen und überprüft alle, ob es sich dabei um strings 
   # handelt und ob 16 Windrichtungen vorhanden sind. Anschließend werden die
   # Windrichtungen in die Globale Variable "windDirection" gespeichert. 
   global windDirection
   windDirections = obj['wind-direction']['wind-directions']
   windDirectionCounter = 0

   for item in windDirections:
      if isinstance(windDirections[item], str) == True:
         windDirectionCounter += 1
      elif isinstance(windDirections[item], str) == False:
         print(Back.RED + " Windrichtungsdaten konnten nicht gelanden werden! Exit Code 1 ")
         exit()

   if windDirectionCounter == 16: 
      print(Fore.GREEN + " Windrichtungsdaten erfolgreich geladen! ")
   else: 
      print(Back.RED + " Windrichtungsdaten konnten nicht gelanden werden! Exit Code 1 ")
      exit()
   
   windDirection = windDirections

   # Lädt die minimale und maximale Temperatur und überprüft diese mithilfe der 
   # "ProofSettingsTypeSupporter" Funktion auf ihre Richtig- und Vollständigkeit. 
   # Anschließend werden das Temperatur Minimum und Maximum, sowie der Mittelwert
   # jeweils in einer Globalen Variable gespeichert. Außerdem wird ein Globale 
   # Variable "currentTemperatureMonth" erstellt, welche die Tempereatur des 
   # aktuellen Monats speichert. 
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

   # Lädt die minimale und maximale Windgeschwindigkeit und überprüft diese mithilfe  
   # der "ProofSettingsTypeSupporter" Funktion auf ihre Richtig- und Vollständigkeit. 
   # Anschließend werden das Windgeschwindgkeits Minimum und Maximum, sowie der 
   # Mittelwert jeweils in einer Globalen Variable gespeichert. Außerdem wird ein 
   # Globale Variable "currentWindSpeedMonth" erstellt, welche die Windgeschwindigkeit
   # des aktuellen Monats speichert. 
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

   # Lädt den minimalen und maximalen Luftdurck und überprüft diese mithilfe  
   # der "ProofSettingsTypeSupporter" Funktion auf ihre Richtig- und Vollständigkeit. 
   # Anschließend wird das Minimum und Maximum des Luftdrucks, sowie der 
   # Mittelwert jeweils in einer Globalen Variable gespeichert. 
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

# Diese Funktion überprüft ob die Zahl, welche übergeben wird, auch wirklich ein 
# Intager ist und ob die Zahl 0 oder größer ist. Wenn dies der Fall ist, wird 
# eine Ausgabe getätigt, die dem Nutzer das erfolgreiche Laden bestätigen, wenn 
# nicht wird dem Nutzer dies mitgeteilt und das Programm beendet. 
def ProofSettingsIntSupporter(number, name):
   if type(number) == int and (number == 0 or number > 0):
      Outprint = name + " erfolgreich gelanden! "
      print(Fore.GREEN + Outprint)
   else:
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit()

# Diese Funktion überprüft ob die Zahl, welche übergeben wird, auch wirklich ein 
# Intager ist, ob die Zahl 0 oder größer ist und ob das sie nicht größer als 24 ist. 
# Wenn dies der Fall ist, wird eine Ausgabe getätigt, die dem Nutzer das erfolgreiche 
# Laden bestätigen, wenn nicht wird dem Nutzer dies mitgeteilt und das Programm beendet. 
# Da die Zahl auf einen Wert zwischen 0 und 24 überprüft wird, wird an dieser Stelle
# der Tag/Nacht Zyklus überprüft.
def ProofSettingsDayNightSupporter(number, name):
   if type(number) == int and (number == 0 or number > 0) and (number == 24 or number < 24):
      Outprint = name + " erfolgreich gelanden! "
      print(Fore.GREEN + Outprint)
   else:
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit()

# Diese Funktion überprüft ob die einzelnen Zahlen der Liste, welche übergeben wird, 
# auch wirklich Intager sind und ob die Zahl größer als 0 und kleiner als 13 sind. 
# Zudem wird überprüft, ob pro Liste 3 Zahlen vorhanden sind. Wenn dies der Fall ist, 
# wird eine Ausgabe getätigt, die dem Nutzer das erfolgreiche Laden bestätigen, wenn 
# nicht wird dem Nutzer dies mitgeteilt und das Programm beendet. 
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

# Diese Funktion überprüft ob die Zahl, welche übergeben wird, auch wirklich ein 
# Intager ist. Wenn dies der Fall ist, wird eine Ausgabe getätigt, die dem Nutzer 
# das erfolgreiche Laden bestätigen, wenn nicht wird dem Nutzer dies mitgeteilt 
# und das Programm beendet. 
def ProofSettingsSeasonsSupporter(number, name):
   if type(number) == int: 
      Outprint = name + " erfolgreich geladen! "
      print(Fore.GREEN + Outprint)
   else: 
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit() 

# Diese Funktion überprüft ob die Zahlen, welche übergeben werde, auch wirklich
# Intager sind und ob das Maximum größer ist als das Minimum. Wenn dies der Fall 
# ist, wird eine Ausgabe getätigt, die dem Nutzer das erfolgreiche Laden bestätigen, 
# wenn nicht wird dem Nutzer dies mitgeteilt und das Programm beendet. 
def ProofSettingsTypeSupporter(minimal, maximum, name):
   if type(minimal and maximum) == int and maximum > minimal: 
      Outprint = name + " erfolgreich geladen! "
      print(Fore.GREEN + Outprint)
   else: 
      Outprint = name + " konnten nicht gelanden werden! Exit Code 1 "
      print(Back.RED + Outprint)
      exit() 

# Diese Funktion startet die Datengenerierung
def MainGeneration():

   # Startet die "ProofSettings" Funktion zum überprüfen aller Einstellungen
   ProofSettings()

   # Übernimmt die Variablen und setzt sie auf ihre Standardwerte
   global generateDataSets # Zählt, wie viele Datensätze bereits generiert wurden
   global hurricaneProbability # Gibt an, wie hoch die Hurrikan Wahrscheinlichkeit ist
   global generatedDataFactor # Bestimmt, wie viele Datensätze generiert werden sollen
   global hurricaneBoolean # Gibt an, ob ein Hurrikan startet
   hurricaneBoolean = False
   global hurricaneInAction # Gibt an, ob aktuell ein Hurrikan generiert wird
   hurricaneInAction = False

   # Generiert solange Daten, bis der "generatedDataFactor" erreicht ist, wird pro Datensatz
   # neu ausgeführt 
   while generateDataSets != generatedDataFactor: 
      # Alle 500 Datensätze wird dieser Erfolg dem Nutzer ausgegeben und zur Schonung 
      # der Kapazitäten eine Sekunde Pause eingelegt
      if int(generateDataSets) % 500 == 0 and generateDataSets != 0: 
         print(generateDataSets, Back.GREEN + " Datensätze generiert! \n")
         time.sleep(1)

      # Bestimmt ob ein Hurrikan stattfindet, oder nicht
      hurricaneChance = random.uniform(0,100)

      # Überprüft ob ein Hurrikan stattfindet oder ein neuer gestartet werden soll. Wenn 
      # dies nicht der Fall ist, wird die Abfrage ausgeführt.  
      if hurricaneChance > hurricaneProbability and hurricaneInAction == False:
         hurricaneBoolean = False
         # Die Datengenerierung wird mit der Information im "hurricaneBoolean" gestartet
         DataGeneration()

      # Überprüft ob ein Hurrikan stattfindet oder ein neuer gestartet werden soll. Wenn 
      # dies der Fall ist, wird die Abfrage ausgeführt.  
      elif hurricaneChance == hurricaneProbability or hurricaneChance < hurricaneProbability or hurricaneInAction == True:
         hurricaneBoolean = True
         # Die Datengenerierung wird mit der Information im "hurricaneBoolean" gestartet
         DataGeneration()
      
      # Bestätigt, dass ein Datensatz generiert wurde und addiert daraufhin einen weiteren
      # hinzu
      generateDataSets += 1
   
   # Führt die SaveData Funktion aus, die die Daten abschließend Speichert
   SaveData()

# Diese Funktion ist dafür Zuständig für die Datengenerierung die richtigen Funktionen 
# abzurufen
def DataGeneration():
   global getTemperatureData # Variable zum Verhindern von Endlosschleifen
   global getWindSpeedData # Variable zum Verhindern von Endlosschleifen
   global getAirPressureData # Variable zum Verhindern von Endlosschleifen
   global hurricaneInAction # Gibt an, ob aktuell ein Hurrikan generiert wird
   global hurricaneBoolean # Gibt an, ob ein Hurrikan startet
   global generateDataSets # Zählt, wie viele Datensätze bereits generiert wurden

   # Setzt die Varaibalen auf ihren Standardwert 
   getTemperatureData = True  
   getWindSpeedData = True
   getAirPressureData = True

   # F
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
        "Dataset": generateDataSets
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
   hurricaneMultiplicatorForTemperature = hurricaneMultiplicator / 2
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

            if hurricaneInAction == True and lastGeneratedTemperature * hurricaneMultiplicatorForTemperature <= temperatureMaximum:
               lastGeneratedTemperature = lastGeneratedTemperature * hurricaneMultiplicatorForTemperature

            if hurricaneInAction == True and lastGeneratedTemperature * hurricaneMultiplicatorForTemperature > temperatureMaximum:
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
   hurricaneMultiplicatorForWindSpeed = hurricaneMultiplicator / 2
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

      if isNightBoolean == True and (lastGeneratedWindSpeed/5) *6 >= windSpeedMinimal:
         lastGeneratedWindSpeed = (lastGeneratedWindSpeed/5) *6

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

            if isNightBoolean == True and (lastGeneratedWindSpeed/5) *6 >= windSpeedMinimal:
               lastGeneratedWindSpeed = (lastGeneratedWindSpeed/5) *6
            
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
            
            if isNightBoolean == True and (lastGeneratedWindSpeed/5)*6 <= windSpeedMaximum:
               lastGeneratedWindSpeed = (lastGeneratedWindSpeed/5)*6

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
          
          if hurricaneInAction == True and lastGeneratedAirPressure > 720:
            lastGeneratedAirPressure = round(random.uniform(675,720))
             

          if airPressureMinimal < lastGeneratedAirPressureMinimal:
            lastGeneratedAirPressure = round(random.uniform(lastGeneratedAirPressureMinimal, lastGeneratedAirPressureMaximum))

          elif airPressureMinimal > lastGeneratedAirPressureMinimal or airPressureMinimal == lastGeneratedAirPressureMinimal:
            lastGeneratedAirPressure += 25
            getAirPressureData = not getAirPressureData 
            GenerateAirPressure()

       elif lastGeneratedAirPressure > airPressureMeanValue or lastGeneratedAirPressure == airPressureMeanValue:
          
          if hurricaneInAction == True and lastGeneratedAirPressure > 720:
            lastGeneratedAirPressure = round(random.uniform(675,720))
          
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