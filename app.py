import sqlite3
conexion = sqlite3.connect("database.db")
print("Base de datos creado")
conexion.close()

from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Prenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Float)
with app.app_context():
    db.create_all()
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
@app.route("/prendas")  #[GET]
def obteber_prendas():
    prendas = Prenda.query.all()
    resultado = []

    for p in prendas:
        resultado.append({
            "id": p.id,
            "nombre": p.nombre,
            "precio": p.precio,
        })
    return resultado

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
    # nuevo_id = len(prendas) + 1
    nueva_prenda = Prenda(
        nombre = datos["nombre"],
        precio = datos["precio"]
    )
    db.session.add(nueva_prenda)
    db.session.commit()
    return {
        "id": nueva_prenda.id,
        "nombre": nueva_prenda.nombre,
        "precio": nueva_prenda.precio,
    }

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