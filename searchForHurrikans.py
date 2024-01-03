import json

def SearchAlgorithmen():
    with open('massDataGeneration.json','r') as file:
        obj = json.load(file)
    
    countingHurrikans = 0

    for dataSet in obj:
        time = dataSet["Time"]
        windDirection = dataSet["Wind-Direction"]
        temperature = dataSet["Temperature"]
        windSpeed = dataSet["Wind-Speed"]
        airPressure = dataSet["Air-Pressure"]
        dataset = dataSet["Datasets"]
        
        if windSpeed > 73 and windSpeed < 96 and airPressure > 720 and temperature >= 26:
            print("Am", time, "war ein Hurrikan mit der Stufe 1. Der Datensatz ist: ", dataset)
            print(dataSet, "\n")
            countingHurrikans += 1

        if windSpeed > 95 and windSpeed < 111 and airPressure < 720 and airPressure > 708 and temperature >= 26:
            print("Am", time, "war ein Hurrikan mit der Stufe 2. Der Datensatz ist: ", dataset)
            print(dataSet, "\n")
            countingHurrikans += 1

        if windSpeed > 110 and windSpeed < 131 and airPressure < 709 and airPressure > 694 and temperature >= 26:
            print("Am", time, "war ein Hurrikan mit der Stufe 3. Der Datensatz ist: ", dataset)
            print(dataSet, "\n")
            countingHurrikans += 1

        if windSpeed > 130 and windSpeed < 156 and airPressure < 710 and airPressure > 675 and temperature >= 26:
            print("Am", time, "war ein Hurrikan mit der Stufe 4. Der Datensatz ist: ", dataset)
            print(dataSet, "\n")
            countingHurrikans += 1

        if windSpeed > 155 and airPressure < 676 and temperature >= 26:
            print("Am", time, "war ein Hurrikan mit der Stufe 5. Der Datensatz ist: ", dataset)
            print(dataSet, "\n")
            countingHurrikans += 1

    print(countingHurrikans)
SearchAlgorithmen()