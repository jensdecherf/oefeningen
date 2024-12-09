# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# data = response.json()
# completed = data['completed']
# if completed == "False":
#     print("Er moet nog werk worden gedaan")
# print(data['title'])
# print(response.json()['title'])
# print(response.status_code)
# print(response.headers["Content-Type"])

# #Oefening desease.sh API
# import requests
# country = input("\ngeef een land: ")
# api_url = "https://disease.sh/v3/covid-19/countries/" + country
# response = requests.get(api_url)
# gevallen = response.json()['cases']
# doden = response.json()['deaths']
# hersteld = response.json()['recovered']
# print("\nAantal gevallen: ", gevallen)
# print("Aantal sterfgevallen: ", doden)
# print("Aantal herstelde patienten: ", hersteld)

# import requests
# import random
# api_url = "https://v2.jokeapi.dev/joke/Any/1"
# response = requests.get(api_url)
# data = response.json()

# while True:
#     mop = input("\nWil je een mop? Typ 'ja' voor een mop of typ 'nee' om te stoppen: ")
#     if mop == "nee":
#         break
#     if mop == "ja":
#         if data['type'] == 'twopart':
#             print("\n" + data['setup'])
#             print(data['delivery'])
#         elif data['type'] == 'single':
#             print("\n" + data['joke'])

# import requests

# seen_jokes = set()  # Om eerder ontvangen moppen op te slaan

# while True:
#     mop = input("\nWil je een mop? Typ 'ja' voor een mop of typ 'nee' om te stoppen: ")
#     if mop.lower() == "nee":
#         break
#     if mop.lower() == "ja":
#         api_url = "https://v2.jokeapi.dev/joke/Any"
#         response = requests.get(api_url)
#         data = response.json()

#         # Haal de mop op
#         if data['type'] == 'twopart':
#             joke = f"{data['setup']} {data['delivery']}"
#         elif data['type'] == 'single':
#             joke = data['joke']
#         else:
#             print("Onbekend graptype ontvangen.")
#             continue

#         # Controleer of de mop al eerder is ontvangen
#         if joke in seen_jokes:
#             print("\nDeze mop heb je al gehoord! Laten we een nieuwe proberen.")
#         else:
#             print("\n" + joke)
#             seen_jokes.add(joke)

# import requests
# api_url = "http://localhost:8085/data.json"
# response = requests.get(api_url)
# data = response.json()
# print(data)

import requests
API_KEY = "453056d75d4005ab741e7ce795437f1b"
city = input("\ngeef een stad: ")
api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(api_url)
data = response.json()
temperatuur = data['main']['temp']
beschrijving = data['weather'][0]['description']
vochtigheid = data['main']['humidity']
wind = data['wind']['humidity']
print(f"\nDe temperatuur is: {temperatuur} °C")
print("Het is vandaag: ", beschrijving)
print("De luchtvochtigheid = ", vochtigheid)

