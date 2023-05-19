#Zadanie 2
#Zapisz do pliku lokalnego zawartość przykładowego logu: https://github.com/elastic/examples/blob/master/Machine%20Learning/Security%20Analytics%20Recipes/suspicious_login_activity/data/auth.log

#Następnie napisz 'parser', wykorzystując wyrażenia regularne tam, gdzie to możliwe, aby wyciągać z każdej linii datę, adres ip,
# użytkownika lub usługę i komunikat. Zapisz do pliku csv datę w formacie RRRR-MM-DD HH:mm:ss, adres ip w formacie z kropkami,
# usługę/użytkownika bez PID (to wartość numeryczna wewnątrz []) i komunikat z cytowaniem (quoting dla csv).
import re
import csv
import requests

# Pobranie zawartości logu
url = "https://github.com/elastic/examples/blob/master/Machine%20Learning/Security%20Analytics%20Recipes/suspicious_login_activity/data/auth.log"
response = requests.get(url)
log_content = response.text

# Wyrażenia regularne do wyciągania danych
regex_pattern = r"(\w{3}\s+\d{2}\s\d{2}:\d{2}:\d{2}).*?(?:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-zA-Z0-9_-]+)(?:\[\d+\])).*?\"(.*?)\""

# Otwarcie pliku CSV do zapisu
csv_file = open("parsed_log.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
csv_writer.writerow(["Data", "Adres IP", "Użytkownik/Usługa", "Komunikat"])

# Parsowanie logu
matches = re.findall(regex_pattern, log_content)
for match in matches:
    date = match[0]
    ip = match[1] if match[1] else ""
    user_service = match[2] if match[2] else ""
    message = match[3]
    csv_writer.writerow([date, ip, user_service, message])

# Zamknięcie pliku CSV
csv_file.close()