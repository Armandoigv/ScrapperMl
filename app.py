import re
from flask import Flask, jsonify, request, render_template, Response
import json
from functions import todosProductos
from functions import limite_producto
import requests

app = Flask(__name__)

@app.route('/mercadolibre', methods = ['GET'])
def mercadolibre():
    # Variable con el request solicitado, inicialmente llega como tipo texto y por lo tanto se debe convertir a json
    # print(request.data,type(request.data))
    data = json.loads(request.data)
    # print(data,type(data))
    # print(data['producto'])
    if 'limite' not in data:
        titulos, urls, precios = todosProductos(data['producto'])
    else:
        titulos, urls, precios = limite_producto(data['producto'], data['limite'])    
    return jsonify({"datos" : {"Titulos": titulos, "Urls": urls, "Precios": precios} })

@app.route("/descargarInfo", methods=["GET", "POST"])

def descargarInfo():
    if request.method == "POST":
        print('hola')
        producto = request.form["producto"]
        limite = request.form["limite"]
        #r = requests.get('http://192.168.100.180:5000/mercadolibre', json = {"producto":producto,"limite":int(limite)})
        r = requests.get('http://scrapmerca.herokuapp.com/mercadolibre', json = {"producto":producto,"limite":int(limite)})
        print(r.status_code)
        if r.status_code == 200:
            print(r.text, type(r.text))
            data = json.loads(r.text)
            print("\n\n\n")
            t = ""
            for i,j,z in zip(data["datos"]["Titulos"], data["datos"]["Precios"], data["datos"]["Urls"]):
                #print(i, j, z)
                t+=f"{i}|{j}|{z}\n" 
            return Response(
                t,
                mimetype="text",
                headers= {
                    "Content-disposition":"attachment; filename=datos.txt"
                }
            )
            #print("\n\n\n")
            #print(data,type(data))
        return "Error"
        #print(producto, limite)
        #return {"asd":"Gracias"}
        pass
    return render_template('index.html')

# Correr la aplicación
# host = "0.0.0.0.0" Para correr la aplicación desde cualquier lado

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)