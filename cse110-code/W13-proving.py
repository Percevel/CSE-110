import math
def wind_chill(temp,wind):
    return(35.74+ 0.6215*temp- 35.75*(wind**.16)+0.4275*temp*(wind**.16))

def f_to_c(farin):
    return((farin*9/5)+32)

temper = float(input("What is the temperature? "))
FC = input("Fahrenheit or Celsius (F/C)? ")
if FC.lower() == "c":
        temper = f_to_c(temper)
for x in range(0,61,5):
    print(f"At temperature {temper:.2f}F, and wind speed {x} mph, the windchill is: {wind_chill(temper,x):.2f}F")