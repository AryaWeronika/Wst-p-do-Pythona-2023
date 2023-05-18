#Zadanie 3
#Napisz skrypt, który będzie pytał użytkownika o czas (format HH:MM:SS), który następnie zostanie wyświetlony dla 4 poniższych
# miejsc (stref czasowych): Tokyo, Waszyngton, Sydney, Londyn.

from datetime import datetime
import pytz

def convert_time(time_str, timezone):
    # Pobranie obecnej daty i godziny
    now = datetime.now()

    # Konwersja podanego czasu na obiekt datetime
    time = datetime.strptime(time_str, '%H:%M:%S').time()

    # Połączenie daty i czasu
    combined_datetime = datetime.combine(now.date(), time)

    # Ustawienie strefy czasowej
    timezone = pytz.timezone(timezone)
    localized_datetime = timezone.localize(combined_datetime)

    return localized_datetime

# Pytanie użytkownika o czas
user_time_str = input("Podaj czas w formacie HH:MM:SS: ")

# Konwersja czasu dla różnych stref czasowych
timezones = {
    'Tokyo': 'Asia/Tokyo',
    'Waszyngton': 'America/New_York',
    'Sydney': 'Australia/Sydney',
    'Londyn': 'Europe/London'
}

for city, timezone in timezones.items():
    converted_time = convert_time(user_time_str, timezone)
    formatted_time = converted_time.strftime('%H:%M:%S')
    print(f"Czas w {city}: {formatted_time}")