# Importiert das "JSON" Modul -> Speichern/Lesen von Daten mit einer JSON Datei
import json

# Importiert das "colorama" Modul -> Farbiger Text in der Ausgabe / Konsole
from colorama import * 
init(autoreset=True) 

from pprint import pprint

def MainModell():
    with open('settings.json','r') as file: 
      obj = json.load(file)
   
    global generatedData
    savingFile = obj['general-settings']['saving-file']
    splittedFileName = savingFile.split(".")

    if type(savingFile) == str and splittedFileName.pop() == "json":
        print(Fore.GREEN + " Speicherdatei erfolgreich gelanden! ")
           
        with open(savingFile,'r') as file: 
            generatedData = json.load(file)
        
        SearchForHurrikans()

    else:
        print(Back.RED + " Speicherdatei konnten nicht gelanden werden! Exit Code 1 ")
        exit()

    
def SearchForHurrikans():
    global generatedData

    dataSetCounter = 0
    hurricaneCounter = 0

    hurricaneCounterOne = 0
    hurricaneDatasetsOne = []
    hurricaneCounterTwo = 0
    hurricaneDatasetsTwo = []
    hurricaneCounterThree = 0
    hurricaneDatasetsThree = []
    hurricaneCounterFour = 0
    hurricaneDatasetsFour = []
    hurricaneCounterFive = 0
    hurricaneDatasetsFive = []
    lastDataSet = generatedData.pop()["Dataset"]

    while dataSetCounter < lastDataSet:
        
        time = generatedData[dataSetCounter]["Time"]
        windDirection = generatedData[dataSetCounter]["Wind-Direction"]
        airTemperature = generatedData[dataSetCounter]["Air-Temperature"]
        waterTemperature = generatedData[dataSetCounter]["Water-Temperature"]
        windSpeed = generatedData[dataSetCounter]["Wind-Speed"]
        airPressure = generatedData[dataSetCounter]["Air-Pressure"]

        if waterTemperature > 24 and airPressure > 700 and windSpeed > 76:
            nextHurricane = dataSetCounter + 1
            hurricaneDatasetsOne.append(nextHurricane)
            hurricaneCounter += 1
            hurricaneCounterOne += 1
        
        elif waterTemperature > 24 and (airPressure > 706 and airPressure < 722) and (windSpeed > 91 and windSpeed < 131):
            nextHurricane = dataSetCounter + 1
            hurricaneDatasetsTwo.append(nextHurricane)
            hurricaneCounter += 1
            hurricaneCounterTwo += 1
        
        elif waterTemperature > 24 and (airPressure > 692 and airPressure < 711) and (windSpeed > 90 and windSpeed < 151):
            nextHurricane = dataSetCounter + 1
            hurricaneDatasetsThree.append(nextHurricane)
            hurricaneCounter += 1
            hurricaneCounterThree += 1

        elif waterTemperature > 24 and (airPressure < 710 and airPressure > 675) and (windSpeed > 110 and windSpeed < 176):
            nextHurricane = dataSetCounter + 1
            hurricaneDatasetsFour.append(nextHurricane)
            hurricaneCounter += 1
            hurricaneCounterFour += 1

        elif waterTemperature > 24 and airPressure > 674 and windSpeed > 135:
            nextHurricane = dataSetCounter + 1
            hurricaneDatasetsFive.append(nextHurricane)
            hurricaneCounter += 1
            hurricaneCounterFive += 1

        dataSetCounter += 1


    with open('resultCache.json', 'w') as file:
        forecastData = {
            "forecast-data": {
                "predicted-hurricanes": hurricaneCounter,
                "predicted-hurricanes-1": hurricaneCounterOne,
                "predicted-hurricanes-1-datasets": hurricaneDatasetsOne,  
                "predicted-hurricanes-2": hurricaneCounterTwo,
                "predicted-hurricanes-2-datasets": hurricaneDatasetsTwo, 
                "predicted-hurricanes-3": hurricaneCounterThree,
                "predicted-hurricanes-3-datasets": hurricaneDatasetsThree, 
                "predicted-hurricanes-4": hurricaneCounterFour,
                "predicted-hurricanes-4-datasets": hurricaneDatasetsFour, 
                "predicted-hurricanes-5": hurricaneCounterFive,
                "predicted-hurricanes-5-datasets": hurricaneDatasetsFive
            }
        }
        json.dump(forecastData, file, indent=4,)

MainModell()