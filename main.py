from datetime import datetime

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