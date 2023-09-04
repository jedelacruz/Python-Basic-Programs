#BMI checker
#this program lets you enter your height and weight and it calculates your bmi
#this program also lets you know what weight range do you belong

print("================ BMI Calculator ================")
print()
name = input("Enter your name: ")
age = input("Enter your age: ")
height = float(input("Enter your height in meter: "))
weight = float(input("Enter your weight in Kg: "))
bmi = (weight/height) / height
print()
print("==================== Result ====================")
print()
print("Name: " + name)
print("Age: " + age)
print("BMI: " + str(bmi))
if(bmi > 30):
    print("Weight Range: Obesity")
elif(bmi > 25):
    print("Weight Range: Overweight")
elif(bmi > 18.5):
    print("Weight Range: Healthy")
else:
    print("Weight Range: Underweight")
