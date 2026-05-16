import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv('dataset/german_credit_data.csv')

# Drop unnecessary column if present
if 'Unnamed: 0' in df.columns:
    df.drop('Unnamed: 0', axis=1, inplace=True)

# Fill missing values
df['Saving accounts'] = df['Saving accounts'].fillna('unknown')
df['Checking account'] = df['Checking account'].fillna('unknown')

# Convert target variable
df['Risk'] = df['Risk'].map({
    'good': 0,
    'bad': 1
})

# Features and target
X = df.drop('Risk', axis=1)
y = df['Risk']

# Numerical columns
numeric_features = [
    'Age',
    'Job',
    'Credit amount',
    'Duration'
]

# Categorical columns
categorical_features = [
    'Sex',
    'Housing',
    'Saving accounts',
    'Checking account',
    'Purpose'
]

# Preprocessing
preprocessor = ColumnTransformer([
    (
        'num',
        StandardScaler(),
        numeric_features
    ),
    (
        'cat',
        OneHotEncoder(handle_unknown='ignore'),
        categorical_features
    )
])

# Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    (
        'classifier',
        RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
    )
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
pipeline.fit(X_train, y_train)

# Save complete pipeline
joblib.dump(
    pipeline,
    'saved_model/credit_pipeline.pkl'
)

print("Pipeline trained and saved successfully.")