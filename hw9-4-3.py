#author CJP 1/19/2022
def count_e(num):
    x = 0
    for letter in num:
        if letter == "e":
           x += 1
    return x

print(count_e("therefore"))