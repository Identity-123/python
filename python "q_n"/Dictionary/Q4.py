employees = ["kelly", "Emma"]
defaults = {"destination": "Developer", "Salary": 8000}
new = dict.fromkeys(employees, defaults)
print(new)