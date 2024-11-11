from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize

api = Flask(__name__)


file_path = "anagrafe.json"
cittadini = JsonDeserialize(file_path)

file_path_users = "utenti.json"
utenti = JsonDeserialize(file_path_users)


@api.route('/login', methods = ['POST'])
def GestisciLogin():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        # dizionario: ("username":"....", "password":"....")
        jsonReq = request.json
        sUsernameInseritoDaClient = jsonReq["username"]
        if sUsernameInseritoDaClient in utenti:
            sPasswordInseritaDaClient = jsonReq["password"]
            if sPasswordInseritaDaClient == utenti[sUsernameInseritoDaClient]["password"]:
                sPrivilegio = utenti[sUsernameInseritoDaClient]["privilegi"]
                return jsonify({"Esito": "000", "Msg": "Utente registrato", "Privilegio":sPrivilegio}), 200
            else:
                # username giusto, password errata
                return jsonify({"Esito": "001", "Msg": "Credenziali errate"})
        else:
            # username errato, password giusta
            return jsonify({"Esito": "001", "Msg": "Credenziali errate"})
    else:
        return jsonify({"Esito": "001", "Msg": "Formato rischiesta errato"})




@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        """
        prima verifico utente, password e privilegi,
        dove l'username e password me l'ha inviato il client
        mentre il privilegio lo vado a leggere nel file {utenti.json}
        """
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            return jsonify({"Esito": "001", "Msg": "Cittadino già esistente"}), 200
        else:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path) 
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200




@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale):
    """
    prima verifico utente, password e privilegi,
    dove l'username e password me l'ha inviato il client
    mentre il privilegio lo vado a leggere nel file {utenti.json}
    """
    cittadino = cittadini.get(codice_fiscale)
    if cittadino:
        return jsonify({"Esito": "000", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
    else:
        return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200




@api.route('/update_cittadino', methods=['PUT'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino aggiornato con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200




@api.route('/elimina_cittadino', methods=['DELETE'])
def elimina_cittadino():
    """
    prima verifico utente, password e privilegi,
    dove l'username e password me l'ha inviato il client
    mentre il privilegio lo vado a leggere nel file {utenti.json}
    """
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        cod = request.json.get('codFiscale')
        if cod in cittadini:
            del cittadini[cod]
            JsonSerialize(cittadini, file_path)  
            return jsonify({"Esito": "000", "Msg": "Cittadino rimosso con successo"}), 200
        else:
            return jsonify({"Esito": "001", "Msg": "Cittadino non trovato"}), 200
    else:
        return jsonify({"Esito": "002", "Msg": "Formato richiesta non valido"}), 200
    


api.run(host="127.0.0.1", port=8080)
