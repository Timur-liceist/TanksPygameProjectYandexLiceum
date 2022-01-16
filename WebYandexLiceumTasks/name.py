import os


def human_read_format(size):
    s = 1024
    indexes = ["Б", "КБ", "МБ", "ГБ"]
    index = 0
    while size >= s:
        size /= 1024
        index += 1
    return f"{round(size)}{indexes[index]}"


def get_size_of_dir(dirname):
    answer = 0
    for dirpath, dirnames, filenames in os.walk(dirname):
        if filenames:
            # print(rf"{dirpath}\{filenames[0]}")
            answer += os.path.getsize(rf"{dirpath}\{filenames[0]}")
    return answer
    # for i in filenames:
    # print(os.path.getsize("/".join(dirp)))


spisok = sorted([(i, get_size_of_dir(i)) for i in os.listdir() if os.path.isdir(i)], reverse=True)
spisok = list(map(lambda x: (x[0], human_read_format(x[1])), spisok))
for i in spisok:
    print(i[0] + "\t" * 8 + i[1])
