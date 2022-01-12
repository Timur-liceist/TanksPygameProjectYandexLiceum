from zipfile import ZipFile
import json
import os

answer = 0
with ZipFile("input.zip") as myzip:
    for el in myzip.infolist():
        if os.path.isfile(el.filename):
            # t = el.filename.split("/")[-1]
            # file = open(el.filename, "r")
            file = json.load(open(el.filename, "r"))
            for i in file:
                if i["city"] == "Москва" or i["city"] == "Moscow":
                    answer += 1
print(answer)
# for el in myzip.infolist():
#     sp = el.filename.split("/")
#     if sp[-1] == "":
#         sp.remove("")
#     s = ""
#     if os.path.isfile(sp[-1]):
#         print(1)
#         s = " " + str(human_read_format(os.path.getsize(sp[-1])))
#     print("  " * (len(sp) - 1) + sp[-1] + s)
