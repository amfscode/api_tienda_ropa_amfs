import sqlite3
conexion = sqlite3.connect("database.db")
print("Base de datos creado")
conexion.close()

from flask import Flask, request
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config[SQLALCHEMY_DATABASE_URI] = "Sqlite:///database.db"
db =SQLAlchemy(app)

class Prenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Float)

#___________________________________
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
    if "nombre" not in datos:
        return {
            "error" : "falta el nombre"
        }
    if "precio" not in datos:
        return {
            "error" : "falta el precio"
        }
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

@app.route("/prendas/<int:id>",  methods= ["PUT"])
def actualizar_prenda(id):
    datos = request.get_json()
    for prenda in prendas:
        if prenda["id"] == id:
            prenda["nombre"] = datos["nombre"]
            prenda["precio"] = datos["precio"]

            return prenda
    return {
        "error" : "Prenda no encontrada"
    }
# ________________________________

if __name__ == "__main__":
    app.run(debug=True)