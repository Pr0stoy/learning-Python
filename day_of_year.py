def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if is_year_leap(year) and month == 2:
        return 29
    elif not is_year_leap(year) and month == 2:
        return 28
    elif (month < 8 and month % 2 != 0) or (month >= 8 and month % 2 == 0):
        return 31
    else:
        return 30
def day_of_year(year, month, day):
    if  day < 1 or month < 1 or month > 12 or day > days_in_month(year,month):
        return None
    else: 
        sum = 0
        for i in range(1,month):
            sum += days_in_month(year,i)        
        sum += day
        return sum

# Tests
print(day_of_year(2000, 1, 1))    # Expected: 1
print(day_of_year(2000, 2, 29))   # Expected: 60 (Leap year)
print(day_of_year(2021, 3, 1))    # Expected: 60 (Non-leap year)
print(day_of_year(2024, 12, 31))  # Expected: 366
print(day_of_year(2023, 2, 29))   # Expected: None (Invalid date)
print(day_of_year(2024, 13, 35))   # Expected: None (Invalid date)