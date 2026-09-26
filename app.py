from flask import Flask,request,jsonify, render_template
import pandas as pd
import pickle

app=Flask(__name__)

@app.route("/" , methods=["GET"])
def home():
    return render_template("index.html")

def get_cleaned_data(form_data):
    gestation=int(form_data['gestation'])
    parity=int(form_data['parity'])
    age=int(form_data['age'])
    height=int(form_data['height'])
    weight=int(form_data['weight'])
    smoke=int(form_data['smoke'])

    cleaned_data={'gestation': [gestation],
        'parity': [parity],
        'age': [age],
        'height': [height],
        'weight': [weight],
        'smoke': [smoke]}

    return cleaned_data


@app.route('/predict', methods=["POST"])
def get_prediction():
    baby_data_form=request.form
    baby_data_clean=get_cleaned_data(baby_data_form)
    baby_df=pd.DataFrame(baby_data_clean)

    with open("model.pkl", "rb") as obj:
        model=pickle.load(obj)

    prediction=model.predict(baby_df)
    prediction=prediction.tolist()

    response={"Prediction":prediction}
    return render_template("index.html" , prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)

