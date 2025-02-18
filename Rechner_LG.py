def rechner():
    while True:
        try:
            zahl1 = float(input("Gib die erste Zahl ein: "))
            zahl2 = float(input("Gib die zweite Zahl ein: "))
            operator = input("Wähle den Operator (+, -, *, /): ")
            
            if operator == '+':
                ergebnis = zahl1 + zahl2
            elif operator == '-':
                ergebnis = zahl1 - zahl2
            elif operator == '*':
                ergebnis = zahl1 * zahl2
            elif operator == '/':
                while zahl2 == 0:
                    print("Fehler: Division durch Null. Bitte eine neue zweite Zahl eingeben.")
                    zahl2 = float(input("Gib die zweite Zahl erneut ein: "))
                ergebnis = zahl1 / zahl2
            else:
                print("Ungültiger Operator")
                continue
            
            print("Ergebnis:", ergebnis)
            
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben.")
            continue
        
        nochmal = input("Möchten Sie eine weitere Berechnung durchführen? (j/n): ").strip().lower()
        if nochmal != 'j':
            print("Programm beendet.")
            break

rechner()
