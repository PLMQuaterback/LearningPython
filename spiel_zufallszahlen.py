#Erweiterung des Codes spiel_eingabe.py
#Modul random wird dafür bemötigt

import random

#Initialisierung des Generators

random.seed()


#Zufallswerte und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b 
print("Die Aufgabe:", a, "+", b)

#Eingabe
print("Bitte eine Zahl eingeben:")
z = input()

#Eingabe in Zahl umwandeln
zahl = int(z)

#Ausgabe
print("Ihre Eingabe ist:", z)
print("Ihr Ergebnis ist:", c)

