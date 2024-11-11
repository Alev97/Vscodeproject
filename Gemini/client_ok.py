import requests, json, sys

# base_url = "http://127.0.0.1:8080"

sModel = "gemini-1.5-pro-exp-0827"
base_url = "https://generativelanguage.googleapis.com/v1beta/models/" + sModel + ":generateContent?key="
sGoogleApiKey = "AIzaSyDKSmKwps-Nbvzkkk6ve7MrfQ2HZM4XwTk"
api_url = base_url + sGoogleApiKey


print("Benvenuti in Google Gemini")


iFlag = 0
while iFlag == 0:
    print("\nOperazioni disponibili:")
    print("1. Inserisci una domanda")
    print("2. Inserisci una coppia (file/domanda)")
    print("3. Esci")
 

    iOper = int(input("Scegli opzione: "))
    if iOper == 1:
        sQuery = input("Cosa vuoi chiedere? ")
        jsonDataRequest = {"contents": [{"parts": [{"text": sQuery}]}]}
        response = requests.post(api_url, json = jsonDataRequest, verify = True)
        if response.status_code == 200:
            print(response.json())
        else:
            print("Risposta errata!")


    elif iOper == 2:
        print("Servizio da gestire")
       

    elif iOper == 3:
        print("Buona giornata!")
        iFlag = 1 # iFlag da 0 diventa 1 così esce dal ciclo

    else:
        print("Operazione non disponibile, riprova.")

