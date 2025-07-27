import datetime

def get_weekday(day, month, year):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[datetime.date(year, month, day).weekday()]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    return today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

def draw_digital_date(day, month, year):
    digits = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': ['  *', '  *', '  *', '  *', '  *'],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', '***', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['***', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '***'],
        ' ': ['   ', '   ', '   ', '   ', '   ']
    }
    
    date_str = f"{day:02d}{month:02d}{year}"
    for line in range(5):
        print(' '.join(digits[char][line] for char in date_str))

if __name__ == "__main__":
    day = int(input("День: "))
    month = int(input("Месяц: "))
    year = int(input("Год: "))
    
    print(f"День недели: {get_weekday(day, month, year)}")
    print(f"Високосный: {'Да' if is_leap_year(year) else 'Нет'}")
    print(f"Возраст: {calculate_age(year, month, day)} лет")
    print("Дата на табло:")
    draw_digital_date(day, month, year)