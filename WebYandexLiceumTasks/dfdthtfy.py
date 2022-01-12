from zipfile import ZipFile
import os


def human_read_format(size):
    s = 1024
    indexes = ["Б", "КБ", "МБ", "ГБ"]
    index = 0
    while size >= s:
        size /= 1024
        index += 1
    return f"{round(size)}{indexes[index]}"


with ZipFile("input.zip") as myzip:
    for el in myzip.infolist():
        sp = el.filename.split("/")
        if sp[-1] == "":
            sp.remove("")
        s = ""
        if el.filename.split("/")[-1] != "":
            # try:
            #     s = " " + str(human_read_format(os.path.getsize(sp[-1])))
            # except Exception:
            #     pass
            s = " " + str(human_read_format(os.path.getsize(el.filename)))
        print("  " * (len(sp) - 1) + sp[-1] + s)
