from datetime import datetime
import random

#  Завдання 1

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

# Завдання 2

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