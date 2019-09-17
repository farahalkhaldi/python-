print("Welcome to the special recruitment program")

user_name = input("What's your name? ")
user_age = input("How old are you? ")
user_year_of_experience = input("How many years of experience do you have? ")

cv = {}
cv['skills'] = []
skills = ['Python','C++','Java','JavaScript','Css','Html']
selected_skills = []

print("skills")

for index , skill in enumerate(skills):
    skill_number =index+1
    print( str(skill_number) + '.' + skill)

user_skills_number_1 = int(input("Chose a skill from a bove by entering its number: "))
user_skills_number_2 = int(input("Chose a skill from a bove by entering its number: "))


selected_skills.append(skills[user_skills_number_1-1])
selected_skills.append(skills[user_skills_number_2-1])

cv['experience'] = user_year_of_experience
cv['skills'] = selected_skills
cv['name'] = user_name
cv['age'] = user_age


if int(cv['age']) > 25 and int(cv['age']) < 40:
    if int(cv['experience']) > 3:
        if 'Python' in cv['skills']:
            print("You have been accepted, " + cv['name'] + "." )
