import pickle
import json
import numpy as np


total_cols = 17
model_path = "models/model.pkl"

def get_prediction(gender, age, hypertension, heart_disease, ever_married, residence_type, avg_glucose_level, bmi,work_type, smoking_status):

    model = None

    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
    except Exception as e:
        print(e)

    work_type_dict = {
        "Government Job" :1,
        "Never Worked" : 2,
        "Private Job" : 3,
        "Self Employed" : 4,
        "Children" : 5
    }

    smoking_status_dict = {
        "Unknown" : 1,
        "Formerly Smoked": 2,
        "Never Smoked" : 3,
        "Smokes": 4
    }



    gender_map = {"Male": 1, "Female": 0}
    residence_map = {"Urban": 0, "Rural": 1}
    married_map = {"Yes": 1, "No": 0}

    try:
        x = np.zeros(total_cols)
        x[0] = gender
        x[1] = age
        x[2] = hypertension
        x[3] = heart_disease
        x[4] = ever_married
        x[5] = residence_type
        x[6] = avg_glucose_level
        x[7] = bmi

        x[7+work_type] = 1

        x[12+smoking_status] = 1
        return round(model.predict([x])[0],2)
    except Exception as e:
        print(e)


# def get_location_names(self):
#     with open(self.columns_path, "r") as f:
#         data_columns = json.load(f)['data_columns']
#         locations = data_columns[3:]  # first 3 columns are sqft, bath, bhk
#     return locations
#
#
# def get_data_columns(self):
#     with open("artifacts/columns.json", "r") as f:
#         data_columns = json.load(f)['data_columns']
#     return data_columns

# if __name__ == '__main__':
# 	util = UtilOperations()
# 	print(util.get_location_names())
# 	print(util.get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
