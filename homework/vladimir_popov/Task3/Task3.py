

my_dict = {"tuple": (1, 2, 2, 3, 5), "list": [1, 2, 3, 4, 5], "dict": 
           {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}, "set": {1, 2, 3, 4, 5}
           }

print(my_dict["tuple"][-1])
my_dict["list"].append(6)
my_dict["list"].pop(1)
my_dict["dict"]["i am a tuple"] = 333
del my_dict["dict"]["one"]
my_dict["set"].remove(3)
my_dict["set"].add(6)
print(my_dict)