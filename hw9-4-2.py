#author CJP 1/19/2022
def products(num, val):
    for i, v in enumerate(num):
        num[i] = v * val
        v *= val
    return num

print(products([10, 6], 3))