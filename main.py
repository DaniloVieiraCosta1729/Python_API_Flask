from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/endereco-do-app/<id_do_usuario>")

def get_user(id_do_usuario):
    json_com_dados = {
        "id": id_do_usuario,
        "nome":"Danilo",
        "email": "danilo.11235@outlook.com"
    }

    phi = (1+5**0.5)/2

    json_com_dados["phi"] = phi

    informacao = request.args.get("informacao")

    if informacao:
        a = int(informacao)
        a = a*2
        json_com_dados["informacao x 2"] = a
        return jsonify(json_com_dados), 200

@app.route("/criar-usuario", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if __name__=="__main__":
    app.run(debug=True)