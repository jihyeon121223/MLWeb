from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/') #git switch -c mainpage
def index():
    return render_template('index.html') #처음에 틀면 여기로 들어감

@app.route('/mnist',methods=['GET','POST']) #두개로 해도 여기로 호출하겠다
def mnist():
    if request.method == 'GET': #위에 설정 잘 되는지 확인
        return render_template('mnistform.html')
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)