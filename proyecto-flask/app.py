from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/personas")
def listado_personas():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/personas/",
            auth=('ian', 'ian'))
    personas = json.loads(r.content)['results']
    numero_personas = json.loads(r.content)['count']
    return render_template("listado_personas.html", personas=personas,
    numero_personas=numero_personas)

@app.route("/barrios")
def listado_barrios():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/barrios/",
            auth=('ian', 'ian'))
    barrios = json.loads(r.content)['results']
    numero_barrios = json.loads(r.content)['count']
    return render_template("listado_barrios.html", barrios=barrios,
    numero_barrios=numero_barrios)

@app.route("/casas")
def listado_casas():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/casas/",
            auth=('ian', 'ian'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({
            'propietario':obtener_propietario(d['propietario']),
            'barrio':obtener_barrio(d['barrio']),
            'cuartos':d['num_cuartos'], 
            'pisos':d['num_pisos'], 
            'direccion':d['direccion'], 
            'color':d['color'], 
            'valor':d['valor']
        })
    return render_template("listado_casas.html", datos=datos2,
    numero=numero)

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
        datos2.append({
            'propietario':obtener_propietario(d['propietario']),
            'barrio':obtener_barrio(d['barrio']),
            'cuartos':d['num_cuartos'], 
            'costo':d['costo_mensual'],
            'direccion':d['direccion'], 
            'valor':d['valor']
        })
    return render_template("listado_departamentos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_propietario(url):
    """
    Funcion para poder obtener los valores de un propietario en especifico
    """
    r = requests.get(url, auth=('ian', 'ian'))
    nombre_propietario = json.loads(r.content)['nombres']
    return nombre_propietario

def obtener_barrio(url):
    """
    Funcion para poder obtener los valores de un barrio en especifico
    """
    r = requests.get(url, auth=('ian', 'ian'))
    nombre_barrio = json.loads(r.content)['nombres']
    return nombre_barrio
