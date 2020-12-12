print("Welcome To The Temprature Converter App")
tempF = float(input("Enter The Temprature In Farhenite :\t"))
tempC = (5/9)+(tempF - 32)
tempK = tempC + 273.15

tempF = round(tempF,2)
tempC = round(tempC,2)
tempK = round(tempK,2)

print("\n Temp In Farhenite:\t" + str(tempF))
print("\n Temp In Celcius:\t" + str(tempC))
print("\n Temp In Kelvin:\t" + str(tempK))