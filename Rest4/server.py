from flask import Flask, json, request
import requests
from myjson import JsonSerialize, JsonDeserialize

sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)


@api.route('/pippo', methods=['GET'])
def GestisciPippo():
    myresponse = requests.get("https://www.google.it")
    return myresponse


@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    # prendi i dati della richiesta
    content_type = request.headers.get('Content_Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto " + sCodiceFiscale)
        # carichiamo l'anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            JsonSerialize(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error":"000", "Msg":"OK"}
            return json.dumps(jResponse),200
        else:
            jResponse = {"Error":"001+", "Msg":"Codice fiscale già presente in anagrafe"}
            return json.dumps(jResponse),200
    else:
        return "Errore, fromato non riconsciuto",401
    # controlla che il cittadino  non è gia presente in anagrafe

    # rispondi 

@api.route('/get_dati_citt', methods=['GET'])
def GestisciChiedidaticittadino():
    content_type = request.headers.get('Content_Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == "application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto " + sCodiceFiscale)
        # carichiamo l'anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale in dAnagrafe:
            # dAnagrafe[sCodiceFiscale] = jRequest
            # JsonSerialize(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error":"000", "Msg":dAnagrafe[sCodiceFiscale] }
            return json.dumps(jResponse),200
        else:
            jResponse = {"Error":"001+", "Msg":"Hai inserito un cf inesistente"}
            return json.dumps(jResponse),200
    else:
        return "Errore, fromato non riconsciuto",401


api.run(host="127.0.0.1", port = 8081)