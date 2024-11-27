#printoefening les 1
#print('hello world')
#print('mijn naam is')

#variabele aanduiden met =
#Begroetingsbericht='Goedemorgen deze morgen'
#print(Begroetingsbericht)

#Abrakadabra='Dit is een goochelspreuk'
#print('goochelspreuk')
#print(Abrakadabra)

#nummers
#an_int = 2
#a_float = 2.1

#print(an_int+3)
#print(a_float+2.1)

#nummers oefening
#release_year = 2001
#runtime = 10
#rating_out_of_10 = 7.0

#Berekeningen
#coffee_price = 1.50
#number_of_coffees = 4

#print(coffee_price * number_of_coffees)
#print(coffee_price)
#print(number_of_coffees)

#coffee_price = 2

#print(coffee_price * number_of_coffees)
#print(coffee_price)
#print(number_of_coffees)

#spaties creeren tussen variabelen
#een mogelijkheid:
#a = 'de les' 
#b = 'is leuk' 
#print(a+' '+b)

gestapte_kms = 12
gestapte_kms +=2
gestapte_kms +=3
#print (gestapte_kms)

#my_age = 35
#half_my_age = my_age/2
#greeting = 'Hallo daar' 
#name = 'Jens'
#greeting_with_name = greeting +' '+ name 
#print (half_my_age)
#print (greeting_with_name)

#my_baby_bool = "true"
#print(type(my_baby_bool))
#my_baby_bool_two = True
#print(type(my_baby_bool_two))

#user_name = "Dave"
#if user_name == "Dave":
#    print("Get of my computer Dave!")

x = 20
y = 20
#if x==y:
    #print("getallen zijn gelijk")
#if x!=y:
    #print("getallen zijn niet gelijk")

#Credits = 121
#if Credits >= 120:
   # print("je hebt genoeg credits")
#if Credits < 120:
 #   print("je hebt niet genoeg credits")

#if x==20 and y==20:
    #print("getallen zijn gelijk aan 20")
#if x==20 or y==20:
    #print("één van de getallen is gelijk aan 20")
#if not x==20 and y==20:
    #print("beide getallen moeten 20 zijn!")

#grade = 61

#if grade >= 90:
#    print("A")
#elif grade >= 80:
#    print("B")
#elif grade >= 70:
#    print("C")
#elif grade >= 60:
#    print("D")
#else:
#    print("F")

#a = 12
#b = 2
#print(a + b) 
#print(a - b)
#print(a * b)
#print(a / b)

#naam = input("Wat is je naam? ")
#print(naam)
#gewicht = int(input("Wat is je gewicht? "))
#lengte = int(input("Wat is je lengte? "))
#print(lengte + gewicht)

#nummer = int(input("Voer een getal in "))
#if nummer % 2 == 0:
#    print("dit is een even getal")
#else:
#   print("dit is een oneven getal")

#gewicht = float(input("Wat is je gewicht? "))
#lengte = float(input("Wat is je lengte? "))
#BMI = (gewicht/(lengte*lengte))
#print(BMI)

#celsius = float(input("Wat is de temperatuur in Celsius? "))
#fahrenheit = ((celsius * (9/5))+32)
#print (fahrenheit)

#originele_prijs = float(input("Wat is de originele prijs van dit product? "))
#prijs_met_korting = originele_prijs * 0.8
#print("De prijs met korting is") 
#print(prijs_met_korting)

#voorbeeld van een lijst:
#sam_height_and_testscore ["Sam", 67, 85.5, True]
 
#een lege lijst:
#empty_list = []

#.append gebruiken om zaken achteraf toe te voegen aan een lijst
#orders = ["daisies", "periwinkle"]
#orders.append("tulips")
#orders.append("roses")
#print(orders)

#2 lijsten samenvoegen
#my_list = [1, 2, 3]
#my_list_new = my_list + [4, 5]
#print(my_list_new)

#om een bv derde element uit een lijst weer te geven (n+1):
#print(my_list_new[2])

#selecteer het 4de element uit de lijst studenten
#studenten = ["Jef", "Bram", "Joske", "Marie"]
#student_vier = (studenten[3])
#print (student_vier)

#laatste element uit de lijst raadplegen (index -1)
#print (studenten[-1])

#voorlaatste element uit de lijst raadplegen (index -2)
#print (studenten[-2])

#lijst bewerken: 3de item in een lijst vervangen bv
#garden = ["Tomatoes", "Green Breans", "Cauliflower", "Grapes"]
#garden[2] = "Strawberries"
#print(garden)

#Een item verwijderen uit een lijst via .remove
#garden.remove("Grapes")
#print(garden)

#een sequentie van integers aanmaken in een lijst via een range
#my_range = range(0,100,5)
#print(list(my_range))

#De lengte van een lijst (of aantal items in een lijst tellen), kan je via het commando len
#print(len(my_range))

#sliced list
#print(my_range[1:8])

#sort() = een lijst gaan sorteren. vb:
#sorted_garden = sorted(garden)
#print(sorted_garden)

#oefening
#getallen = []
#getallen.append("2")
#getallen.append("1")
#getallen.append("3")
#getallen.append("4")
#getallen.append("5")
#getallen.pop(2)
#print(getallen)

