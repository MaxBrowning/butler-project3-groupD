from flask import Flask, render_template, jsonify, request
import data
import pickle
import requests
import numpy as numpy
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

#load the ml model which we have saved earlier in .pkl format            
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

#creating object for StandardScaler
standard_to = StandardScaler()


#define the route for post request method 
@app.route("/predict", methods=['POST'])

#define the predict function which is going to predict the results from ml model based on the given values through html form
def predict():
    if request.method == 'POST':
        Total_Assessed_Value= float(request.form['Assessed_Value'])
        Parcel_Acreage = float(request.form['Acreage'])
         #propertyclass(feature) is categorized into  
        Property_Class=request.form['Property_Class']
        if(Property_Class=='Agricultural'):
            Class_Code_Translated_Agricultural=1
            Class_Code_Translated_Commercial=0
            Class_Code_Translated_Exempt=0 
            Class_Code_Translated_Industrial=0 
            Class_Code_Translated_Locally_Assessed=0 
            Class_Code_Translated_Mineral=0 
            Class_Code_Translated_Residential=0 
        elif(Property_Class=='Commercial'):
            Class_Code_Translated_Agricultural=0
            Class_Code_Translated_Commercial=1
            Class_Code_Translated_Exempt=0 
            Class_Code_Translated_Industrial=0 
            Class_Code_Translated_Locally_Assessed=0 
            Class_Code_Translated_Mineral=0 
            Class_Code_Translated_Residential=0 
        elif(Property_Class=='Exempt'):
            Class_Code_Translated_Agricultural=0
            Class_Code_Translated_Commercial=0
            Class_Code_Translated_Exempt=1 
            Class_Code_Translated_Industrial=0 
            Class_Code_Translated_Locally_Assessed=0 
            Class_Code_Translated_Mineral=0 
            Class_Code_Translated_Residential=0 
        elif(Property_Class=='Industrial'):
            Class_Code_Translated_Agricultural=0
            Class_Code_Translated_Commercial=0
            Class_Code_Translated_Exempt=0 
            Class_Code_Translated_Industrial=1 
            Class_Code_Translated_Locally_Assessed=0 
            Class_Code_Translated_Mineral=0 
            Class_Code_Translated_Residential=0 
        if(Property_Class=='Residential'):
            Class_Code_Translated_Agricultural=0
            Class_Code_Translated_Commercial=0
            Class_Code_Translated_Exempt=0 
            Class_Code_Translated_Industrial=0 
            Class_Code_Translated_Locally_Assessed=0 
            Class_Code_Translated_Mineral=0 
            Class_Code_Translated_Residential=1
        else:
            Class_Code_Translated_Agricultural=0
            Class_Code_Translated_Commercial=0
            Class_Code_Translated_Exempt=0 
            Class_Code_Translated_Industrial=0 
            Class_Code_Translated_Locally_Assessed=0 
            Class_Code_Translated_Mineral=0 
            Class_Code_Translated_Residential=0  

        Vacant=request.form['Vacant']
        if(Vacant=='Yes'):
            Vacant=1
        else:
            Vacant=0

        prediction=model.predict([[Total_Assessed_Value,Parcel_Acreage,Class_Code_Translated_Agricultural,Class_Code_Translated_Commercial,Class_Code_Translated_Exempt, Class_Code_Translated_Industrial,Class_Code_Translated_Locally_Assessed,Class_Code_Translated_Mineral, Class_Code_Translated_Residential,Vacant]])
        output=round(prediction[0],2)
        
        #condition for invalid values
        return render_template('index.html',prediction_text= "This property is worth {}".format(output))
        
    #html form to be displayed on screen when no values are inserted; without any output or prediction
    else:
        return render_template('index.html')

@app.route('/property', methods=['GET'])
def database_data():
    propertydata = data.get_db_data()
    response = jsonify(propertydata)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == '__main__':
    app.run(debug=True)