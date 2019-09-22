import datetime 


today_date = datetime.datetime.today()

def check_birthdate(day,month,year):
    if year > today_date.year:
        return False
    elif year == today_date.year and month > today_date.month:
        return False
    elif year == today_date.year and month == today_date.month and day > today_date.day:
        return False
    else:
        return True



def calculate(day,month,year):
    year_dif = today_date.year - year
    month_dif = today_date.month - month
    day_dif = today_date.day - day
    if year_dif >= 0 :
        if month_dif < 0:
            year_dif = year_dif - 1
        else:
            year_dif = year_dif         
    else:
        print("the birthdate is invalid")

    if month_dif < 0: 
        month_dif = 12 + month_dif


    if day_dif > 0: 
        day_dif = 30 - day_dif
    elif day_dif < 0:
        day_dif += 30
    else:
        day_dif = 0
        print("happy birthday")
        
        
    answer= "you are {} years {} months and {} days old".format(year_dif,month_dif,day_dif) 
    print(answer)





if __name__ == '__main__':

    year = int(input("Enter Year Of Birth: "))
    month = int(input("Enter Month Of Birth: "))
    day = int(input("Enter Day Of Birth: "))

    check_correct_date = check_birthdate(day,month,year) 

    if check_correct_date is True:
        calculate(day,month,year) 
    else:
        print("Birthdate is Invalid")


