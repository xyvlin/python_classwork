Person1_name = "Alice"
Person1_is_male = False
Person1_height = 154
Person1_weight = 50

Person2_name = "Bob"
Person2_is_male = True
Person2_height = 170
Person2_weight = 68

Person3_name = "Charlie"
Person3_is_male = True
Person3_height = 165
Person3_weight = 55

Person4_name = "Diana"
Person4_is_male = False
Person4_height = 160
Person4_weight = 60

Person5_name = "Eve"
Person5_is_male = False
Person5_height = 158
Person5_weight = 52

Person6_name = "Frank"
Person6_is_male = True
Person6_height = 175
Person6_weight = 70

Person7_name = "Grace"
Person7_is_male = False
Person7_height = 168
Person7_weight = 58

Person8_name = "Hank"
Person8_is_male = True
Person8_height = 180
Person8_weight = 75

Person9_name = "Ivy"
Person9_is_male = False
Person9_height = 155
Person9_weight = 48

Person10_name = "Jack"
Person10_is_male = True
Person10_height = 172
Person10_weight = 65

#Start writing your code here. 
def calcBmi(w, h):
    return round(w / ((h / 100) ** 2),2)

def categorize(bmi):
    if bmi<18.5:
        return "Too Skinny"
    elif bmi<24.9:
        return "Normal"
    else:
        return "Too Fat"

def gender(g):
    if g: 
        return "his"
    else:
        return "her"

print(f"{Person1_name} is {Person1_height} cm and {Person1_weight} kg, so {gender(Person1_is_male)} BMI is {calcBmi(Person1_weight,Person1_height)}, which is {categorize(calcBmi(Person1_weight,Person1_height))}.")
print(f"{Person2_name} is {Person2_height} cm and {Person2_weight} kg, so {gender(Person2_is_male)} BMI is {calcBmi(Person2_weight,Person2_height)}, which is {categorize(calcBmi(Person2_weight,Person2_height))}.")
print(f"{Person3_name} is {Person3_height} cm and {Person3_weight} kg, so {gender(Person3_is_male)} BMI is {calcBmi(Person3_weight,Person3_height)}, which is {categorize(calcBmi(Person3_weight,Person3_height))}.")
print(f"{Person4_name} is {Person4_height} cm and {Person4_weight} kg, so {gender(Person4_is_male)} BMI is {calcBmi(Person4_weight,Person4_height)}, which is {categorize(calcBmi(Person4_weight,Person4_height))}.")
print(f"{Person5_name} is {Person5_height} cm and {Person5_weight} kg, so {gender(Person5_is_male)} BMI is {calcBmi(Person5_weight,Person5_height)}, which is {categorize(calcBmi(Person5_weight,Person5_height))}.")
print(f"{Person6_name} is {Person6_height} cm and {Person6_weight} kg, so {gender(Person6_is_male)} BMI is {calcBmi(Person6_weight,Person6_height)}, which is {categorize(calcBmi(Person6_weight,Person6_height))}.")
print(f"{Person7_name} is {Person7_height} cm and {Person7_weight} kg, so {gender(Person7_is_male)} BMI is {calcBmi(Person7_weight,Person7_height)}, which is {categorize(calcBmi(Person7_weight,Person7_height))}.")
print(f"{Person8_name} is {Person8_height} cm and {Person8_weight} kg, so {gender(Person8_is_male)} BMI is {calcBmi(Person8_weight,Person8_height)}, which is {categorize(calcBmi(Person8_weight,Person8_height))}.")
print(f"{Person9_name} is {Person9_height} cm and {Person9_weight} kg, so {gender(Person9_is_male)} BMI is {calcBmi(Person9_weight,Person9_height)}, which is {categorize(calcBmi(Person9_weight,Person9_height))}.")
print(f"{Person10_name} is {Person10_height} cm and {Person10_weight} kg, so {gender(Person10_is_male)} BMI is {calcBmi(Person10_weight,Person10_height)}, which is {categorize(calcBmi(Person10_weight,Person10_height))}.")