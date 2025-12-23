university = [
    {
        "name": "armin",
        "score": 14
    },
    {
        "name": "ashkan",
        "score": 20
    },
    {
        "name": "sina",
        "score": 20
    }
]

for x in university :
    print(x.items())
sum = 0
for i in university :
    y = i.get("score")
    sum += y
average = sum // len(university)
print(F"The average score of the students is {average}.")
