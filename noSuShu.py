#!/usr/bin/evn python
def sushu(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
print filter(sushu,range(1,102))
