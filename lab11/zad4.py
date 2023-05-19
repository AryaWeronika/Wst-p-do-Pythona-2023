#Zadanie 4
#Stwórz listę kilku instancji obiektów z zadania 3 i ponownie serializuj listę obiektów do pliku i
# ją ponownie odczytać do tej samej postaci.
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

    def increase_age(self):
        self.age += 1

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

# Tworzenie instancji klasy Person
person1 = Person("Weronika", 24)
person2 = Person("Bob", 30)
person3 = Person("Charlie", 35)

# Tworzenie listy obiektów
people = [person1, person2, person3]

# Serializacja listy obiektów do pliku binarnego za pomocą modułu pickle
with open("people.pickle", "wb") as file:
    pickle.dump(people, file)

# Wczytywanie stanu z pliku binarnego
with open("people.pickle", "rb") as file:
    loaded_people = pickle.load(file)

# Przykład użycia wczytanej listy obiektów
for person in loaded_people:
    print(person)
    person.greet()