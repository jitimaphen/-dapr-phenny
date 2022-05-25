from flask_cors import CORS
from flask import Flask, redirect, url_for, request, render_template
import requests
import json
import os


app = Flask(__name__)
CORS(app)

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
dapr_url = "http://localhost:{}/v1.0/invoke/phenny/method/tenant/".format(dapr_port)
# dapr_python_app_url = "http://localhost:{}/v1.0/invoke/pythonapp/method/bird".format(dapr_port)
stateUrl = "http://localhost:{}/v1.0/state/statestore/user/".format(dapr_port)

@app.route('/users')
def User():
    result = requests.get(stateUrl, headers={"Content-Type": "application/json"}, data=b'')
    print("get state result---------------", result.text)
    return "<h1>Hello World"+result.text+"</h1>"


@app.route('/dsstatus', methods=['POST'])
def ds_subscriber():
    # data = request.get_json()
    print("App: PubSub received a message!", flush=True)
    print("request-------------", request.data)
    print("request-------------", request.get_json())
    redirect(url_for('success', name="test"))
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/loading/<name>')
def loading(name):
    return 'Loading ..... %s' % name


@app.route('/success/<name>')
def success(name):
    return 'Success %s' % name


@app.route('/register', methods=['POST', 'GET'])
def register():
    print("request.method", request.method)
    if request.method == 'POST':
        name = request.form['nm']
        age = request.form['age']

        message = {"name": name, "age": age}
        requests.post(dapr_url, json=message)

        return redirect(url_for('loading', name=name))
    else:
        return render_template('register.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
