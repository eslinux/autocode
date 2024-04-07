
# https://docs.python.org/3/library/re.html


import re

def test():
    pattern = r"^Hello"
    string = "Hello, world!"

    isMatch = re.match(pattern, string)
    if isMatch:
        print("Match !")
    else:
        print("Not match !")

if __name__ == '__main__':
    test()


