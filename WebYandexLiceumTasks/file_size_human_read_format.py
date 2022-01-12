import os


def human_read_format(size):
    s = 1024
    indexes = ["Б", "КБ", "МБ", "ГБ"]
    index = 0
    while size >= s:
        size /= 1024
        index += 1
    return f"{round(size)}{indexes[index]}"


def get_files_sizes():
    files = os.listdir()
    answer = []
    for i in files:
        if os.path.isfile(i):
            answer.append(f"{i} {human_read_format(os.path.getsize(i))}")
    return "\n".join(answer)
