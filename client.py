from flask import Flask, render_template, request
from apiZomato import getfoodplaces, locateByIP

apiKey = "bbe37c3293f8080f24379ef4a4530ddc"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/lista', methods=['POST', 'GET'])
def lista():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Procurar':
                valores = request.form
                lista = getfoodplaces(apiKey, valores['Latitude'], valores['Longitude'])
        if request.form['submit_button'] == "Usar endereço de IP":
                coor = locateByIP()['loc']
                latlon = coor.split(',')
                lista = getfoodplaces(apiKey, latlon[0], latlon[1])
        return render_template('lista.html', lista=lista['restaurants'])


if __name__ == '__main__':
    app.run(debug=True)
