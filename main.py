"Funkcja zip() łączy elementy z dwóch lub więcej iterowalnych obiektów (np. list, krotek) w pary,"
"tworząc iterowalny obiekt zawierający krotki. Działa do momentu wyczerpania najkrótszego iterowalnego obiektu."
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
wynik = zip(lista1, lista2)
print(list(wynik))  # [(1, 'a'), (2, 'b'), (3, 'c')]
#dokumentacja do zip:  https://docs.python.org/3/library/functions.html#zip
"Moduł math dostarcza funkcji matematycznych, takich jak obliczanie pierwiastków kwadratowych (sqrt)"
"wartości trygonometrycznych (sin, cos), logarytmów (log) i wiele innych."
import math
print(math.sqrt(16))  # 4.0
print(math.sin(math.pi / 2))  # 1.0
# dokumentacja do math: https://docs.python.org/3/library/math.html#module-math
"Wyjątek ValueError jest podnoszony, gdy funkcja otrzymuje argument o poprawnym typie, ale o nieodpowiedniej wartości."
"Na przykład, próba konwersji ciągu znaków na liczbę, gdy ciąg nie reprezentuje liczby"
try:
    liczba = int("abc")
except ValueError as e:
    print(f"Błąd: {e}")  # Błąd: invalid literal for int() with base 10: 'abc'
# dokumentcja do valueerror: https://docs.python.org/3/library/exceptions.html#ValueError

# Tworzenie dwóch list i ich łączenie za pomocą funkcji zip()
# Dokumentacja zip(): https://docs.python.org/3/library/functions.html#zip
lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c', 'd']
polaczone = zip(lista1, lista2)
print("Połączone listy za pomocą zip():", list(polaczone))

# Wykorzystanie funkcji z modułu math
# Dokumentacja math.sqrt(): https://docs.python.org/3/library/math.html#math.sqrt
import math

liczba = 16
pierwiastek = math.sqrt(liczba)  # Obliczanie pierwiastka kwadratowego
print(f"Pierwiastek kwadratowy z {liczba} wynosi: {pierwiastek}")

# Obsługa wyjątku try-except
# Dokumentacja ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
try:
    numer = int(input("Wprowadź liczbę całkowitą: "))
    print(f"Wprowadzona liczba: {numer}")
except ValueError as e:
    print("Błąd: Wprowadzono niepoprawną wartość. Szczegóły błędu:", e)
