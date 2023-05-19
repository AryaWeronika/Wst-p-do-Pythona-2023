#Zadanie 1
#Napisz wyrażenia regularne przeszukując plik strings.txt i znajdź:
#wszystkie liczby
#wszystkie liczby co najmniej 3 cyfrowe
#wszystkie adresy IPv4
#wszystkie wyrazy rozpoczynające się od wielkiej litery
#wszystkie linie z pliku, które mają co najmniej 4 wyrazy
#wszystkie adresy url
import re

with open('strings.txt', 'r') as file:
    data = file.read()

# Wszystkie liczby
numbers = re.findall(r'\d+', data)

# Wszystkie liczby co najmniej 3-cyfrowe
numbers_3_digits = re.findall(r'\d{3,}', data)

# Wszystkie adresy IPv4
ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', data)

# Wszystkie wyrazy rozpoczynające się od wielkiej litery
capitalized_words = re.findall(r'\b[A-Z]\w*\b', data)

# Wszystkie linie z pliku, które mają co najmniej 4 wyrazy
lines_with_4_words = re.findall(r'^(?:\S+\s+){3,}\S+$', data, re.MULTILINE)

# Wszystkie adresy URL
urls = re.findall(r'\b(?:https?|ftp)://\S+\b', data)

print("Wszystkie liczby:", numbers)
print("Wszystkie liczby co najmniej 3-cyfrowe:", numbers_3_digits)
print("Wszystkie adresy IPv4:", ip_addresses)
print("Wszystkie wyrazy rozpoczynające się od wielkiej litery:", capitalized_words)
print("Wszystkie linie z pliku, które mają co najmniej 4 wyrazy:")
for line in lines_with_4_words:
    print(line)
print("Wszystkie adresy URL:", urls)