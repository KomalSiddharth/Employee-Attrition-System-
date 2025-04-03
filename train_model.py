import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# load processed data
df=pd.read_csv('processed_data.csv')

# define feautres
X=df.drop('Attrition',axis=1)
y=df['Attrition']

# Train test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

# train the model
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

# save the model
pickle.dump(model,open("attrition_model.pkl","wb"))
print("Model train and saved successfully")