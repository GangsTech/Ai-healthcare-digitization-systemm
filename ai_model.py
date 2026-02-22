import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    "age":[25,40,60,30,50,70],
    "bp":[120,140,160,130,150,170],
    "sugar":[90,160,200,110,180,220],
    "risk":[0,1,1,0,1,1]
})

X = data[["age","bp","sugar"]]
y = data["risk"]

model = LogisticRegression()
model.fit(X,y)

def predict(age,bp,sugar):
    return model.predict([[age,bp,sugar]])[0], model
