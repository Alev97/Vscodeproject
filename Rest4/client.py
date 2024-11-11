import json, requests
import sys

base_url = "http://127.0.0.1:8081"

def RichiediDatiCittadino():
    nome = input("Inserisci nome cittadino: ")
    cognome = input("Inserisci cognome cittadino: ")
    dataNascita = input("Inserisci data nascita: ")
    codFiscale = input("Inserisci codice fiscale: ")
    jRequest = {"nome": nome, "cognome": cognome, "data nascita": dataNascita, "codice fiscale": codFiscale}
    return jRequest

def RichediCfCittadino():
    codFiscale = input("Inserisci codice fiscale: ")
    jRequest = {"codice fiscale":codFiscale}
    return jRequest

def ModificaDatiCittadino():
    codFiscale= input("Inserisci codice fiscale: ")
    jRequest = {"codice fiscale":codFiscale}
    return jRequest


def CreaInterfaccia():
    print("Operazioni disponibili")
    print("1. Inserisci cittadino(es. atto di nascita)")
    print("2. Richiedi dati cittadino (es. cert. residenza)")
    print("3. Modifica dati cittadino")
    print("4. Elimina cittadino")
    print("5. Exit")

CreaInterfaccia()
sOper = input("Selezione operazione ")
while (sOper != "5"):
    if sOper == "1":
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = RichiediDatiCittadino()
        try:
            response = requests.post(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")

    elif sOper == "2":
        api_url = base_url + "/get_dati_citt"
        jsonDataRequest = RichediCfCittadino()
        try:
            response = requests.get(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
    
    elif sOper =="3":
        api_url = base_url + "/mod_dati_citt"
        jsonDataRequest = ModificaDatiCittadino()
        


    CreaInterfaccia()
    sOper = input("Seleziona operazione ")