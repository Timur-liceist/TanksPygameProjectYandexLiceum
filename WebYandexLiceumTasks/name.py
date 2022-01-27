# h = ""
# t = input()
# while t != "&":
#     h += t
#     t = input()
# print(h)
# print("\n"[-1])

# text = list(open(file, "r", encoding="utf8").read())
# text.remove("\n")
# answer = []
# for i in range(frame_frame_height):
#     # t = 0
#     stroka = ""
#     # if i == 5:
#     #     breakpoint()
#     while len(stroka) != frame_frame_width:
#         char = text.pop(0)
#         if char == "\n":
#             break
#         else:
#             stroka += char
#         # t += 1
#
#     # print(i, stroka)
#     answer.append(stroka)
# # print(answer)
# return "\n".join(answer)
# k = 0
# text = open(file, "r", encoding="utf8").read().split("\n")
# for stroka in text:  # file.readstroka()
#     for i in range(0, len(stroka), frame_width):
#         print(stroka[i:i + frame_width])
#         k += 1
#         if k >= frame_height:
#             return
#     else:
#         print()
#         k += 1
#         if k >= frame_height:
#             return