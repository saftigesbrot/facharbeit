import json
import random
import datetime
import time
from datetime import date, timedelta

generatedDataFactor = 1000
StartDate = "2023-04-23 15:18:28.044869"
generatedData = []
# generatedData: Durch len(generatedData) kann die Anzahl der Tage welche bereits generiert wurde bestimmt werden

def MainGeneration():

   GeneratedDataSets = 0
   while GeneratedDataSets != generatedDataFactor:

    if GeneratedDataSets == 0:
       lastGeneratedTime = StartDate
    else:
       lastGeneratedLen = len(generatedData) - 1 #Weil er bei 0 beginnt zu zählen
       lastGeneratedTime = generatedData[lastGeneratedLen]
        # Beachten, dass durch neue Daten dies nicht mehr funktioniert, da die Time in der Json verrückt wird
    
    NewTime = datetime.datetime.strptime(lastGeneratedTime, "%Y-%m-%d %H:%M:%S.%f") + timedelta(minutes=1)

    StringifyNewTime = str(NewTime)
    generatedData.append(StringifyNewTime)

    GeneratedDataSets = GeneratedDataSets + 1
   
   SaveData()
   

def SaveData():
    JSONData = json.dumps(generatedData, indent=4)

    SavingFile = open("massDataGeneration.json", "w")
    SavingFile.write(JSONData)
    SavingFile.close()

MainGeneration()