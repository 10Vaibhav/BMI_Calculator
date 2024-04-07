
height = float(input("what is your height in meters ?? ex.1.75\n"))

weight = int(input("what is your weight in kilograms ?? ex.54\n"))


BMI = weight/(height*height)
if BMI <=18.5 :
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI <25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI <30 :
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <35 :
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is{BMI}, you are clinically obese.")

