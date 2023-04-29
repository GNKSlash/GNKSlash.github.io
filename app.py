from flask import Flask, render_template, request

app = Flask(__name__)

logs = []

@app.route('/', methods=['POST'])
def index():
    log = request.form['log']
    logs.append(log)
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
