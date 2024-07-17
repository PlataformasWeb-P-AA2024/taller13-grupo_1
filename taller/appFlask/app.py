from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/listaredificios")
def listar_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/edificios/",
            auth=('admin', '1'))
    edificios = json.loads(r.content)['results']
    nEdificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    nEdificios=nEdificios)


@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/departamentos/",
            auth=('admin', '1'))
    departamentos = json.loads(r.content)['results']
    nDepartamentos = json.loads(r.content)['count']
    datos2 = []
    for d in departamentos:
        datos2.append(

        {
        'nombre':d['nombre'],
        'costo':d['costo'],
        'nCuartos':d['nCuartos'],
        'edificio': obtener_edificio(d['edificio'])}
       
        )
    return render_template("losdepartamentos.html", departamentos=datos2,
    nDepartamentos=nDepartamentos)

# funciones ayuda

def obtener_edificio(url):
   
    r = requests.get(url, auth=('admin', '1'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio




@app.route("/crearEdificios", methods=['GET', 'POST'])
def crear_edificios():
    if request.method == 'POST':

        nombre = request.form['nombre']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        tipo = request.form['tipo']

        data = {
            'nombre': nombre,
            'direccion': direccion,
            'ciudad': ciudad,
            'tipo': tipo
        }

        r = requests.post('http://127.0.0.1:8000/edificios/', 
        data=data, 
        auth=('admin', '1'))
        print(r)
        
        return redirect(url_for('index'))

    return render_template("crearedificios.html")

app.run()
