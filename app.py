from flask import Flask, jsonify, request
import json
from functions import todosProductos
from functions import limite_producto

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

# Correr la aplicación
# host = "0.0.0.0.0" Para correr la aplicación desde cualquier lado

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)