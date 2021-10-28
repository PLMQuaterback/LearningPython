#prozentsatz von steuern von einem betrag x errechnen

#Eingabe
print("Geben Sie bitte Ihr Brutto Gehalt in € ein:")
gehalt = float(input())

print ("Geben SIe bitte den Steuersatz wie folgt ein 18% sind 0.18")

steuersatz = float(input())
#Berechnung

steuerbetrag = gehalt * steuersatz

#Ausgabe
print("Es ergibt sich eine Steuer von",
steuerbetrag, "Euro")

