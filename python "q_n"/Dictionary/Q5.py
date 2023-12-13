# we can do it using two methods: -

# Using dictionary comprehension
def dictionary_comprehension():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"

    }
    keys = ["name", "salary"]
    new_dict = {k: sample_dict[k] for k in keys}
    print(new_dict)


# using update()method and loop
def update_method():
    dict_1 = {
        "name": 'rajan',
        "age": 20,
        "salary": "error not found",
        "city": "bangaluru"
    }
    key = ['name', 'salary']
    res = {}
    for k in key:
        res.update({k: dict_1[k]})
    print(res)


dictionary_comprehension()
update_method()