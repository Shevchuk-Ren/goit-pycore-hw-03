from datetime import datetime, timedelta
import random
import re

#  TASK 1

def get_days_from_today(date):
    format = "%Y-%m-%d"
    current_date= datetime.today()
    
    try:
        datetime_date = datetime.strptime(date, format)
        difference = current_date.toordinal() - datetime_date.toordinal()
        return difference
    except ValueError:
        print(f"ValueError: Time date {date} has differend format. Try 'РРРР-ММ-ДД'")

print(get_days_from_today('2024-12-09'))
print(get_days_from_today('2021-10-09'))
print(get_days_from_today('2024.12.09')) # error

# TASK 2

def get_numbers_ticket(min: int, max: int, quantity: int):
    list_numbers = []
    try:
       for x in range(quantity):
          ticket_number = random.randint(min, max)

          if ticket_number in list_numbers:
              continue
          
          list_numbers.append(ticket_number)
       return list_numbers
    except TypeError:
        print(f"ValueError: Вхідні значення мають бути номерами")

    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print('Ваші лотерейні числа:', lottery_numbers)

#  TASK 3

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number: str):
    try:
        clean_number = re.sub(r'[^\d+]', '', phone_number)

        if not clean_number.find("+") == 0:
            if "38" in clean_number and clean_number.find("3") == 0:
                clean_number = '+' + clean_number
            else:
                clean_number = '+38' + clean_number
        return clean_number
    
    except TypeError:
        print('TypeError: string not found')
        

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
    
# TASK 4

def get_upcoming_birthdays(users):
    # Поточна дата
    today = datetime.today().date()
    # Дата через 7 днів
    next_week = today + timedelta(days=7)
    
    upcoming_birthdays = []
    
    for user in users:
        
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        if today <= birthday_this_year <= next_week:
            congratulation_date = birthday_this_year
            

            if congratulation_date.weekday() == 5: 
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  
                congratulation_date += timedelta(days=1)
            

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Doe", "birthday": "1985.07.28"},
    {"name": "Jane Smith", "birthday": "1990.07.30"},
    {"name": "John Doe", "birthday": "1985.08.01"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
