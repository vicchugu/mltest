from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    val1  = request.form['crim']
    val2  = request.form['zm']
    val3  = request.form['indus']
    val4  = request.form['chas']
    val5  = request.form['nox']
    val6  = request.form['rm']
    val7  = request.form['age']
    val8  = request.form['dis']
    val9  = request.form['rad']
    val10 = request.form['tax']
    val11 = request.form['ptratio']
    val12 = request.form['b']
    val13 = request.form['lstat']
    arr = np.array([val1, val2, val3, val4, val5,val6, val7, val8, val9, val10, val11, val12, val13])
    arr = arr.astype(np.float64)
    pred = model.predict([arr])

    return render_template('index.html', data=int(pred))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
