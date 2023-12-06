
from flask import Flask, render_template, request
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
crop_labels = {0:["Apple","Heavy Clay or Compact Subsoil","Compost","29,450 per Acer"],
               1:["Banana","Rich loamy soil","Manure,Compost","83,450 per Acer"],
               2:["Blackgram","Sandy soils to Heavy cotton soils","Fish Emuslion","53,450 per Acer"],
               3:["Chickpea","Deep black soils","Poultry Litter","33,450 per Acer"],
               4:["Coconut","Red sandy loam","Compost","43,450 per Acer"],
               5:["Coffee","Fertile volcanic red soil","Coffee Grounds","23,450 per Acer"],
               6:["Cotton","Black cotton soils","Cottonseed Meal","19,250 per Acer"],
               7:["Grapes","Black soils and red loams","Compost,Bone Meal","73,450 per Acer"],
               8:["Jute","Alluvial","Compost","33,450 per Acer"],
               9:["Kidneybeans","Loamy soil","Legume Inoculants","33,450 per Acer"],
               10:["Lentil","Acidic soils","Legume Inoculants","93,450 per Acer"],
               11:["Maize","Oamy sand to clay loam","Manure,Fish Emulsion","19,450 per Acer","73,450 per Acer"],
               12:["Mango","Alluvial","Compost,Fish Emulsion","43,450 per Acer"],
               13:["Mothbeans","Dry sandy soil","Legume Inoculants","13,450 per Acer"],
               14:["Mungbean","Red laterite soils","Legume Inoculants","63,450 per Acer"],
               15:["Muskmelon","Acidity soil","Compost,Fruit and Vegetable Scraps","53,450 per Acer"],
               16:["Orange","Deep well drained loamy soils","Compost,Wood Ash","12,47 per Acer"],
               17:["Papaya","Sandy loam soil","Compost","12,47 per Acer","23,450 per Acer"],
               18:["Pigeonpeas","Black cotton soils","Legume Inoculants","63,450 per Acer"],
               19:["Pomegranate","Deep loamy soils","Compost,Bone Meal","23,450 per Acer"],
               20:["Rice","Clay loams","Rice Bran","23,450 per Acer"],
               21:["Watermelon","Sandy loam","Compost,Fruit and Vegetable Scraps","83,450 per Acer"]}
# Load the Decision Tree Regressor model
model = joblib.load('C:/Users/Dell/Desktop/Croprediction Capstone/Croprediction Capstone/model.joblib')
# Define a Flask app
app = Flask(__name__)
# Define a route to render the crop prediction form
@app.route('/', methods=['GET','POST'])    
def show_form():
    return render_template('predict.html')
# Define a route to handle the form submission and display the result
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        pH = float(request.form['pH'])
        rainfall = float(request.form['rainfall'])
        features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, pH, rainfall]])
        prediction = model.predict(features)
        predicted_labels = crop_labels[int(prediction)]
        return render_template('predict.html', fruit=predicted_labels[0],soil=predicted_labels[1],natfer=predicted_labels[2],price=predicted_labels[3])  # Get the single prediction
    return render_template('predict.html')
if __name__ == '__main__':
    app.run(debug=True)
