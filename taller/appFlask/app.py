from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/losestudiantes")
def los_estudiantes():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/estudiantes/",
            auth=('jose', '12345'))
    estudiantes = json.loads(r.content)['results']
    numero_estudiantes = json.loads(r.content)['count']
    return render_template("losestudiantes.html", estudiantes=estudiantes,
    numero_estudiantes=numero_estudiantes)


@app.route("/lostelefonos")
def los_telefonos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/numerosts/",
            auth=('admin', '1'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("lostelefonos.html", datos=datos,
    numero=numero)


@app.route("/lostelefonosdos")
def los_telefonos_dos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/numerosts/",
            auth=('jose', '12345'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append(

        {
        'telefono':d['telefono'],
        'tipo':d['tipo'],
        'estudiante': obtener_estudiante(d['estudiante'])}
        # http://127.0.0.1:8000/api/estudiantes/4/
        # René
        )
    return render_template("lostelefonosdos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_estudiante(url):
    """
    http://127.0.0.1:8000/api/estudiantes/4/
    """
    r = requests.get(url, auth=('jose', '123455'))
    nombre_estudiante = json.loads(r.content)['nombre']
    return nombre_estudiante


app.run()
