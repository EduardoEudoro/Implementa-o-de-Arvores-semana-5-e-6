import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_error


df = pd.read_csv('student_exam_scores.csv')

X = df.iloc[:, [1,2,3,4]]
y = df.iloc[:, 5]

X = pd.get_dummies(X, drop_first=False)

if y.dtype == 'O':
    raise ValueError("A coluna alvo (y) é categórica. Use RandomForestClassifier em vez de Regressor.")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

regressor = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    oob_score=True
)
regressor.fit(X_train, y_train)

print(f"OOB R^2: {regressor.oob_score_:.4f}")
print(f"Train MSE: {mean_squared_error(y_train, regressor.predict(X_train)):.4f}")
print(f"Test  MSE: {mean_squared_error(y_test,  regressor.predict(X_test)):.4f}")
print(f"Test   R² score: {r2_score(y_test, regressor.predict(X_test)):.4f}")
print(f"Test MAE: {mean_absolute_error(y_test, regressor.predict(X_test)):.4f}")


feature_1 = X.iloc[:, 0].values

X_grid = np.arange(min(feature_1), max(feature_1), 0.01).reshape(-1, 1)

X_full_grid = np.zeros((X_grid.shape[0], X.shape[1]))
X_full_grid[:, 0] = X_grid[:, 0]
