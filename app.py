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
    nuevo_id = len(prendas) + 1
    nueva_prenda = {
        "id" : nuevo_id,
        "nombre": datos["nombre"],
        "precio": datos["precio"]
    }
    prendas.append(nueva_prenda)
    return nueva_prenda

# ________________________________

@app.route("/prendas/<int:id>", methods = ["DELETE"])
def eliminar_prendas(id):
    for prenda in prendas:
        if prenda["id"] == id:
            prendas.remove(prenda)

            return {
                "mensaje" : "prenda eliminada"
            }
        return {
            "error": "prenda no encontrada"
        }

# ________________________________

if __name__ == "__main__":
    app.run(debug=True)