dict_ = dict()
dict_["A"] = 1
dict_["B"] = 2

print(dict_["A"])

dict_.clear()
print(dict_)

# deletion
del dict_["A"]

# KeyError
print(dict_["A"])
