from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Edificios API</p>"


@app.route("/edificios")
def listado_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/edificios/",
            auth=('ian', 'ian'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("listado_edificios.html", edificios=edificios,
    numero_edificios=numero_edificios)

@app.route("/departamentos")
def listado_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/departamentos/",
            auth=('ian', 'ian'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'propietario':d['nombre_propietario'], 'cuartos':d['num_cuartos'], 'costo':d['costo'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("listado_departamentos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('ian', 'ian'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
