def rechner():
    while True:
        try:
            zahl1 = float(input("Gib die Länge in cm an: "))
            zahl2 = float(input("Gib die Breite in cm an: "))
            ergebnis = zahl1 * zahl2
            print("Ergebnis:", ergebnis, "Quadratcentimeter")
            break
            
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben.")

rechner()