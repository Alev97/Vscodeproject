from flask import Flask, render_template, request

api = Flask(__name__)

utenti=[['mario','password1','M','0'],['pippo','password2','M','0'],['Zoelee','pass3','F','0']]
utenti_2 = []

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/regok', methods=['GET'])
def regko():
    return render_template('reg_ok.html')


@api.route('/regko', methods=['GET'])
def regok():
    return render_template('reg_ko.html')


@api.route('/registrati', methods=['GET'])
def registra():
    nome=request.args.get("nome")
    print("Nome inserito" + nome)

    password=request.args.get("cognome")
    utente = []
    utente [0] = nome
    utente [1] = password

        if utente in utenti:
            return render_template('reg_ok.html')
        else:
            return render_template('reg_ko.html')
    

    return render_template('reg_ko.html')

    


api.run(host="0.0.0.0", port=8085)
