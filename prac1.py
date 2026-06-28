# House price prediction

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , mean_squared_error , r2_score

data = pd.read_csv("C:\\Users\\Wick\\Documents\\MLdocs\\Housing.csv")

print(data.head())
# Convert categorical columns
data["mainroad"] = data["mainroad"].map({"yes":1,"no":0})
data["guestroom"] = data["guestroom"].map({"yes":1,"no":0})
data["basement"] = data["basement"].map({"yes":1,"no":0})
data["hotwaterheating"] = data["hotwaterheating"].map({"yes":1,"no":0})
data["airconditioning"] = data["airconditioning"].map({"yes":1,"no":0})

x =  data[['area','bedrooms','bathrooms','stories',
          'mainroad','guestroom','basement',
          'hotwaterheating','airconditioning','parking']]

y = data[['price']]

model = LinearRegression()

x_train , x_test , y_train , y_test = train_test_split(
    x,y, test_size=0.2 , random_state=42
)
model.fit(x_train , y_train)

predicted_price = model.predict(x_test)

mae = mean_absolute_error(y_test, predicted_price)
mse = mean_squared_error(y_test, predicted_price)
r2 = r2_score(y_test , predicted_price)

print("Mean Absolute Error:" , mae)
print("Mean Squared Error:", mse)
print("R² Score:", r2)

new_data = [[8664,6,2,1,1,0,0,1,1,5]]
predicted_new = model.predict(new_data)

print(f"Predicted House Price: ₹{predicted_new[0][0]:,.2f}")



plt.figure(figsize=(8,6))

plt.hist(data["price"], bins=20)

plt.xlabel("Price")
plt.ylabel("Number of Houses")

plt.title("Distribution of House Prices")

plt.show()

