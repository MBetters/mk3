from flask import Flask, render_template, request, json, send_from_directory, send_file

app = Flask(__name__)

# Serve up the app's home page
@app.route("/")
def home():
    return render_template('app.html')

# Serve up javascript files.
@app.route('/static/js/<js_file_name>')
def send_js(js_file_name):
    return send_file("static/js/" + js_file_name)

# TODO: Change this to be something like /servoValues
#       with a payload of 4 servo degree values that are numbers between 0 and 180.
@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'OK','user':user,'pass':password})

if __name__ == "__main__":
    app.run()
