from flask import Flask
app = Flask(__name__)
@app.route("/")# == http://127.0.0.1:5000/
def home():
    # return "API funcionando"
    return {
        "mensaje": "API funcionando",
        "version": "1.0"
    }
@app.route("/prendas")
def prendas():
    return [
        {
            "id": 1,
            "nombre": "Polo Negro",
            "precio": 35
        },
        {
            "id": 2,
            "nombre": "Casaca Azul",
            "precio": 80
        }
    ]


if __name__ == "__main__":
    app.run(debug=True)
