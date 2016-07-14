# 6_4_memo.py

import os

def memo(_option, _text = ""):
    filepath = "D:/Python/memo.txt"
    if (_option == "r"):
        if os.path.exists(filepath):
            with open(filepath, _option) as file:
                return file.read()
        else:
            return "Error"
    else:
        with open(filepath, _option) as file:
            file.write(_text)

option = input("문서 편집 옵션을 입력하세요.(r, w, a)\n")
if option == "r":
    result = memo(option)
    print(result)
else:
    text = input("메모를 입력하세요.\n") + "\n"
    memo(option, text)