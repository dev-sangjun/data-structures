dict_ = dict()
dict_["A"] = 1
dict_["B"] = 2

print(dict_["A"])

# contains keys
print("A" in dict_)

# contains values
print(1 in dict_.values())

# contains key, value
print("A" in dict_ and dict_["A"] == 1)

# clear
dict_.clear()
print(dict_)

# deletion
del dict_["A"]

# KeyError
print(dict_["A"])
