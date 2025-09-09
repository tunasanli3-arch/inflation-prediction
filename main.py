import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_excel('last_excel.xlsx')

df_transposed = df.transpose()
df_transposed2= df.transpose()

df_transposed.columns = df_transposed.iloc[0]
df_transposed = df_transposed[1:]

df_transposed.dropna(inplace=True)


#X = df_transposed[['PHR', 'PG', 'NM', 'GDP', 'GDPpc', 'GDPg', 'UR', 'PRr', 'Ihf', 'CGD', 'FDI']]  # Features
X = df_transposed[['GDP']]
y = df_transposed['I']  # Target variable

# Split the data into training and testing sets (90% training, 10% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=True)

# Initialize the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

print(y_test)
print(y_pred)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Predict inflation for the next year (2023)
# Assuming you have the variable values for 2022 stored in a list named 'values_2022'

predicted_inflation_2023 = model.predict([[25439700000000]])
print("Predicted inflation for 2023:", predicted_inflation_2023)

