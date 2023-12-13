sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
x = sampleDict["class"]["student"]["marks"]["history"]
print(x)
print(sampleDict.get("class", "student"))
