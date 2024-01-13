import json

def SearchAlgorithmen():
    with open('massDataGeneration.json','r') as file:
        obj = json.load(file)
    
    global countingHurrikans 
    countingHurrikans= 0
    global hurricaneCounterOne 
    hurricaneCounterOne = 0
    global hurricaneDatasetsOne 
    hurricaneDatasetsOne = []
    global hurricaneCounterTwo  
    hurricaneCounterTwo = 0
    global hurricaneDatasetsTwo 
    hurricaneDatasetsTwo = []
    global hurricaneCounterThree 
    hurricaneCounterThree = 0
    global hurricaneDatasetsThree 
    hurricaneDatasetsThree = []
    global hurricaneCounterFour 
    hurricaneCounterFour = 0
    global hurricaneDatasetsFour 
    hurricaneDatasetsFour = []
    global hurricaneCounterFive 
    hurricaneCounterFive = 0
    global hurricaneDatasetsFive 
    hurricaneDatasetsFive = []

    for dataSet in obj:
        time = dataSet["Time"]
        windDirection = dataSet["Wind-Direction"]
        waterTemperature = dataSet["Water-Temperature"]
        airTemperature = dataSet["Air-Temperature"]
        windSpeed = dataSet["Wind-Speed"]
        airPressure = dataSet["Air-Pressure"]
        dataset = dataSet["Dataset"]

        
        if windSpeed > 73 and windSpeed < 96 and airPressure > 720 and waterTemperature >= 26 and airTemperature == waterTemperature/2:
            # print("Am", time, "war ein Hurrikan mit der Stufe 1. Der Datensatz ist: ", dataset)
            # print(dataSet, "\n")
            hurricaneDatasetsOne.append(dataset)
            countingHurrikans += 1
            hurricaneCounterOne += 1

        if windSpeed > 95 and windSpeed < 111 and airPressure < 720 and airPressure > 708 and waterTemperature >= 26 and airTemperature == waterTemperature/2:
            # print("Am", time, "war ein Hurrikan mit der Stufe 2. Der Datensatz ist: ", dataset)
            # print(dataSet, "\n")
            hurricaneDatasetsTwo.append(dataset)
            countingHurrikans += 1
            hurricaneCounterTwo += 1

        if windSpeed > 110 and windSpeed < 131 and airPressure < 709 and airPressure > 694 and waterTemperature >= 26 and airTemperature == waterTemperature/2: 
            # print("Am", time, "war ein Hurrikan mit der Stufe 3. Der Datensatz ist: ", dataset)
            # print(dataSet, "\n")
            hurricaneDatasetsThree.append(dataset)
            countingHurrikans += 1
            hurricaneCounterThree += 1

        if windSpeed > 130 and windSpeed < 156 and airPressure < 710 and airPressure > 675 and waterTemperature >= 26 and airTemperature == waterTemperature/2:
            # print("Am", time, "war ein Hurrikan mit der Stufe 4. Der Datensatz ist: ", dataset)
            # print(dataSet, "\n")
            hurricaneDatasetsFour.append(dataset)
            countingHurrikans += 1
            hurricaneCounterFour += 1

        if windSpeed > 155 and airPressure < 676 and waterTemperature >= 26 and airTemperature == waterTemperature/2:
            # print("Am", time, "war ein Hurrikan mit der Stufe 5. Der Datensatz ist: ", dataset)
            # print(dataSet, "\n")
            hurricaneDatasetsFive.append(dataset)
            countingHurrikans += 1
            hurricaneCounterFive += 1

    CompareForecastWithSearch()


def CompareForecastWithSearch():

    global countingHurrikans 

    global hurricaneCounterOne 
    global hurricaneDatasetsOne 
    global hurricaneDatasetsOneCorrect
    hurricaneDatasetsOneCorrect = []
    hurricaneDatasetsOneInCorrect = []

    global hurricaneCounterTwo  
    global hurricaneDatasetsTwo 
    global hurricaneDatasetsTwoCorrect
    hurricaneDatasetsTwoCorrect = []
    hurricaneDatasetsTwoInCorrect = []

    global hurricaneCounterThree 
    global hurricaneDatasetsThree
    global hurricaneDatasetsThreeCorrect
    hurricaneDatasetsThreeCorrect = []
    hurricaneDatasetsThreeInCorrect = []

    global hurricaneCounterFour 
    global hurricaneDatasetsFour 
    global hurricaneDatasetsFourCorrect
    hurricaneDatasetsFourCorrect = []
    hurricaneDatasetsFourInCorrect = []

    global hurricaneCounterFive 
    global hurricaneDatasetsFive 
    global hurricaneDatasetsFiveCorrect
    hurricaneDatasetsFiveCorrect = []
    hurricaneDatasetsFiveInCorrect = []

    file = open('resultCache.json')
    cacheData = json.load(file)
    
    hurricaneSteps = 5
    hurricaneProofing = 1
    hurricaneProofingNumberStr = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

    while hurricaneSteps > hurricaneProofing or hurricaneSteps == hurricaneProofing:
        hurricaneProofingName = "predicted-hurricanes-" + str(hurricaneProofing) + "-datasets"

        for dataSetProofing in cacheData["forecast-data"][hurricaneProofingName]:
            
            # Funktioniert nicht (Erstellt die Variable nicht richtig)
            proofingDataset = "hurricaneDatasets" +  hurricaneProofingNumberStr[hurricaneProofing] 
            proofingDatasetCorrect = proofingDataset + "Correct"
            proofingDatasetInCorrect = proofingDataset + "InCorrect"

            print(proofingDataset)

            for hurricaneDataSet in proofingDataset:
                if dataSetProofing == hurricaneDataSet:
                    proofingDatasetCorrect.append(dataSetProofing)
                else:
                    proofingDatasetInCorrect.append(dataSetProofing)
        
        hurricaneProofing += 1
    # print("Incorrect: ", hurricaneDatasetsFourInCorrect)
    # print("Corect: ", hurricaneDatasetsFourCorrect)
SearchAlgorithmen()