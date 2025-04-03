import pandas as pd
df=pd.read_csv('Employee Attrition System/Employee Attrition System.csv')
df['Attrition']=df['Attrition'].map({"Yes":1,"No":0})
selected_features=["Age", "MonthlyIncome", "JobSatisfaction", "WorkLifeBalance", "YearsAtCompany", "Attrition"]
df = df[selected_features]
df.to_csv("processed_data.csv", index=False)
print("✅ Data Preprocessed & Saved Successfully!")