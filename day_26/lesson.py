# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {key:len(key) for key in sentence.split()}
# print(result)

#################
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {key:(value * 9/5) + 32 for (key, value) in weather_c.items()}
# print(weather_f)

#################
student_dict = {
    "student": ["Ira", "Vova", "Mark"],
    "score": [55, 66, 77]
}
# Loop through the dict
# for (key, value) in student_dict.items():
#     print(value)

import pandas

df = pandas.DataFrame(student_dict)
print(df)

#Loop through the DF
# for (key, value) in df.items():
#     #print(key)
#     print(value)

# Loop through rows of a DF

for index, row in df.iterrows():
    #print(index)
    print(row.student)
    if row.student == "Ira":
        print(row.score)
