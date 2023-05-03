#Zadanie 7
#Korzystając z kodu umieszczonego poniżej oraz
# wykorzystując funkcję zdefiniowaną w zadaniu 6 napisz rozwiązanie,
# które będzie operowało na zwracanej kolejce z zadania 6, wykonując jej rotację,
# i wyświetlało tak jak w funkcji spinit aktualne wartości "koła fortuny", aż zatrzyma
# się na właściwym (można przyjąć, że będzie to pierwszy element kolejki). Wykonaj kilka
# obrotów kołem dla przetestowania kodu (wartości obrotu mogą być "na sztywno" lub losowane).
import random
from collections import deque, Counter
import time

def lot(los: deque, win: int):
    los.rotate(random.randint(0, len(los)))

    print(f"Maszyna losująca: {los}")
    if los[0] != win:
        time.sleep(1)
        lot(los, win)

def tab(*args):
    return deque(Counter(args).elements())
los = tab(9, 2, 3, 4, 5, 6, 7, 8, 1)
win = random.choice(los)

los.rotate(1)
lot(los, win)
print("Wygrana")