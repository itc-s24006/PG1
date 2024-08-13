import json


name_list = {
        'tanaka':{
            'age':20,
            'bloodtype':'A',
            'gender':'mele'
        },
        'satou':{
            'age':19,
            'bloodtype':'O',
            'gender':'femele'
        },
        'suzuki':{
            'age':20,
            'bloodtype':'AB',
            'gender':'mele'
        }
}

with open('name_list.json','w') as f1:
    json.dump(name_list, f1)

with open('name_list.json', 'r') as f2:
    name_list_l = json.load(f2)

for key, val in name_list_l.items():
    print(key, val)
