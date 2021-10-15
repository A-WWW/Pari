from pymongo import MongoClient
from bson.objectid import ObjectId
import csv

cluster = MongoClient("mongodb+srv://A-WWW:32125M32125@cluster0.0b6py.mongodb.net/School?retryWrites=true&w=majority")
db = cluster["School"]
collection = db["Pari"]

# проверка кодировки
with open('isxod.csv') as f:
    print(f)
data = []
g=[]
results = []
with open('isxod.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
a = dict.fromkeys(data.pop(0))
print(a)
# не понимая общей задачи тяжело ообратить внимание на что-то конкретное (подобрать разделение по конкретным нужным разделителям  и т.д)
# , но по ходу работы с кодом могу сказать, что основная проблема была при скачивании изночальных данных с базы, получилося рельный "суп"
# в котором потом  необходимо  возится с кодом
data_sort = [i[0].split(',') for i in data]
for i in range(len(data_sort)):
    b = {'id': data_sort[i][0]}
    b['alert_id'] = data_sort[i][1]
    for j in range(len(data_sort[i])):
        if data_sort[i][j].isalpha() and len(data_sort[i][j]) == 2:
            if data_sort[i][j].islower():
                b['language'] = data_sort[i][j]
            if data_sort[i][j].isupper():
                b['country'] = data_sort[i][j]
            else:
                b['country'] = "None"
        if data_sort[i][j].startswith('https'):
            print(data_sort[i][j])
    b['title/description'] = str(data_sort[i][3].replace('"',"") + data_sort[i][4].replace('"',""))
    b['score'] = data_sort[i][-3]
    b['alert_name'] = data_sort[i][-1].replace('"',"") + (data_sort[i][-2].replace('"',""))
    g.append(b)

# for i in data:
#     print(i)
for i in g:
    print(i)
# for i in data_sort:
#     print(i)




class Database:

    def __init__(self, data):
        self.data = data

    def database(self):
        collection.insert_many(self.data)

    def database_c(self):
        for i in list(collection.find({})):
            print(i)
test=Database(g)
test.database()
test.database_c()







