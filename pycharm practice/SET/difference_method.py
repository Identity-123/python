java = {"Rajan", "Sanjith", "Kushal", "Krishna"}
python = {"Sachin", "Roshan", "Rajan", "Sanjith"}

# there are two methods for difference
# 1. set1.difference(set2): -


diff = python.difference(java)
# The above code will show the elements that are present only in python

diff_0 = java.difference(python)
# the above code will only show the elements only presented in java

print(diff)
print(diff_0)

# second methods: - using "-" symbol
differencePython = python-java
differenceJava = java-python
print(differencePython)
print(differenceJava)
