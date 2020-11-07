# if...else敘述
print("奇偶數判斷")
num = input("請輸入數字:")
rem = int(num) % 2
# 傳統寫法
if (rem == 0):
    print("%d 是偶數" % int(num))
else:
    print("%d 是奇數" % int(num))
# PEP 8
if rem:
    print("%d 是偶數" % int(num))
else:
    print("%d 是奇數" % int(num))
# 高手用法
print("%d 是奇數" % int(num) if rem else "%d 是偶數" % int(num))

x, y = eval(input("輸入兩個數字:"))
max_ = x if x > y else y
print("方法一最大值:", max_)
max_ = max(x, y)
print("方法二最大值:", max_)
min_ = x if x < y else y
print("方法一最小值:", min_)
min_ = min(x, y)
print("方法二最小值:", min_)

