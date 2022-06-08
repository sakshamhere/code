import json

def Hrisk(bmi):
    if bmi <= 18.4:
        return 'Underweight','Malnutrition risk'
    elif bmi>= 18.5 and bmi<=24.9:
        return 'Normal weight','Low risk'
    elif bmi>= 25 and bmi<=29.9:
        return 'Overweight','Enhanced risk'
    elif bmi>= 30 and bmi<=34.9:
        return 'Moderately obese','Medium risk'
    elif bmi>= 35 and bmi<=39.9:
        return 'Severely obese ','High risk'
    else:
        return 'Very severely obese','Very high risk'

def BMI():
    file = open('data.json')
    jsn = json.load(file)
    OverweightCount=0
    for data in jsn:
        if data['WeightKg'] and data['HeightCm']:
            data['BMI'] = round(data['WeightKg']/(data['HeightCm']/100)**2,2)
            data['BMI Category'],data['Health risk'] = Hrisk(data['BMI'])
            if data['BMI Category']=='Overweight':
                OverweightCount+=1

    with open('result.json',"w") as file:
        json.dump(jsn,file)
    
    #return
    print(OverweightCount)


BMI() 

