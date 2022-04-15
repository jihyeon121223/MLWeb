from flask import Flask,render_template

app = Flask(__name__)

@app.route('/') #git switch -c mainpage
def index():
    return render_template('index.html') #처음에 틀면 여기로 들어감


if __name__ == '__main__':
    app.run(debug=True)