#Input height validation
MIN_h=1
MAX_h=300
rawheight=input('Enter your height in centimeter')
#Validate 
try:
    height=float(rawheight)
except ValueError:
    print(f"'{rawheight} is not a number. Please enter a value like 164")
    raise SystemExit(1)

if not MIN_h <= height <= MAX_h:
    print(f"{height} is outside the plausible range"
          f"({MIN_h} to {MAX_h}). Please check your entry.")
    raise SystemExit(1)

#Input weight validation
MIN_w=10
MAX_w=500
rawweight=input('Enter your height in kg')
#Validate 
try:
    weight=float(rawweight)
except ValueError:
    print(f"'{rawweight} is not a number. Please enter a value like 52")
    raise SystemExit(1)

if not MIN_w <= weight <= MAX_w:
    print(f"{weight} is outside the plausible range"
          f"({MIN_w} to {MAX_w}). Please check your entry.")
    raise SystemExit(1)

#BMI calculation
height_m = height/100
bmi=weight/(height_m**2)

#BMI Category
if bmi < 18.5:
    category="Underweight"
    advice="You might want to speak to your doctor about whether gaining some weight would benefit your health."
elif 18.5 < bmi < 24.9:
    category="Healthy weight"
    advice="This is great. Eating a healthy diet and being physically active are important for reducing your cancer risk, even at a healthy weight. For cancer prevention, you should aim for your BMI to be as low as you can within the healthy range."
elif 25.0 < bmi < 29.9:
    category="Overweight"
    advice="It’s likely your cancer risk will reduce by losing some weight. Aim to gradually lose weight by making healthy changes to your diet and adding in more activity. It’s best to speak to your doctor before making any major changes to your lifestyle."
else:
    category="Obesity"
    advice="It’s likely your cancer risk will reduce by losing some weight. Aim to gradually lose weight by making healthy changes to your diet and adding in more activity. It’s best to speak to your doctor before making any major changes to your lifestyle."
#print
print (f"Your BMI is {bmi:.1f}. This is usually classed as a {category}.\n"
       f"{advice}")