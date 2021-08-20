import sys

def t():
    print("t")


def h():
    print("help")


com = sys.argv[1]
if com == "t":
    t()
elif com == "h":
    h()
else:
    print("error")
