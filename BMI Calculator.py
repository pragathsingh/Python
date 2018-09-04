weight = float(raw_input('Tell me your Weight : '))
height = float(raw_input('Tell me your  Height : '))

#1 ft = 0.3048 m
#1 m = 3.2808399 ft
#1 inch = 0.0254 m

def HealthDefining(CurrentBmi):
    answer = ""
    if CurrentBmi >= 25:
        answer= "Over Weight"
    if CurrentBmi <= 24.9:
        answer = "Healthy"
    return answer

def FeetToMeter(feet):
    return feet * 0.3048

bmi = weight/(FeetToMeter(height)**2)
print '\nYour Bmi is : '+str(bmi) +"\n According to it you are " + HealthDefining(bmi)


