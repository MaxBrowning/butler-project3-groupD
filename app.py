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
scaler = StandardScaler()


#define the route for post request method 
@app.route("/predict", methods=['POST'])

#define the predict function which is going to predict the results from ml model based on the given values through html form
def predict():
    if request.method == 'POST':
        Total_Assessed_Value = float(request.form['Assessed_Value'].replace(',','').replace('$',''))
        Parcel_Acreage = float(request.form['Acreage'])
        Vacant = request.form['Vacant']
        if (Vacant == 'Yes'):
            Parcel_Vacancy_Y = 1
            Parcel_Vacancy_N = 0
        else:
            Parcel_Vacancy_Y = 0
            Parcel_Vacancy_N = 1

        Property_Class = request.form['Property_Class']

        if (Property_Class == 'Agricultural'):
            Class_Code_Translated_Agricultural = 1
            Class_Code_Translated_Commercial = 0
            Class_Code_Translated_Exempt = 0 
            Class_Code_Translated_Industrial = 0 
            Class_Code_Translated_Locally_Assessed = 0 
            Class_Code_Translated_Residential = 0 
        elif (Property_Class =='Commercial'):
            Class_Code_Translated_Agricultural = 0
            Class_Code_Translated_Commercial = 1
            Class_Code_Translated_Exempt = 0 
            Class_Code_Translated_Industrial = 0 
            Class_Code_Translated_Locally_Assessed = 0 
            Class_Code_Translated_Residential = 0 
        elif (Property_Class == 'Exempt'):
            Class_Code_Translated_Agricultural = 0
            Class_Code_Translated_Commercial = 0
            Class_Code_Translated_Exempt = 1 
            Class_Code_Translated_Industrial = 0 
            Class_Code_Translated_Locally_Assessed = 0   
            Class_Code_Translated_Residential = 0 
        elif (Property_Class == 'Industrial'):
            Class_Code_Translated_Agricultural = 0
            Class_Code_Translated_Commercial = 0
            Class_Code_Translated_Exempt = 0 
            Class_Code_Translated_Industrial = 1 
            Class_Code_Translated_Locally_Assessed = 0 
            Class_Code_Translated_Residential = 0 
        elif (Property_Class == 'Locally Assessed'):
            Class_Code_Translated_Agricultural = 0
            Class_Code_Translated_Commercial = 0
            Class_Code_Translated_Exempt = 0 
            Class_Code_Translated_Industrial = 0 
            Class_Code_Translated_Locally_Assessed = 1  
            Class_Code_Translated_Residential = 0
        elif (Property_Class == 'Residential'):
            Class_Code_Translated_Agricultural = 0
            Class_Code_Translated_Commercial = 0
            Class_Code_Translated_Exempt = 0 
            Class_Code_Translated_Industrial = 0 
            Class_Code_Translated_Locally_Assessed = 0  
            Class_Code_Translated_Residential = 1
    # open file pickle.load x and y
    new_data= [[Total_Assessed_Value, Parcel_Acreage, Parcel_Vacancy_Y, Parcel_Vacancy_N, Class_Code_Translated_Agricultural, Class_Code_Translated_Commercial, Class_Code_Translated_Exempt, Class_Code_Translated_Industrial, Class_Code_Translated_Locally_Assessed, Class_Code_Translated_Residential]]
    # apply x scaler to xdata
    Xscaler = pickle.load(open("Xscaler.pkl", "rb"))
    Yscaler = pickle.load(open("Yscaler.pkl", "rb"))

    scaled = Xscaler.transform(new_data)

    # for inverse transformation
    #inversed = scaler.inverse_transform(scaled)
    #print(inversed)
    prediction = Yscaler.inverse_transform(model.predict(scaled))
    # apply y scaler.inverse transform
    output = round(prediction[0],2)

   
    print (output)


    if output:           #condition for invalid values
        return render_template('index.html', prediction_text = "This property is worth ${:,.2f}".format(output))
        
    #html form to be displayed on screen when no values are inserted; without any output or prediction
    else:
        return render_template('index.html')

@app.route('/property', methods=['GET'])
def database_data():
    propertydata = data.get_db_data()
    response = jsonify(propertydata)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/explore')
def explore():
    return render_template('explore.html')


if __name__ == '__main__':
    app.run(debug=True)