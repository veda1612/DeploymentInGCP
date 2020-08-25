# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('SVC_rbf_model_v1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():    
    if request.method == 'POST':
        Price=request.form['Price']
        if(Price=='low'):
            Price=0                
        elif(Price=='med'):
            Price=1
        elif(Price=='high'):
            Price=2
        else:
            Price=3
        MaintenanceCost=request.form['Maintenance Cost']
        if(MaintenanceCost=='low'):
            MaintenanceCost=0                
        elif(MaintenanceCost=='med'):
            MaintenanceCost=1
        elif(MaintenanceCost=='high'):
            MaintenanceCost=2
        else:
            MaintenanceCost=3
        NumberOfDoors=request.form['Number of Doors']
        if(NumberOfDoors=='5more'):
            NumberOfDoors=5  
        Capacity=request.form['Capacity']
        if(Capacity=='more'):
            Capacity=5            
        SizeOfLuggageBoot=request.form['Size of Luggage Boot']
        if(SizeOfLuggageBoot=='small'):
            SizeOfLuggageBoot=0      
        elif(SizeOfLuggageBoot=='med'):
            SizeOfLuggageBoot=1
        else:
            SizeOfLuggageBoot=2 
        safety=request.form['safety']
        if(safety=='low'):
            safety=0                
        elif(safety=='med'):
            safety=1
        else:
            safety=2
            
        prediction=model.predict([[Price,MaintenanceCost,NumberOfDoors,Capacity,SizeOfLuggageBoot,safety]])
        output=prediction
        if output<0:
            return render_template('results.html',prediction_texts="Sorry,entered input is wrong, prediction has some problem")
        elif output==0:
            return render_template('results.html',prediction_text="unacc")
        elif output==1:
            return render_template('results.html',prediction_text="acc")
        elif output==2:
            return render_template('results.html',prediction_text="good")
        elif output==3:
            return render_template('results.html',prediction_text="vgood")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
