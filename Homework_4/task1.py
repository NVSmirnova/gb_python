from sys import argv

skript_name, vyrabotka, stavka_h, bonus = argv
print("Your zp is: ", int(vyrabotka) * int(stavka_h) + int(bonus), "tygrikof")