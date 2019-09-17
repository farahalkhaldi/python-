from datetime import date

def check_birthdate(day,month,year):

    today = date.today()
    if year > today.year:
        return False
    elif year == today.year and month > today.month:
        return False
    elif year == today.year and month == today.month and day > today.day:
        return False
    else:
        return True


def calculate_age(day,month,year):
    
    today = date.today()
    user_age_year = today.year - year
    if month > today.month:
        user_age_month = month - today.month
    else:
        user_age_month = today.month - month
    if day > today.day:
        user_age_day = day - today.day
    else:
        user_age_day = today.month - day

    print("You are {} Years, {} months and {} days years old ".format(user_age_year,user_age_month,user_age_day))



if __name__ == '__main__':

    user_year_of_birth = int(input("Enter Year Of Birth: "))
    user_month_of_birth = int(input("Enter Month Of Birth: "))
    user_day_of_birth = int(input("Enter Day Of Birth: "))

    check_correct_date = check_birthdate(user_day_of_birth,user_month_of_birth,user_year_of_birth)

    if check_correct_date is True:
        calculate_age(user_day_of_birth,user_month_of_birth,user_year_of_birth)
    else:
        print("Birthdate is Invalid")
