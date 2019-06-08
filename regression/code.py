# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df = pd.read_csv(path)
print(df.head())
X = df.iloc[:, df.columns != 'list_price']
#print(X.head())
y = df.iloc[:,1]
#print(y.head())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)
#print(X_train.head())

# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = X_train.columns
fig, axes = plt.subplots(nrows = 3, ncols = 3)
for i in range(0,3):
    for j in range(0,3):
        col = cols[i * 3 + j]
        axes[i,j].scatter(X_train[col], y_train)


# code ends here



# --------------
# Code starts here
import seaborn as sns
corr = X_train.corr()
plt.figure(figsize=(10,10))
ax = sns.heatmap(corr,linewidth=0.5,vmin=-1, cmap='coolwarm',annot=True)
plt.show()
#print(corr)
X_train.drop(columns=['play_star_rating', 'val_star_rating'], axis=1, inplace=True)
X_test.drop(columns=['play_star_rating', 'val_star_rating'], axis=1, inplace=True)

print(X_train.shape)
print(X_test.shape)
# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error: ', mse)
r2 = r2_score(y_test, y_pred)
print('R-squared error : ',r2)



# Code ends here


# --------------
# Code starts here
residual = y_test - y_pred

plt.hist(residual)

# Code ends here


