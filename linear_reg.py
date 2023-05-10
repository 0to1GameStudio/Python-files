import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
fueleconomy_df=pd.read_csv('c:/Users/Nikhil/Downloads/Share FuelEconomy.csv')
fueleconomy_df.head(100)
print(fueleconomy_df)
print(fueleconomy_df.describe())
print(fueleconomy_df.info())
sns.jointplot(x = 'Horse Power' ,y = 'Fuel Economy (MPG)',data= fueleconomy_df)
plt.show()
sns.pairplot(fueleconomy_df)
plt.show()
sns.lmplot(x = 'Horse Power' ,y = 'Fuel Economy (MPG)',data = fueleconomy_df)
plt.show()
x =fueleconomy_df[['Horse Power']]
y =fueleconomy_df[['Fuel Economy (MPG)']]
print(x)
print(y)
print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
print(x_train.shape)
print(x_test.shape)

from  sklearn.linear_model import LinearRegression
regressor = LinearRegression(fit_intercept= True)
regressor.fit(x_train,y_train)
print('Linear Model Coeff (m):',regressor.coef_)
print('Linear Model Coeff (b):',regressor.intercept_)

y_predict = regressor.predict(x_test)
print(y_predict)
print(y_test)
plt.scatter(x_train,y_train,color='gray')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.xlabel('Horse Power (HP)')
plt.ylabel('MPG')
plt.title('HP vs. MPG(training Set)')
plt.show()
plt.scatter(x_test,regressor.predict(x_test),color='blue')
plt.xlabel('Horse Power')
plt.ylabel('MPG')
plt.title('HP vs MPG(Testing Set)')
plt.show()
