from flask import Flask,render_template,request
import os, pickle
import numpy as np
from PIL import Image

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
        img = Image.open(path).convert("L")
        img = np.resize(img,(1,784))
        # img = 255 - (img)
        img = np.resize(img,(1,784))
        mpath = os.path.dirname(__file__)+'/model1.pickle'
        with open(mpath,'rb') as f:
            model = pickle.load(f)
        pred = model.predict(img)
        return render_template('mnistresult.html',data=pred) #데이타 라는 이름으로 예측값을 넘기겠다


if __name__ == '__main__':
    app.run(debug=True)