#oefening 2:
#studenten = ["Jef", "Bram", "Joske","Alice", "Marie"]
#studenten.remove("Alice")
#print(studenten)

#oefening 3 met de lijst uit oefening 1
#getallen.sort()
#print(getallen)

#oefening 4
#getallen = []
#getallen.append("1")
#getallen.append("2")
#getallen.append("3")
#getallen.append("4")
#getallen.append("5")
#getallen.pop(2)
#getallen.insert(1,"6")
#getallen.remove("2")
#print(getallen)

#oefening 5 (met "% 2" ga je de restwaarde gaan controleren of deze 2 is of niet)
#nummers = [1,2,3,4,5]
#if nummers[0] % 2 == 0:
#    print ("Even getal:",nummers[0])
#else:
#    print ("Oneven getal:",nummers[0])
#if nummers[1] % 2 == 0:
#   print ("Even getal:",nummers[1])
#else:
#    print ("Oneven getal:",nummers[1])
#if nummers[2] % 2 == 0:
#    print ("Even getal:",nummers[2])
#else:
#    print ("Oneven getal:",nummers[2])
#if nummers[3] % 2 == 0:
#    print ("Even getal:",nummers[3])
#else:
#    print ("Oneven getal:",nummers[3])
#if nummers[4] % 2 == 0:
#    print ("Even getal:",nummers[4])
#else:
#    print ("Oneven getal:",nummers[4])

#oefening 6
#studenten = [85,92,78,90,88,76,89,95,80]
#studenten.append(84)
#studenten.remove(76)
#studenten.insert(2,91)
#studenten.sort()
#print(studenten)
#print(sum(studenten)/len(studenten)) 
#hoogste_waarde = max(studenten)
#print(hoogste_waarde)
#if hoogste_waarde > 90:
#    studenten[0] += 5
#    studenten[1] += 5
#    studenten[2] += 5
#    studenten[3] += 5
#    studenten[4] += 5
#    studenten[5] += 5
#    studenten[6] += 5
#    studenten[7] += 5
#    studenten[8] += 5
#    studenten[9] += 5
#print(studenten)
#print(sum(studenten)/len(studenten))


#Voorbeeld van een for-loop:
#studenten = ["Jef", "Bram", "Joske","Alice", "Marie"]
#for student in studenten:
#   print(student)

#for temp in range(6):
#    print ("loop") + str(temp + 1)

#Voorbeeld van een while-loop
#count = 0
#while count <= 3:
#    print (count)
#    count +=1

#Alle elementen printen met een while-loop:
#studenten = ["Jef", "Bram", "Joske","Alice", "Marie"]
#length = len(studenten)
#index = 0
#while index < length:
#    print(studenten[index])
#    index +=1

#Een bepaald element uit een lijst printen met een break:
#print("Lijst aan het checken...")
#studenten = ["Jef", "Bram", "Joske","Alice", "Marie"]
#for student in studenten:
# if student == "Bram":
#    print("Gevonden...")
#    break
#print("Klaar...")

#Oefening 1
#squares = []
#single_digits = range(0,11)
#for every_digit in single_digits:
#    print(every_digit)
#    squares.append(every_digit*2)
#print(squares)

#Oefening 2: Patroonafdruk
#for i in range(1, 6):
#    print('*' * i)

#def weather_check():
#    print("Het is een mooie dag")
#    print('waarschuwing: het zal regenen')
#weather_check()

#Oefening Gehele getallen
# Lijst om de even getallen op te slaan
#even_getallen = []

# Vraag de gebruiker om 10 gehele getallen in te voeren
#for i in range(10):
#    getal = int(input("Voer geheel getal in:1 "))
#    # Controleer of het getal even is
#    if getal % 2 == 0:
#        even_getallen.append(getal)

# Bereken het gemiddelde van de even getallen, als er even getallen zijn
#if even_getallen:
#    gemiddelde = sum(even_getallen) / len(even_getallen)
#    print("De even getallen zijn:", even_getallen)
#    print("Het gemiddelde van de even getallen is:", gemiddelde)
#else:
#    print("Er zijn geen even getallen ingevoerd.")

#Oefening
#even_getallen = []
#lijst_getallen = [2,5,6,8,9,12,13,14]
#for getal in lijst_getallen:
#    if getal % 2 == 0:
#        even_getallen.append(getal)
#print(even_getallen)

#even_getallen = []
#for getal in range(1,11):
#    if getal % 3 == 0:
#        continue
#    if getal % 2 == 0:
#        even_getallen.append(getal)

#getallen = 11
#while getallen <= 20:
#    if getallen % 2 == 0:
#        even_getallen.append(getallen)
#    getallen += 1   
#    if getallen % 3 == 0:
#        continue
#    if getallen == 17:
#        break
#print(even_getallen)


#Oefening
# invoer_getallen = []

# # Vraag de gebruiker om 10 gehele getallen in te voeren
# for getal in range(100):
#     getal = int(input("Voer geheel getal in: "))
#     invoer_getallen.append(getal)
#     if sum(invoer_getallen) >= 100:
#         break
# print("Het totaal is", sum(invoer_getallen))

#Oefening
# for getal in range(1,21):
#     print(getal)
#     if getal == 13:
#         print("Het getal 13 is gevonden")
#         break

#Splitten
# test = "santana"
# test2 = test.split("n")
# print(test2)

