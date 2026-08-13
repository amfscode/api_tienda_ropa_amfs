from flask import Flask
app = Flask(__name__)
prendas = [
{
    "id": 1,
    "nombre": "Polo negro",
    "precio": 35
},
{
    "id": 2,
    "nombre": "Casaca",
    "precio": 80
},
{
    "id": 3,
    "nombre": "Jean",
    "precio": 120
}
]
@app.route("/")# == http://127.0.0.1:5000/
def home():
    # return "API funcionando"
    return {
        "mensaje": "API funcionando",
        "version": "1.0"
    }
@app.route("/prendas")
def prendas():
    return prendas

@app.route("/prendas/<int:id>")
def obtener_prendas(id):
    for prenda in prendas:
        if prenda["id"] == id:
            return prenda
    return {
        "error": "Prenda no encontrada"
    }

if __name__ == "__main__":
    app.run(debug=True)