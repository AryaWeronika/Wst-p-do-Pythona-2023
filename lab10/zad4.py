#Zadanie 4
#Napisz funkcję, która dla podanej daty wyświetli wiek w postaci: Dzisiaj masz X lat, Y miesięcy i Z dni. Do twoich kolejnych urodzin pozostało N dni.

from datetime import date

def calculate_age(birth_date):
    today = date.today()

    # Obliczenie wieku w latach, miesiącach i dniach
    age = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Korekta, jeśli urodziny jeszcze nie miały miejsca w tym roku
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
        months += 12

    # Korekta, jeśli dzisiaj jest wcześniejszy dzień w miesiącu niż data urodzin
    if today.day < birth_date.day:
        months -= 1
        days += 30

    # Obliczenie liczby dni do kolejnych urodzin
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if today > next_birthday:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    days_to_birthday = (next_birthday - today).days

    # Formatowanie wieku i dni do kolejnych urodzin
    age_str = f"Dzisiaj masz {age} lat, {months} miesięcy i {days} dni."
    days_to_birthday_str = f"Do twoich kolejnych urodzin pozostało {days_to_birthday} dni."

    return age_str, days_to_birthday_str

# Przykładowe użycie funkcji
birth_date = date(1999, 3, 16)
age, days_to_birthday = calculate_age(birth_date)
print(age)
print(days_to_birthday)