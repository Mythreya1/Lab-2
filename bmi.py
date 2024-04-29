def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / height**2

    print("Your BMI is " + str(bmi))
    if bmi < 18.5:
        print("-1")
    elif bmi > 25.0:
        print("1")
    else:
        print("0")

calculate_bmi(weight=57, height=1.73)

