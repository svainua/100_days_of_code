import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# data_dict = {}

# data_dict["Fur Color"] = []
# data_dict["Count"] = []

# for color in data["Primary Fur Color"]:
#     if color not in data_dict["Fur Color"]:
#         data_dict["Fur Color"].append(color)
#         data_dict["Count"].append(len(data[data["Primary Fur Color"] == color]))

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


