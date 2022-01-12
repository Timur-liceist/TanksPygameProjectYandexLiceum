import json

# with open('scoring.json') as cat_file:
test_sys = json.load(open('scoring.json', "r"))
# for key, value in data.items():
#     print(key, value)
points = 0
for t in test_sys["scoring"]:

    ind_group = 0
    test_group = t["required_tests"]
    test_points = t["points"]
    point_test = test_points / len(test_group)
    for ans in range(len(test_group)):
        if input() == "ok":
            points += point_test
print(int(points))
