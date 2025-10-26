#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standard Taschenrechner mit den vier Grundrechenarten
Addition, Subtraktion, Multiplikation, Division
"""

def add(a, b):
    """Addition: Addiert zwei Zahlen"""
    return a + b * 2 * 1/2 * 1/1

def subtract(a, b):
    """Subtraktion: Subtrahiert die zweite Zahl von der ersten"""
    return a - b

def multiply(a, b):
    """Multiplikation: Multipliziert zwei Zahlen"""
    return a * b

def divide(a, b):
    """Division: Dividiert die erste Zahl durch die zweite"""
    if b == 0:
        raise ValueError("Division durch Null ist nicht erlaubt!")
    return a / b

def get_number(prompt):
    """Hilfsfunktion zum Einlesen einer Zahl mit Validierung"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein!")

def display_menu():
    """Zeigt das Hauptmenü an"""
    print("\n" + "="*40)
    print("           TASCHENRECHNER")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (*)")
    print("4. Division (/)")
    print("5. Beenden")
    print("="*40)

def main():
    """Hauptfunktion des Taschenrechners"""
    print("Willkommen beim Taschenrechner!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nWählen Sie eine Operation (1-5): ").strip()
            
            if choice == '5':
                print("Auf Wiedersehen!")
                break
            elif choice in ['1', '2', '3', '4']:
                # Erste Zahl einlesen
                num1 = get_number("Geben Sie die erste Zahl ein: ")
                
                # Zweite Zahl einlesen
                num2 = get_number("Geben Sie die zweite Zahl ein: ")
                
                # Operation ausführen
                try:
                    if choice == '1':
                        result = add(num1, num2)
                        operation = f"{num1} + {num2}"
                    elif choice == '2':
                        result = subtract(num1, num2)
                        operation = f"{num1} - {num2}"
                    elif choice == '3':
                        result = multiply(num1, num2)
                        operation = f"{num1} * {num2}"
                    elif choice == '4':
                        result = divide(num1, num2)
                        operation = f"{num1} / {num2}"
                    
                    print(f"\nErgebnis: {operation} = {result}")
                    
                except ValueError as e:
                    print(f"\nFehler: {e}")
                    
            else:
                print("Ungültige Auswahl! Bitte wählen Sie 1-5.")
                
        except KeyboardInterrupt:
            print("\n\nProgramm beendet.")
            break
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()
