from flask import Flask, render_template, request
from apiZomato import getfoodplaces

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/lista', methods=['POST', 'GET'])
def lista():
    if request.method == 'POST':
        valores = request.form
        apiKey = "bbe37c3293f8080f24379ef4a4530ddc"
        lista = getfoodplaces(apiKey, valores['Latitude'], valores['Longitude'])
        return render_template('lista.html', lista=lista['restaurants'])


if __name__ == '__main__':
    app.run(debug=True)
