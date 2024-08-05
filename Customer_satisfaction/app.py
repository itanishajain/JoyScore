from flask import Flask, render_template, url_for, request
import joblib
from werkzeug.utils import redirect

model = joblib.load('logistic_regression.lb')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route("/prediction", methods=['POST'])
def prediction():
    age = int(request.form['age'])
    flight_distance = int(request.form['flight_distance'])    
    infligth_entertainment = int(request.form["inflight-entertainment"])
    baggage_handling = int(request.form["baggage-handling"])   
    cleanliness = int(request.form["cleanliness"])  
    departure_delay = int(request.form["departure_delay"])
    arrival_delay  = int(request.form["arrival_delay"])
    gender = int(request.form["gender"])
    customer_type  = int(request.form["customer-type"])
    travel_type = int(request.form["travel-type"])
    class_Type  = request.form["class-type"]
    Class_Eco = 0
    Class_Eco_Plus = 0
    if class_Type == 'ECO':
        Class_Eco = 1 
        Class_Eco_Plus = 0
    elif class_Type == 'ECO_PLUS':
        Class_Eco = 0 
        Class_Eco_Plus = 1
    else:
        Class_Eco = 0
        Class_Eco_Plus = 0
    UNSEEN_DATA = [[age, flight_distance, infligth_entertainment, baggage_handling,
                   cleanliness, departure_delay, arrival_delay, gender,
                   customer_type, travel_type, Class_Eco, Class_Eco_Plus]]

    prediction = model.predict(UNSEEN_DATA)[0]
    labels = {'1': "SATISFIED", '0': "DISATISFIED"}
    
    # Redirect with a delay
    return render_template('output.html', output=labels[str(prediction)])

if __name__ == "__main__":
    app.run(debug=True)
