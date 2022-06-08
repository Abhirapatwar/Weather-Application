import requests
from flask import Flask,request, render_template
import flask
from flask_bootstrap import Bootstrap


app = Flask(__name__,
            template_folder='templates')
app.config['SECRET_KEY'] = 'secret123'
Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def get_data():
    z = None
    if flask.request.method == 'POST':
        form = flask.request.form
        z = form['zipcode']

    if z == None:
        response = {"name": "Enter a zip code"}
        

    else:
        api_url = "https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}".format(
            z, 'in', "28081895045b1e9e7dbd34cc30ee52a7")

        response = requests.get(api_url)
        response = response.json()
    return render_template("home.html", response=response)


if __name__ == '__main__':
    app.run(debug=True)
