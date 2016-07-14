# 6_5_replace.py

tmp = 0
beforefilepath = "D:/Python/Before.txt"
afterfilepath = "D:/Python/After.txt"

with open(beforefilepath, "r") as file:
    tmp = file.read()

print("변경하기 전\n")
print(tmp + "\n")

tmp = tmp.replace("\t", " " * 4)

print("변경 후\n")
print(tmp + "\n")

with open(afterfilepath, "w") as file:
    file.write(tmp)