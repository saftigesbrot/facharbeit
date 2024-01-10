# Importiert das "JSON" Modul -> Speichern/Lesen von Daten mit einer JSON Datei
import json

# Importiert das "colorama" Modul -> Farbiger Text in der Ausgabe / Konsole
from colorama import * 
init(autoreset=True) 

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
    lastDataSet = generatedData.pop()["Dataset"]

    while dataSetCounter < lastDataSet:
        
        time = generatedData[dataSetCounter]["Time"]
        windDirection = generatedData[dataSetCounter]["Wind-Direction"]
        airTemperature = generatedData[dataSetCounter]["Air-Temperature"]
        waterTemperature = generatedData[dataSetCounter]["Water-Temperature"]
        windSpeed = generatedData[dataSetCounter]["Wind-Speed"]
        airPressure = generatedData[dataSetCounter]["Air-Pressure"]

        if waterTemperature > 24 and airPressure > 700 and windSpeed > 60:
            print("Hurrikan der Stufe 1 Wahrscheinlich im nächsten Datensatz. Aktueller Datensatz: ", dataSetCounter)
            hurricaneCounter += 1

        

        dataSetCounter += 1

    with open('result.json', 'w') as file:
        data = []
        print(data)
        forecastData = {
            "forecast-data": {
                "predicted-hurricanes": 0,
                "predicted-hurricanes-1": 0,
                "predicted-hurricanes-2": 0,
                "predicted-hurricanes-3": 0,
                "predicted-hurricanes-4": 0,
                "predicted-hurricanes-5": 0       
            }
        }
        data.append(forecastData)
        json.dump(forecastData, file, indent=4)

MainModell()