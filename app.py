from flask import Flask, request, render_template
import pickle as pkl

app= Flask(__name__)

model=pkl.load(open('model.pkl','rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    Nitrogen=int(request.form['Nitrogen'])
    Phosphorous=int(request.form['Phosphorous'])
    Potassium=int(request.form['Potassium'])
    Temperature=int(request.form['Temperature'])
    Humidity=int(request.form['Humidity'])
    pH=int(request.form['pH'])
    Rainfall=int(request.form['rainfall'])
    predicted=model.predict([[Nitrogen, Phosphorous, Potassium, Temperature, Humidity, pH, Rainfall]])
    predicted=predicted[0]

    print(predicted)
    return render_template("index.html",predicted=f'{predicted}')


if __name__=='__main__':
    app.run()