#Przejdź na stronę https://pyformat.info/ a następnie zapisz w oddzielnym pliku .py i wykonaj 
# 5 wybranych przykładów formatowania ciągów oznaczonego jako „New”, których nie było w przykładach z 
# tego podrozdziału (np. z wyrównaniem do prawej lub lewej strony, ilością pozycji liczby, znakiem, wypełnieniem spacji itp
# .). Przerób zaprezentowane tam przykłady tak, żeby korzystały z zapisu w postaci f-string.



from datetime import datetime


#1 
print(f'{"Xphonesss":10.5}!')
#2 
print(f'{3.141592653589793:f}')
#3 
print(f'{23:=+7d}')
#4 
print(f'{datetime.now():%Y-%m-%d %H:%M}')
#5 
print(f'{"tekst":{"^"}{20}}')