import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df=pd.read_csv("houseprices.csv",index_col=0)
df.columns=df.columns.str.strip()
df=df.reset_index(drop=True)
print(df)

reg=LinearRegression()
reg.fit(df[['beds','baths','size','zip_code']],df['price'])
prediction=reg.predict([[3,2,3000,9000]])
print("House price is:",prediction)

plt.scatter(df[['size']],df['price'])
plt.xlabel("Parameters")
plt.ylabel("Price")
plt.savefig("house_price.png")
plt.show()