# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random
import string

def generate_code(count, length):
    forSelect = string.ascii_letters + string.digits
    arr = []
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        arr.append(Re)
        # print(Re)   
    return arr 


if __name__ == '__main__':
    arr = generate_code(200,20)

    for key, v in enumerate(arr):
        print(key,v)
