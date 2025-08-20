# BMI Calculation
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"{bmi: .2f} You are underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"{bmi: .2f} You have a normal weight.")
elif 25 <= bmi < 29.9:
    print(f"{bmi: .2f} You are overweight")
else:
    print(f"{bmi: .2f} You are obese.")