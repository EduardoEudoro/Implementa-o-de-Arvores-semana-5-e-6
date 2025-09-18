import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

df = pd.read_csv("student_exam_scores.csv")

X = df.iloc[:, [1,2,3,4]]
y = df.iloc[:, 5]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

reg = DecisionTreeRegressor(random_state=42)
reg.fit(X_train, y_train)

y_train_pred = reg.predict(X_train)
y_test_pred = reg.predict(X_test)

print(f"Train MSE: {mean_squared_error(y_train, y_train_pred):.4f}")
print(f"Test  MSE: {mean_squared_error(y_test, y_test_pred):.4f}")
print(f"Test  MAE: {mean_absolute_error(y_test, y_test_pred):.4f}")
print(f"Test  R²:  {r2_score(y_test, y_test_pred):.4f}")
