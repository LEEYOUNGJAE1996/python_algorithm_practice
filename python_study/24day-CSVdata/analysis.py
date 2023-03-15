import pandas

data = pandas.read_csv(
    "./python_study/24day-CSVdata/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
print(gray_squirrels)
print(black_squirrels)
print(cinnamon_squirrels)
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(len(data[data["Primary Fur Color"] == "Gray"]))

data_dictionary = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

df = pandas.DataFrame(data_dictionary)
df.to_csv('./python_study/24day-CSVdata/squirrel_count.csv')
