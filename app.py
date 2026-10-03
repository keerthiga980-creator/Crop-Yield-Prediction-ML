from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model and preprocessor
model = joblib.load("crop_yield_real_random_forest.pkl")
preprocessor = joblib.load("crop_yield_preprocessor.pkl")


@app.route("/")
def home():
    return "Crop Yield Prediction API is running!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    input_data = pd.DataFrame({
        "area": [data["area"]],
        "year": [data["year"]],
        "average_rain_fall_mm_per_year": [
            data["rainfall"]
        ],
        "pesticides_tonnes": [
            data["pesticides"]
        ],
        "avg_temp": [
            data["temperature"]
        ],
        "item": [data["crop"]]
    })

    input_encoded = preprocessor.transform(input_data)

    prediction = model.predict(input_encoded)

    return jsonify({
        "predicted_yield_hg_ha": round(float(prediction[0]), 2)
    })


if __name__ == "__main__":
    app.run(debug=True)
