import random
temperatureMinimal = -30
temperatureMaximum = 30
lastGeneratedTemperature = -30

lastGeneratedTemperatureMinimal = lastGeneratedTemperature - 2 
lastGeneratedTemperatureMaximum = lastGeneratedTemperature + 2

if temperatureMinimal < lastGeneratedTemperatureMinimal and temperatureMaximum > lastGeneratedTemperatureMaximum:
    lastGeneratedTemperature = round(random.uniform(lastGeneratedTemperatureMinimal, lastGeneratedTemperatureMaximum))
    print("Es wurde if ausgeführt")
else:
    print("Es wurde Else ausgeführt")

