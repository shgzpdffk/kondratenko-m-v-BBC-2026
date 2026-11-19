import pandas as pd
import numpy as np 

df = pd.read_csv("/Users/shgzpdffk/Documents/kondratenko-m-v-BBC-2026/HW4/Titanic-Dataset.csv")

required = ["Age", "Sex", "Pclass", "Fare", "Embarked", "Cabin", "Survived"]
propusk = [prop for prop in required if prop not in df.columns]

print("Нет столбцов:", propusk)


n = int(input("сколько строк вывести? "))

print(df.head(n))
print(df.tail())
print("Возраст, среднее: ", df["Age"].mean(), "Медианное: ", df["Age"].median(), "Минимальное: ", df["Age"].min(), 'Максимальное: ', df["Age"].max(), "Стандартное отклонениe: ", df["Age"].std())
print("Стоимость билета, среднее: ", df["Fare"].mean(), "Медианное: ", df["Fare"].median(), "Минимальное: ", df["Fare"].min(), 'Максимальное: ', df["Fare"].max(), "Стандартное отклонениe: ", df["Fare"].std())
print("Количество братьев, сестёр и супругов, среднее: ", df["SibSp"].mean(), "Медианное: ", df["SibSp"].median(), "Минимальное: ", df["SibSp"].min(), 'Максимальное: ', df["SibSp"].max(), "Стандартное отклонениe: ", df["SibSp"].std())
print("Количество родителей и детей, среднее: ", df["Parch"].mean(), "Медианное: ", df["Parch"].median(), "Минимальное: ", df["Parch"].min(), 'Максимальное: ', df["Parch"].max(), "Стандартное отклонениe: ", df["Parch"].std())
print("Кол-во пассажиров 1-го класса: ", len(df[df["Pclass"] == 1]))
print("Кол-во пассажиров 2-го класса: ", len(df[df["Pclass"] == 2]))
print("Кол-во пассажиров 3-го класса: ", len(df[df["Pclass"] == 3]))
print("Кол-во уникальных портов: ", df["Embarked"].nunique())

for i in df:
    print("Кол-во пропусков в столбце", i, ":", df[i].isna().sum())
    print("Процент пропусков: ", df[i].isna().sum() / len(df[i])  * 100)

print("Максимальное кол-во пропусков в классе 'Cabin'")

iz_zn = df["Age"].notna().sum()
#print("Возраст, среднее: ", df["Age"].mean(), "Медианное: ", df["Age"].median(), "Минимальное: ", df["Age"].min(), 'Максимальное: ', df["Age"].max(), "Стандартное отклонениe: ", df["Age"].std(), iz_zn)

median_age = df["Age"].median()
df = df.fillna(median_age)

print("Возраст, среднее: ", df["Age"].mean(), "Медианное: ", df["Age"].median(), "Минимальное: ", df["Age"].min(), 'Максимальное: ', df["Age"].max(), "Стандартное отклонениe: ", df["Age"].std(), iz_zn)
#Возраст, среднее:  29.69911764705882 Медианное:  28.0 Минимальное:  0.42 Максимальное:  80.0 Стандартное отклонениe:  14.526497332334042 714
#Возраст, среднее:  29.36158249158249 Медианное:  28.0 Минимальное:  0.42 Максимальное:  80.0 Стандартное отклонениe:  13.019696550973201 714
#показатели до и после замены медианным

print("Неизвестен порт посадки: ", df["Embarked"].isna().sum())
df = df.dropna(subset = ["Embarked"])

prop_c = df["Cabin"].isna().sum() / len(df["Cabin"]) * 100
print(prop_c)
if prop_c >= 50:
    df = df.drop(columns = ["Cabin"])
    print("Столбец Cabin удален")

print("Оставшиеся пропуски:")
print(df.isna().sum())

age = df["Age"].to_numpy()
sex = df["Sex"].to_numpy()
fare = df["Fare"].to_numpy()
survived = df["Survived"].to_numpy()

total_surviviors = np.mean(survived) * 100
print("Процент выживших: ", total_surviviors)

#men = sex == 'male'
#women = sex == "female"

print("Выжило мужчин: ", np.nanmean(survived[sex == "male"]) * 100)
print("Выжило женщин: ", np.nanmean(survived[sex == "female"]) * 100)

print("Средний возраст мужчин: ", np.nanmean(age[sex == "male"]))
print("Средний возраст женщин: ", np.nanmean(age[sex == "female"]))

print("Средний возраст выживших мужчин: ", np.nanmean(age[(sex == "male") & (survived == 1)]))
print("Средний возраст погибших мужчин: ", np.nanmean(age[(sex == "male") & (survived == 0)]))

print("Средний возраст выживших женщин: ", np.nanmean(age[(sex == "female") & (survived == 1)]))
print("Средний возраст погибших женщин: ", np.nanmean(age[(sex == "female") & (survived == 0)]))

