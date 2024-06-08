# data = []
# with open("weather_data.csv") as file:
#     content = file.readlines()
#     for row in data:
#         stripped_row = row.strip("\n")
#         data.append(stripped_row)
# print(data)        


# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)    

import pandas
 
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()
# average_temp = round(sum(temp_list) / len(temp_list), 2)
# print(average_temp)

average_temp = data["temp"].mean()
#print(average_temp)
max_temp = data["temp"].max()
#print(max_temp)

######

#print(data["condition"])
#print(data.condition)

#### Get data in row

#print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])

monday = (data[data.day == "Monday"])
print(monday)
#print((monday.temp[0] * 9/5) + 32 )


##### Create Dataframe from Scratch

# data_dict = {
#     "students": ["Ira", "Vova", "Mark"],
#     "scores": [55, 66, 77]
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("new_data.csv")
