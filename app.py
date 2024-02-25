import json
from flask import Flask, jsonify, request
import os
import joblib
import pandas as pd
import mlflow
import numpy as np
import requests


app = Flask(__name__)
@app.route("/predict", methods=["POST"])
def predict():
    input = request.get_json()
    
    df = pd.DataFrame(input['dataframe_records'][0])
    df= df.T
    df.columns=["Age","Sex","BP","Cholesterol","Na_to_K"]
    
    ord_bp = joblib.load("artifacts/Ordinal_encode_bp.pkl")
    ord_cho = joblib.load("artifacts/Ordinal_encode_cho.pkl")

    ord_sex=joblib.load("artifacts/Onehot_encode_sex.pkl")
    label_en=joblib.load("artifacts/Label_encode.pkl")
    
    df['BP'] = ord_bp.transform(df[['BP']])
    df['Cholesterol'] = ord_cho.transform(df[['Cholesterol']])
    df['Sex'] = ord_sex.transform(df[['Sex']])
    std = joblib.load("artifacts/Std.pkl")
    df=std.transform(df[:])
    out=np.argmax(loaded_model.predict(df[:,:]), axis=1)
    data={"output": f"{label_en.inverse_transform(out)}"}
    return jsonify(data)




if __name__=="__main__":
    from argparse import ArgumentParser
    
    par = ArgumentParser()
    par.add_argument("--model_uri", type=str)
    par.add_argument("--model_version", type=int)
    par.add_argument("--MLFLOW_TRACKING_URI", type=str)
    args = par.parse_args()
    
    mlflow.set_tracking_uri(args.MLFLOW_TRACKING_URI)
    model_uri=f"models:/{str(args.model_uri)}/{str(args.model_version)}"
    loaded_model = mlflow.pyfunc.load_model(model_uri=model_uri)
    app.run(host="0.0.0.0", port=5000, debug=True)
