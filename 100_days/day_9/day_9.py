
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
    }

print(programming_dictionary["Bug"])

programming_dictionary["Bug"] = "A moth in your computer";

print(programming_dictionary["Bug"])

# for loop will provide the key
for key in programming_dictionary:
    print(programming_dictionary[key])

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

#Dictionary Excercise
#TODO-1: Create an empty dictionary called student_grades.
#TODO-2: Write your code below to add the grades to student_grades.👇

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90 and score <= 100:
        student_grades[student] = "Outstanding"
    elif score > 80 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
