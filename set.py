set_ = set()

set_.add("A")
set_.add("B")

print(set_)

# contains
print("A" in set_)

set_.remove("A")
print("A" in set_)

# clear
set_.clear()
print(set_)

# KeyError
set_.remove("C")

print(set_)