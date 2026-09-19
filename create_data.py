import pandas as pd

# DataFrame
table1 = pd.DataFrame({"yes": [12, 13], "no": [45, 67]})
print(table1)

table2 = pd.DataFrame(
    {
        "Saikat": ["I am a boy", "I like mango"],
        "Tisha": ["I am a girl", "I like mango too"],
    }
)
print(table2)

table3 = pd.DataFrame(
    {"Bob": ["Hola", "Hello"], "Sue": ["Hi", "Adab"]}, index=["PersonA", "PersonB"]
)
print(table3)

# Series
list = pd.Series([1, 2, 3, 4, 5, 6, 7])
print(list)

list1 = pd.Series(
    [30, 40, 50], index=["2017 Sales", "2018 Sales", "2019 Sales"], name="Product A"
)
print(list1)
