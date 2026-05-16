# CodeAlpha_Credit_Scoring_Model
A machine learning-based credit scoring web application that predicts customer credit risk using a Random Forest model and Flask deployment.
A machine learning-powered web application that predicts the credit risk of a customer based on their financial and demographic information. The project uses a Random Forest Classification model along with a Scikit-learn preprocessing pipeline and is deployed using Flask for real-time predictions through a user-friendly web interface.

Project Overview

Financial institutions and banks use credit scoring systems to evaluate whether a customer is likely to repay a loan. This project simulates a simplified real-world credit risk assessment system using machine learning.

The application takes user inputs such as:

Age
Job level
Credit amount
Loan duration
Housing type
Savings account status
Checking account status
Loan purpose

and predicts whether the customer is:

Low Risk Customer
High Risk Customer

along with the probability of default risk.

Features
Real-time credit risk prediction
Machine Learning-based classification system
Random Forest Classifier implementation
Scikit-learn preprocessing pipeline
Automatic categorical encoding and feature scaling
Flask web application deployment
User-friendly frontend interface
Probability-based prediction output
Clean and modular project structure
Technologies Used
Programming Language
Python
Machine Learning
Scikit-learn
Random Forest Classifier
Pipeline
ColumnTransformer
Data Processing
Pandas
NumPy
Web Framework
Flask
Frontend
HTML
CSS
Model Serialization
Joblib
Machine Learning Workflow

The machine learning pipeline includes:

Data Collection
Data Cleaning
Missing Value Handling
Feature Engineering
Categorical Encoding
Feature Scaling
Model Training
Model Evaluation
Model Deployment

Models Used

The following models were trained and evaluated:

Model	Purpose
Logistic Regression	Baseline comparison
Decision Tree Classifier	Tree-based model
Random Forest Classifier	Final selected model

The Random Forest model was selected as the final model due to its superior performance in:

Accuracy
F1-score
ROC-AUC
Generalization capability
Evaluation Metrics

The project evaluates model performance using:

Accuracy
Precision
Recall
F1-score
ROC-AUC Score
Confusion Matrix

These metrics are important in credit scoring because incorrect loan approvals can lead to financial losses.

Dataset

Dataset used:

German Credit Dataset

The dataset contains customer financial information. Comparison:

Credit amount
Loan dura: tion
Employment details
Savings/checking account information
Housing status
Loan purpose

Target Variable:

Good Credit Risk
Bad Credit Risk

Future Improvements

Possible future enhancements include:

SHAP explainability integration
Better UI/UX design
Cloud deployment
User authentication
Database integration
Advanced ML models like XGBoost
Loan approval recommendation system
API development
Learning Outcomes

This project helped in understanding:
Machine Learning model development
Data preprocessing pipelines
Feature engineering
Model evaluation techniques
Flask deployment
End-to-end ML application development

Conclusion
This project demonstrates a complete end-to-end machine learning workflow for predicting customer credit risk. By integrating machine learning with a Flask web application, the system provides real-time predictions and simulates a simplified banking credit evaluation process.
