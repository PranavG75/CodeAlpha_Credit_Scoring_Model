from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained pipeline
model = joblib.load(r'C:\Users\Pranav Parab\Desktop\Pranav\credit_score\saved_model\credit_pipeline.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    # Collect user input
    input_data = pd.DataFrame([{
        'Age': int(request.form['age']),
        'Job': int(request.form['job']),
        'Credit amount': float(request.form['credit_amount']),
        'Duration': int(request.form['duration']),
        'Sex': request.form['sex'],
        'Housing': request.form['housing'],
        'Saving accounts': request.form['saving_accounts'],
        'Checking account': request.form['checking_account'],
        'Purpose': request.form['purpose']
    }])

    # Predict
    prediction = model.predict(input_data)[0]

    # Probability
    probability = model.predict_proba(input_data)[0][1]
    

    # Result text
    if prediction == 1:
        result = "HIGH RISK CUSTOMER"
    else:
        result = "LOW RISK CUSTOMER"

    return render_template(
        'index.html',
        prediction=result,
        probability=round(probability * 100, 2)
    )


if __name__ == '__main__':
    app.run(debug=True)