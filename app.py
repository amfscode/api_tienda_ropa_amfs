from flask import Flask, request
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

# ________________________________
@app.route("/")# == http://127.0.0.1:5000/
def home():
    # return "API funcionando"
    return {
        "mensaje": "API funcionando",
        "version": "1.0"
    }
# ________________________________
@app.route("/prendas")
def obteber_prendas():
    return prendas

# ________________________________
@app.route("/prendas/<int:id>")
def obtener_prendas(id):
    for prenda in prendas:
        if prenda["id"] == id:
            return prenda
    return {
        "error": "Prenda no encontrada"
    }
# ________________________________
@app.route("/prendas",methods = ["POST"])

def crear_prenda():
    datos = request.get_json()

    prendas.append(datos)
    
    return datos
# ________________________________

if __name__ == "__main__":
    app.run(debug=True)