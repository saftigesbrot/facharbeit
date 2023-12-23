import random
import json
import datetime
from colorama import *
init(autoreset=True)

RandomMagnitudeDict = []
i = 0 
QuantityMagnitude =  500
print(Back.GREEN + " Das Programm arbeitet! ")

def MainDataGeneration(i):

    if i < QuantityMagnitude:
        # Formel, welche einen einen nahmen 0 Wert ausspuckt, und selten ausschlägt
        ProbabilityforNaturalDisaster = round(random.random()*20)

        if ProbabilityforNaturalDisaster < 1:
            NaturalDisaster(i, QuantityMagnitude)

        elif ProbabilityforNaturalDisaster > 1:
            RandomMagnitude = round(random.random()*0.5,1)
            i = i + 1
            NaturalDisasterBoolean = False
            SavingData(i, RandomMagnitude, NaturalDisasterBoolean)

    if i == QuantityMagnitude:
        SaveDataToJSON(i)

    elif i != QuantityMagnitude:
        MainDataGeneration(i)


def NaturalDisaster(i, QuantityMagnitude): 
    MaxLenghtofNaturalDisaster = QuantityMagnitude - i
    LenghtofNaturalDisaster = round(random.random()*MaxLenghtofNaturalDisaster)

    NaturalDisasterBoolean = True
    RandomMagnitude = 0.51

    for x in range(LenghtofNaturalDisaster):
        if RandomMagnitude == 10.0:
            MainDataGeneration(i)

        elif RandomMagnitude != 10.0:
            RandomMagnitude = round(random.uniform(RandomMagnitude,10),1)
            i = i + 1
            SavingData(i, RandomMagnitude, NaturalDisasterBoolean)

    MainDataGeneration(i)            


def SavingData(i, RandomMagnitude, NaturalDisasterBoolean):

    TodaysDatetime = datetime.datetime.now()

    RandomMagnitudeTime = TodaysDatetime + datetime.timedelta(hours=i)
    RandomMagnitudeTime = RandomMagnitudeTime.strftime("%d.%m.%Y %H:%M")

    StringifyMagnitudeValue = RandomMagnitude, RandomMagnitudeTime
    StringifyMagnitudeValue = str(StringifyMagnitudeValue)
            
    RandomMagnitudeDict.append(StringifyMagnitudeValue)
    
    if NaturalDisasterBoolean == False:
        MainDataGeneration(i)


def SaveDataToJSON(i):

    JSONData = json.dumps(RandomMagnitudeDict, indent=4)

    SavingFile = open("data.json", "w")
    SavingFile.write(JSONData)
    SavingFile.close()
    print(Back.GREEN + " Erfolgreich: ", i,"Datensätze erstellt!")
    exit()

MainDataGeneration(i)