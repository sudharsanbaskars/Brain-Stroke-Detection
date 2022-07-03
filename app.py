from flask import Flask, render_template, request, Response
from flask_cors import cross_origin
from util import get_prediction

app = Flask(__name__)

# home page
@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')


# Prediction url
@app.route('/predict', methods=['GET', 'POST'])
#@cross_origin()
def predict():
    hypertension_map = {"Yes": 1,"No": 0}
    heart_map = {"Yes": 1,"No": 0}
    gender_map = {"Male": 1, "Female": 0}
    residence_map = {"Urban": 0, "Rural": 1}
    married_map = {"Yes": 1, "No": 0}
    work_type_dict = {
        "Government Job": 1,
        "Never Worked": 2,
        "Private Job": 3,
        "Self Employed": 4,
        "Children": 5
    }

    smoking_status_dict = {
        "Unknown": 1,
        "Formerly Smoked": 2,
        "Never Smoked": 3,
        "Smokes": 4
    }


    try:
        if request.method == "POST":

            gender = gender_map[request.form['gender']]
            age = request.form['age']
            hypertension = hypertension_map[request.form['having_hypertension']]
            heart_disease = heart_map[request.form['having_heart_disease']]
            married = married_map[request.form['married']]
            residence_type = residence_map[request.form['residence_type']]
            avg_glucose_level = float(request.form['avg_glucose_level'])
            bmi = float(request.form['bmi'])
            work_type = work_type_dict[request.form['work_type']]
            smoking_status = smoking_status_dict[request.form['smoking_status']]


            #pred = Prediction()
            result = get_prediction(gender, age, hypertension, heart_disease, married, residence_type,
                                  avg_glucose_level, bmi, work_type, smoking_status)

            if result == 1:
                result = "Brain Stroke is detected from the given data"
            else:
                result = "No Brain detected"

            return render_template('index.html', result=result)
        else:
            return Response("Please Enter a Valid Input")

    except Exception as e:
        print(e)
        return Response("Error Occured: " + str(e))


if __name__ == "__main__":
    app.run(debug=True)








