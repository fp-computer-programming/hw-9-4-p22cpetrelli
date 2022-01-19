#author CJP 1/19/2022
def smash(lst):
    x = ""
    for i, v in enumerate(lst):
        if i == 0:
            x = x + v
        else:
            x = x + " " + v
    return x
print(smash(["My", "name", "is", "cam."]))

