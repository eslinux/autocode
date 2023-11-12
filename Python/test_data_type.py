

#List
my_list = list() # or []
my_list.append(1)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append("hihi")
print(my_list) #[1, 1, 2, 3, 4, 'hihi']


#Set
my_set = set() #or {}
my_set.add(1)
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add("hihi")
print(my_set) #{1, 2, 3, 4, 'hihi'}


#Dict
my_dict = dict()
my_dict["name"] = "Ninh"
my_dict["age"] = 35
my_dict["is_ok"] = True
print(my_dict) #{'name': 'Ninh', 'age': 35, 'is_ok': True}


if "Ninh" == "NINH":
    print("Dung")
else:
    print("sai") #go to here
