from flask import Flask,render_template,request
import os

app = Flask(__name__)

@app.route('/') #git switch -c mainpage
def index():
    return render_template('index.html') #처음에 틀면 여기로 들어감

@app.route('/mnist',methods=['GET','POST']) #두개로 해도 여기로 호출하겠다
def mnist():
    if request.method == 'GET': #위에 설정 잘 되는지 확인
        return render_template('mnistform.html')
    else:
        f = request.files['mnistfile'] #html에서 아까 정해준 이름
        path  = os.path.dirname(__file__)+'/upload/'+f.filename
        f.save(path)
        return "성공!!"


if __name__ == '__main__':
    app.run(debug=True)