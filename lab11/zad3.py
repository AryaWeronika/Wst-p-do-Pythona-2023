#Zadanie 3
#Napisz definicję dowolnej klasy bazując na poprzednich labach. Stwórz jej instancję i zapisz za pomocą
# modułu pickle do pliku binarnego. Załaduj ponownie jej stan.
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
person = Person("Weronika", 24)

# Zapisywanie do pliku binarnego za pomocą modułu pickle
with open("person.pickle", "wb") as file:
    pickle.dump(person, file)

# Wczytywanie stanu z pliku binarnego
with open("person.pickle", "rb") as file:
    loaded_person = pickle.load(file)

# Przykład użycia wczytanego obiektu
print(loaded_person)
loaded_person.greet()
loaded_person.increase_age()
print(loaded_person)