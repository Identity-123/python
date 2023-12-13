# in python intersection it is same as we read in maths books
# let us consider we have name of people who know java and python
java = {"Rajan", "Sanjith", "Kushal", "Krishna"}
python = {"Sachin", "Roshan", "Rajan", "Sanjith"}
# It can be done by using two methods

# 1. Using set_1.intersection()
x = python.intersection(java)
print(x)

# 2. using "&"
intersection = java & python
print(intersection)