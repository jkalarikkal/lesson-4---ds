import pandas as pd 

data = pd.read_csv("titanic.csv")

adult_names = data.loc[data["Age"]>18, "Name"]
print(adult_names)

print(data.iloc[0:11, 2:5])

data.iloc[0:3,2] = 'Jaanvi'
print(data.iloc[0:3, 2])

data.to_csv("ChangedData.csv")
data["Inflated fare"] = data["Fare"] + 10

print(data.head())

data['profit'] = data["Fare"]* data["Pclass"]

print(data.head())


data_renamed = data.rename(
    columns = {
        "Fare" : "Monies",
        "Sex" : "Allocated Chromosomes"
    }
)

print(data_renamed)

print(data["Age"].mean())

print(data[["Age", "Fare"]].mean())

print(data.agg({
    "Age": ["min", "max", "median"],
    "Fare" : ["min", "max"]
}))

print(data.groupby("Sex")["Age"].mean())
print(data[["Sex", "Age"]].groupby("Sex").mean())