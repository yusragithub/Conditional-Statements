height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = weight / (height / 100) ** 2
if bmi<= 18.4 : 
    print("You are under Weight")
elif bmi <= 24.9 :
    print("You are healthy")
elif bmi <= 29.9 :
    print("You are the fatest person in the world")
else :
    print("Eat less, care about other people also")