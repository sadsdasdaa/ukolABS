#Ukol A
print("Napište 3 jídla, ktere jste dneska během dne snědl.")
jidlo1 = input("První jídlo je ")
jidlo2 = input("Druhý jídlo je ")
jidlo3 = input("Třetí jídlo je ")
print("Napište kolik kalorií ma každe jídlo")
pocet_kalori1 = int(input("První jídlo má "))
pocet_kalori2 = int(input("Druhý jídlo má "))
pocet_kalori3 = int(input("Třetí jídlo má "))
celkove_kalorie = (pocet_kalori1+pocet_kalori2+pocet_kalori3)
print (celkove_kalorie)
#Ukol B
print("Napiste 2 aktivity: ")
aktivita1 = input("Aktivitu: ")
aktivita2 = input("Aktivitu: ")
print("Jaka je delka v minutech? ")
doba1 = int(input("Zadej dobu aktivity '{aktivita1}' v min: "))
doba2 = int(input("Zadej dobu aktivity '{aktivita2}' v min: "))
celkovy_vedej = (doba1 + doba2)*5
print(f"Celkem spalene kalorie {celkovy_vedej}")
#Společný
#Kyryl Andrieiev, Mykola Denysenko
print("Kolik kalori jste snědl/a ")
snedeno_kalori = int(input("Snědl/a jsem "))
print("Kolik spalil/a ")
spaleno_kalori = int(input("Spalil jsem "))
print("Napište jestli máte přebytek nebo nedostatek kalorii")
if input("Přebytek"):
    prebytek= int(input("Napište kolik kalori vam přebýva"))
if input("Nedostatek"):
    nedostatek= int(input("Napište o kolik kalori máte nedostatek"))
print(f"Snědl/a jsi {snedeno_kalori} a spálil/a {spaleno_kalori} kcal. Přebytek: {prebytek} kcal.")